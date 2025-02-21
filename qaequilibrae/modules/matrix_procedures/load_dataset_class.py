import struct

import numpy as np
import pandas as pd
from aequilibrae.utils.interface.worker_thread import WorkerThread
from qgis.PyQt.QtCore import pyqtSignal, QVariant

from qaequilibrae.modules.common_tools.global_parameters import float_types, string_types, integer_types


class LoadDataset(WorkerThread):
    signal = pyqtSignal(object)

    def __init__(self, parent_thread, layer, index_field, fields, file_name):
        WorkerThread.__init__(self, parent_thread)
        self.layer = layer
        self.index_field = index_field
        self.fields = fields
        self.error = None
        self.python_version = 8 * struct.calcsize("P")
        self.output = pd.DataFrame([])
        self.output_name = file_name

    def doWork(self):
        feat_count = self.layer.featureCount()
        self.signal.emit(["start", feat_count, f"Total features: {feat_count}"])

        # Create specification for the output file
        datafile_spec = {"entries": feat_count}
        if self.output_name is None:
            datafile_spec["memory_mode"] = True
        else:
            datafile_spec["memory_mode"] = False
        fields = []
        types = []
        idxs = []
        empties = []
        for field in self.layer.dataProvider().fields().toList():
            if field.name() in self.fields:
                if field.type() in integer_types:
                    types.append("<i8")
                    empties.append(np.iinfo(np.int64).min)
                elif field.type() in float_types:
                    types.append("<f8")
                    empties.append(np.nan)
                elif field.type() in string_types:
                    types.append("S" + str(field.length()))
                    empties.append("")
                else:
                    self.error = self.tr("Field {} does has a type not supported.").format(str(field.name()))
                    break
                fields.append(str(field.name()))
                idxs.append(self.layer.dataProvider().fieldNameIndex(field.name()))

        datafile_spec["field_names"] = fields
        datafile_spec["data_types"] = types
        datafile_spec["file_path"] = self.output_name

        if self.error is None:

            # Get all the data
            for p, feat in enumerate(self.layer.getFeatures()):
                for idx, field, empty in zip(idxs, fields, empties):
                    if feat.attributes()[idx] == QVariant():
                        self.output.loc[p, field] = empty
                    else:
                        self.output.loc[p, field] = feat.attributes()[idx]
                self.signal.emit(["update", p, f"Feature count: {p}"])
            self.output.set_index(self.index_field, inplace=True)

        self.signal.emit(["set_text", feat_count])
        self.signal.emit(["finished"])
