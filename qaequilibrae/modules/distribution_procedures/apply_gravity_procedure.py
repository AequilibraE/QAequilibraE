from aequilibrae.distribution import GravityApplication
from aequilibrae.utils.worker_thread import WorkerThread
from qgis.PyQt.QtCore import *


class ApplyGravityProcedure(WorkerThread):
    def __init__(self, parentThread, **kwargs):
        WorkerThread.__init__(self, parentThread)
        self.gravity = GravityApplication(**kwargs)
        self.error = None
        self.output = None
        self.report = []

    def doWork(self):
        try:
            self.gravity.apply()
            self.output = self.gravity.output
            self.report = self.gravity.report
        except ValueError as e:
            self.error = e
        self.jobFinished.emit("apply_gravity")
