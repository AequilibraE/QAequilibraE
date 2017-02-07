import multiprocessing as mp
import numpy as np
import warnings
import sqlite3
import sys
import os
from memory_mapped_files_handling import saveDataFileDictionary


class AssignmentResults:
    def __init__(self):
        """
        @type graph: Set of numpy arrays to store Computation results
        self.critical={required:{"links":[lnk_id1, lnk_id2, ..., lnk_idn], "path file": False}, results:{}}
        """
        self.link_loads = None       # The actual results for assignment
        self.skims = None            # The array of skims
        self.no_path = None          # The list os paths
        self.num_skims = None        # number of skims that will be computed. Depends on the setting of the graph provided
        self.cores = mp.cpu_count()

        self.critical_links = {'save': False,
                               'queries': {},  # Queries are a dictionary
                               'results': False}

        self.link_extraction = {"save": False,
                                'queries': {},  # Queries are a dictionary
                                "output": None}

        self.path_file = {"save": False,
                          "results": None}

        self.nodes = -1
        self.zones = -1
        self.links = -1
        self.__graph_id__ = None

        self.lids = None
        self.direcs = None

        # We set the critical analysis, link extraction and path file saving to False

    # In case we want to do by hand, we can prepare each method individually
    def prepare(self, graph):

        self.nodes = graph.num_nodes + 1
        self.zones = graph.centroids + 1
        self.links = graph.num_links + 1
        self.num_skims = graph.skims.shape[1]

        self.lids = graph.graph['link_id']
        self.direcs = graph.graph['direction']
        self.__redim()
        self.__graph_id__ = graph.__id__

        self.setSavePathFile(False)
        self.setCriticalLinks(False)

    def reset(self):
        if self.link_loads is not None:
            self.skims.fill(0)
            self.no_path.fill(-1)
        else:
            print 'Exception: Assignment results object was not yet prepared/initialized'

    def __redim(self):
        self.link_loads = np.zeros(self.links, np.float64)
        self.skims = np.zeros((self.zones, self.zones, self.num_skims), np.float64)
        self.no_path = np.zeros((self.zones, self.zones), dtype=np.int32)

        self.reset()

    def set_cores(self, cores):
        if isinstance(cores, int):
            if cores > 0:
                if self.cores != cores:
                    self.cores = cores
                    if self.link_loads is not None:
                        self.__redim()
            else:
                raise ValueError("Number of cores needs to be equal or bigger than one")
        else:
            raise ValueError("Number of cores needs to be an integer")

    def setCriticalLinks(self, save=False, queries={}, crit_res_result=None):
        a = np.zeros((max(1,self.zones), 2, 2), dtype=np.float64)
        if save:
            if crit_res_result is None:
                warnings.warn("Critical Link analysis not set properly. Need to specify output file too")
            else:
                if crit_res_result[-3:].lower() != 'aes':
                    dictio_name = crit_res_result + '.aed'
                    crit_res_result += '.aes'
                else:
                    dictio_name = crit_res_result[:-3] + 'aed'

                if self.nodes > 0 and self.zones > 0:
                    if ['elements', 'labels', 'type'] in queries.keys():
                        if len(queries['labels']) == len(queries['elements']) == len(queries['type']):
                            num_queries = len(queries['labels'])
                            a = np.memmap(crit_res_result, dtype=np.float64, mode='w+', shape=(self.zones,self.zones, num_queries))
                            saveDataFileDictionary(self.__graph_id__,'critical link analysis', [int(x) for x in a.shape[:]], dictio_name)
                        else:
                            raise ValueError("Queries are inconsistent. 'Labels', 'elements' and 'type' need to have same dimensions")
                    else:
                        raise ValueError("Queries are inconsistent. It needs to contain the following elements: 'Labels', 'elements' and 'type'")

        self.critical_links = {'save': save,
                               'queries': queries,
                               'results': a
                               }

    def setSavePathFile(self, save=False, path_result=None):
        a = np.zeros((max(1,self.zones), 1, 2), dtype=np.int32)
        if save:
            if path_result is None:
                warnings.warn("Path file not set properly. Need to specify output file too")
            else:
                if path_result[-3:].lower() != 'aep':
                    dictio_name = path_result + '.aed'
                    path_result += '.aep'
                else:
                    dictio_name = path_result[:-3] + 'aed'

                if self.nodes > 0 and self.zones > 0:
                    a = np.memmap(path_result, dtype=np.int32, mode='w+', shape=(self.zones,self.nodes, 2))
                    saveDataFileDictionary(self.__graph_id__,'path file', [int(x) for x in a.shape[:]], dictio_name)

        self.path_file = {'save': save,
                          'results': a
                          }

    def save_loads_to_disk(self, output_file, file_type=None):

        dt = [('Link ID', np.int), ('AB Flow', np.float), ('BA Flow', np.float), ('Tot Flow', np.float)]
        res = np.zeros(np.max(self.lids) + 1, dtype=dt)

        res['Link ID'][:] = np.arange(np.max(self.lids) + 1)[:]

        # Indices of links BA and AB
        ABs = self.direcs < 0
        BAs = self.direcs > 0

        link_flows = self.results()[:-1]

        # AB Flows
        link_ids = self.lids[ABs]
        res['AB Flow'][link_ids] = link_flows[ABs]

        # BA Flows
        link_ids = self.lids[BAs]
        res['BA Flow'][link_ids] = link_flows[BAs]

        # Tot Flow
        res['Tot Flow'] = res['AB Flow'] + res['BA Flow']

        if file_type is None:
            # Guess file type
            if output_file[-3:].upper() == 'CSV':
                file_type = 'csv'
            if output_file[-6:].upper() == 'SQLITE':
                file_type = 'sqlite'

        # Save to disk
        if file_type == 'csv':
            np.savetxt(output_file, res, delimiter=',', header='Link_ID,AB Flow,BA Flow,Tot Flow')

        if file_type == 'sqlite':
            def insert_new_line(conn, link):
                sql = ''' INSERT INTO projects(name,begin_date,end_date)
                          VALUES(?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql, link)
                return cur.lastrowid

            sqlite_file = output_file  # name of the sqlite database file
            table_name = 'link_flows'  # name of the table to be created
            id_field = 'link_id'  # name of the column
            ab_field = 'ab_flow'  # name of the column
            ba_field = 'ba_flow'  # name of the column
            tot_field = 'tot_flow'  # name of the column
            id_type = 'INTEGER'  # column data type
            ab_type = 'REAL'  # column data type
            ba_type = 'REAL'  # column data type
            tot_type =  'REAL'  # column data type

            # Connecting to the database file
            conn = sqlite3.connect(sqlite_file)
            c = conn.cursor()

            # Creating the flows table
            c.execute('CREATE TABLE link_flows (link_id INTEGER PRIMARY KEY, ab_flow, ba_flow, tot_flow REAL)' \
                      .format(tn=table_name, nf=id_field, ft=id_type))

            # writing flows to it
            for link in range(res.shape[0]):
                insert_new_line(conn, link)
            # Committing changes and closing the connection to the database file
            conn.commit()
            conn.close()


