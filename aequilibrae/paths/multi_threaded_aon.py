import numpy as np


class MultiThreadedAoN:
    def __init__(self):
        self.predecessors = None  # The predecessors for each node in the graph
        self.temporary_skims = None  # holds the skims for all nodes in the network (during path finding)
        self.reached_first = None    # Keeps the order in which the nodes were reached for the cascading network loading
        self.connectors = None  # The previous link for each node in the tree
        self.temp_link_loads = None  # Temporary results for assignment. Necessary for parallelization
        self.temp_node_loads = None  # Temporary nodes for assignment. Necessary for cascading

    # In case we want to do by hand, we can prepare each method individually
    def prepare(self, results):
        self.predecessors = np.zeros((results.nodes, results.cores), dtype=np.int32)
        self.temporary_skims = np.zeros((results.nodes, results.num_skims, results.cores), np.float64)
        self.reached_first = np.zeros((results.nodes, results.cores), dtype=np.int32)
        self.connectors = np.zeros((results.nodes, results.cores), dtype=np.int32)
        self.temp_link_loads = np.zeros((results.links, results.cores), np.float64)
        self.temp_node_loads = np.zeros((results.nodes, results.cores), np.float64)