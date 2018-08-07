"""
 -----------------------------------------------------------------------------------------------------------
 Package:    AequilibraE

 Name:       Network preparation
 Purpose:    Prepares networks (extracting nodes A and B from links) on a separate thread

 Original Author:  Pedro Camargo (c@margo.co)
 Contributors:
 Last edited by: Pedro Camargo

 Website:    www.AequilibraE.com
 Repository:  https://github.com/AequilibraE/AequilibraE

 Created:    2014-03-19
 Updated:    21/12/2016
 Copyright:   (c) AequilibraE authors
 Licence:     See LICENSE.TXT
 -----------------------------------------------------------------------------------------------------------
 """

from qgis.core import *
from qgis.PyQt.QtCore import *
import numpy as np
from ..common_tools.auxiliary_functions import *
from ..common_tools import WorkerThread
from ..common_tools.global_parameters import *

class NetworkPreparationProcedure(WorkerThread):
    def __init__(self, parentThread, line_layer, new_line_layer, node_layer=False, node_ids=False,
                 new_node_layer=False, node_start=0):

        WorkerThread.__init__(self, parentThread)
        self.line_layer = line_layer
        self.node_layer = node_layer
        self.node_ids = node_ids
        self.new_node_layer = new_node_layer
        self.new_line_layer = new_line_layer
        self.node_start = node_start
        self.error = None
        self.report = []

    def doWork(self):
        line_layer = self.line_layer
        node_layer = self.node_layer
        node_ids = self.node_ids
        layer = get_vector_layer_by_name(line_layer)
        feat_count = layer.featureCount()

        self.ProgressMaxValue.emit(3)
        self.ProgressValue.emit(0)
        self.ProgressText.emit("Duplicating line layer")

        P = 0
        # We create the new line layer and load it in memory
        epsg_code = int(layer.crs().authid().split(":")[1])
        new_line_layer = self.duplicate_layer(layer, 'Linestring', self.new_line_layer)
        self.ProgressValue.emit(1)

        # Add the A_Node and B_node fields to the layer
        field_names = [x.name().upper() for x in new_line_layer.dataProvider().fields().toList()]
        add_fields = ['A_NODE', 'B_NODE']
        for f in add_fields:
            if f not in field_names:
                res = new_line_layer.dataProvider().addAttributes([QgsField(f, QVariant.Int)])
        new_line_layer.updateFields()
        self.ProgressValue.emit(2)
        # I f we have node IDs, we iterate over the ID field to make sure they are unique
        ids = []

        if node_ids:
            nodes = get_vector_layer_by_name(node_layer)
            index = QgsSpatialIndex()
            idx = nodes.dataProvider().fieldNameIndex(node_ids)

            self.ProgressMaxValue.emit(nodes.featureCount())
            self.ProgressValue.emit(0)

            for P, feat in enumerate(nodes.getFeatures()):
                self.ProgressText.emit("Checking node layer: " + str(P) + "/" + str(nodes.featureCount()))
                self.ProgressValue.emit(P)
                index.insertFeature(feat)
                i_d = feat.attributes()[idx]
                if i_d in ids:
                    self.error = "ID " + str(i_d) + ' is non unique in your selected field'
                    self.report.append(self.error)
                if i_d < 0:
                    self.error = "Negative node ID in your selected field"
                    self.report.append(self.error)
                    break
                ids.append(i_d)

            if self.error is None:
                self.ProgressMaxValue.emit(new_line_layer.featureCount())
                P = 0
                for feat in new_line_layer.getFeatures():
                    P += 1
                    self.ProgressValue.emit(int(P))
                    self.ProgressText.emit("Processing links: " + str(P) + "/" + str(feat_count))

                    # We search for matches for all AB nodes
                    ab_nodes = [('A_NODE', 0), ('B_NODE', -1)]
                    for field, position in ab_nodes:
                        node_ab = list(feat.geometry().asPolyline())[position]
                        # We compute the closest node
                        nearest = index.nearestNeighbor(QgsPointXY(node_ab), 1)

                        # We get coordinates on this node
                        fid = nearest[0]
                        nfeat = nodes.getFeatures(QgsFeatureRequest(fid)).__next__()
                        nf = nfeat.geometry().asPoint()

                        fid = new_line_layer.dataProvider().fieldNameIndex(field)

                        if round(nf[0], 10) == round(node_ab[0], 10) and round(nf[1], 10) == round(node_ab[1], 10):
                            ids = nfeat.attributes()[idx]
                            new_line_layer.dataProvider().changeAttributeValues({feat.id(): {fid: int(ids)}})

                        else: # If not, we throw an error
                            self.error = 'CORRESPONDING NODE NOTE FOUND. Link: ' + str(feat.attributes())
                            self.report.append(self.error)
                            break
                    if self.error is not None:
                        break

                    new_line_layer.commitChanges()
                    self.new_line_layer = new_line_layer
        else:
            self.ProgressMaxValue.emit(feat_count)
            #  Create node layer
            new_node_layer = QgsVectorLayer('Point?crs=epsg:' + str(epsg_code) + '&field=ID:integer', self.new_node_layer, "memory")
            DTYPE = [('LAT', np.float64), ('LONG', np.float64), ('LINK ID', np.int64),
                     ('POSITION', np.int64), ('NODE ID', np.int64)]

            all_nodes = np.zeros(feat_count * 2, dtype=DTYPE)

            l = 0
            #  Let's read all links and the coordinates for their extremities
            for feat in new_line_layer.getFeatures():
                P += 1
                if P % 500 == 0:
                    self.ProgressValue.emit(int(P))
                    self.ProgressText.emit("Links read: " + str(P) + "/" + str(feat_count))

                link = list(feat.geometry().asPolyline())
                if link:
                    link_id = feat.id()

                    node_a = (round(link[0][0], 10), round(link[0][1], 10))
                    node_b = (round(link[-1][0], 10), round(link[-1][1], 10))

                    all_nodes[l][0] = node_a[0]
                    all_nodes[l][1] = node_a[1]
                    all_nodes[l][2] = link_id
                    all_nodes[l][3] = 0
                    l += 1
                    all_nodes[l][0] = node_b[0]
                    all_nodes[l][1] = node_b[1]
                    all_nodes[l][2] = link_id
                    all_nodes[l][3] = 1
                    l += 1

            # Now we sort the nodes and assign IDs to them
            all_nodes = np.sort(all_nodes, order=['LAT', 'LONG'])

            lat0 = -100000.0
            longit0 = -100000.0
            incremental_ids = self.node_start - 1
            P = 0

            self.ProgressMaxValue.emit(feat_count * 2)
            self.ProgressText.emit("Computing node IDs: " + str(0)+"/" + str(feat_count * 2))
            self.ProgressMaxValue.emit(feat_count * 2)

            for i in all_nodes:
                P += 1
                lat, longit, link_id, position, node_id = i

                if lat != lat0 or longit != longit0:
                    incremental_ids += 1
                    lat0 = lat
                    longit0 = longit

                i[4] = incremental_ids

                if P % 2000 == 0:
                    self.ProgressValue.emit(int(P))
                    self.ProgressText.emit("Computing node IDs: " + str(P) + "/" + str(feat_count * 2))

            self.ProgressValue.emit(int(feat_count * 2))
            self.ProgressText.emit("Computing node IDs: " + str(feat_count * 2)+"/" + str(feat_count * 2))

            # And we write the node layer as well
            node_id0 = -1
            P = 0
            self.ProgressMaxValue.emit(incremental_ids)
            cfeatures = []
            for i in all_nodes:
                lat, longit, link_id, position, node_id = i

                if node_id != node_id0:
                    P += 1
                    feature = QgsFeature()
                    feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(lat, longit)))
                    feature.setAttributes([int(node_id)])
                    cfeatures.append(feature)
#                    new_node_layer.dataProvider().addFeatures([feature])
                    node_id0 = node_id

                if P % 500 == 0:
                    self.ProgressValue.emit(int(P))
                    self.ProgressText.emit("Writing new node layer: " + str(P) + "/" + str(incremental_ids))

            a = new_node_layer.dataProvider().addFeatures(cfeatures)
            del cfeatures
            new_node_layer.commitChanges()
            self.ProgressValue.emit(int(incremental_ids))
            self.ProgressText.emit("Writing new node layer: " + str(incremental_ids) + "/" + str(incremental_ids))

            # Now we write all the node _IDs back to the line layer
            P = 0
            self.ProgressText.emit("Writing node IDs to links: " + str(0) + "/" + str(feat_count * 2))

            self.ProgressMaxValue.emit(feat_count * 2)
            fid1 = new_line_layer.dataProvider().fieldNameIndex("A_NODE")
            fid2 = new_line_layer.dataProvider().fieldNameIndex("B_NODE")

            for i in all_nodes:
                P += 1
                lat, longit, link_id, position, node_id = i

                if position == 0:
                    new_line_layer.dataProvider().changeAttributeValues({int(link_id): {fid1: int(node_id)}})
                else:
                    new_line_layer.dataProvider().changeAttributeValues({int(link_id): {fid2: int(node_id)}})

                if P % 50 == 0:
                    self.ProgressValue.emit(int(P))
                    self.ProgressText.emit("Writing node IDs to links: " + str(P) + "/" + str(feat_count * 2))

            self.ProgressValue.emit(int(P))
            self.ProgressText.emit("Writing node IDs to links: " + str(P)+"/" + str(feat_count * 2))

            new_line_layer.commitChanges()
            self.new_line_layer = new_line_layer

            self.new_node_layer = new_node_layer

        self.ProgressText.emit("DONE")

    def duplicate_layer(self, original_layer, layer_type, layer_name):
        epsg_code = int(original_layer.crs().authid().split(":")[1])
        feats = [feat for feat in original_layer.getFeatures()]
        duplicate_layer = QgsVectorLayer(layer_type + "?crs=epsg:" + str(epsg_code), layer_name, "memory")
        new_layer_data = duplicate_layer.dataProvider()
        attr = original_layer.dataProvider().fields().toList()
        new_layer_data.addAttributes(attr)
        duplicate_layer.updateFields()
        new_layer_data.addFeatures(feats)
        del feats
        return duplicate_layer