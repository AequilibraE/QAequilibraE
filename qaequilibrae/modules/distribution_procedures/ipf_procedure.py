from aequilibrae.distribution import Ipf
from aequilibrae.utils.interface.worker_thread import WorkerThread
from PyQt5.QtCore import pyqtSignal


class IpfProcedure(WorkerThread):
    signal = pyqtSignal(object)

    def __init__(self, parentThread, **kwargs):
        WorkerThread.__init__(self, parentThread)
        self.ipf = Ipf(**kwargs)
        self.error = None
        self.output = None
        self.report = []

    def doWork(self):
        self.ipf.fit()
        self.report = self.ipf.report
        self.output = self.ipf.output
        self.signal.emit(["finished"])
