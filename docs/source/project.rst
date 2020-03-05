.. _aequilibrae_project:

AequilibraE Project
===================

.. toctree::
   :maxdepth: 2

The AequilibraE project is one of the newest portions of the
`aequilibrae API <www.aequilibrae.com/python>`_, and therefore not very mature.

For a better overview of the AequilibraE project, please check the
documentation listed above, as this page is dedicated to a practical implementation

Create project from OSM
~~~~~~~~~~~~~~~~~~~~~~~
However, its first feature is the capability of importing networks directly from
`Open Street Maps <www.openstreetmap.org>`_ into AequilibraE's efficient
TranspoNet format. This is also time to give a HUGE shout out to
`Geoff Boeing <http://www.geoffboeing.com/>`_, creator of the widely used Python
package `OSMNx <https://github.com/gboeing/osmnx>`_ . For several weeks I
worked with Geoff in refactoring the entire OSMNx code base so I could include
it as a submodule or dependency for AequilibraE, but its deep integration with
`GeoPandas <www.geopandas.org>`_ and all the packages it depends on (Pandas,
Shapely, Fiona, RTree, etc.), means that we would have to rebuild OSMNx from the
ground up in order to use it with AequilibraE within QGIS, since its Windows
distribution does not include all those dependencies.

For this reason, I have ported some of Geoff's code into AequilibraE
(modifications were quite heavy, however), and was ultimately able to bring this
feature to life.

.. note::
   Importing networks from OSM is a rather slow process, so we recommend that
   you carefully choose the area you are downloading it for. We have also
   inserted small pauses between successive downloads as to not put too much
   pressure on the OSM servers. So be patient!!

Importing networks from OSM can be done by choosing an area for download,
defined as the current map canvas on QGIS...

.. image:: images/model_from_canvas_area.png
    :width: 999
    :align: center
    :alt: Download OSM networks for visible area


... or for a named place.

.. image:: images/model_from_place.png
    :width: 1057
    :align: center
    :alt: Download OSM networks for named place

Project from layers
~~~~~~~~~~~~~~~~~~~

The AequilibraE project can also be bootstrapped from existing line and node
layers obtained from any other source, as long as they contain the following
required field for the conversion:

* Link ID
* a_node
* b_node
* Link direction
* Length
* Speed
* Allowed modes
* Link Type

These requirements often create quite a bit of manual work, as most networks
available do not have complete (or reliable) information. Manually editing the
networks might be necessary, which is common practice in transport modelling .

Before creating a project from the layer, you can understand how to prepare the
layers for this task in the documentation page for :ref:`network_preparation`.

After all field preparation is done, one can import those layers into an
AequilibraE project using a dedicated tool in the **Project** menu in
AequilibraE.

Accessing **AequilibraE > Project > Create Project from Layers**, the user is
presented with the following screen.

.. image:: images/project_from_layers.png
    :width: 1425
    :align: center
    :alt: Create project from layers

After running this tool a sqlite file (spatialite enabled) will be created and
you can edit the network (create, move or delete links and nodes) and both
layers (including node *ID* and *A_Node*/*B_Node* fields) will remain
consistent with each other.

Video tutorial
~~~~~~~~~~~~~~

If you want a summary of everything that was presented in this page, you can
head over to YouTube to see a demonstration of how to download these projects.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/9PF2qHs2hUc"
     frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;
     picture-in-picture" allowfullscreen></iframe>

.. _adding_centroids:

Adding centroids
----------------

Starting in version 0.6 of AequilibraE, centroid connectors can now only be
added to
`AequilibraE projects <http://www.aequilibrae.com/python/V.0.6.0/project.html>`_
, and no longer generates new layers during the process.

Before we describe what this tool can do for you, however, let's just remember
that there is a virtually unlimited number of things that can go awfully wrong
when we edit networks with automated procedures, and we highly recommend that
you **BACKUP YOUR DATA** prior to running this procedure and that you inspect
the results of this tool **CAREFULLY**.

The **GUI** for this procedure is fairly straightforward, as shown below.

.. image:: images/add_connectors_to_project.png
    :width: 827
    :align: center
    :alt: Adding connectors

One would notice that nowhere in the **GUI** one can indicate which modes they
want to see the network connected for or how to control how many connectors per
mode will be created.  Although it could be implemented, such a solution would
be convoluted and there is probably no good reason to do so.

Instead, we have chosen to develop the procedure with the following criteria:

* All modes will be connected to links where those modes are allowed.
* When considering number of connectors per centroid, there is no guarantee that
  each and every mode will have that number of connectors. If a particular mode
  is only available rather far from the centroid, it is likely that a single
  connector to that mode will be created for that centroid
* When considering the maximum length of connectors, the **GUI** returns to the
  user the list of centroids/modes that could not be connected.

Notice that in order to add centroids and their connectors to the network,
we need to create the set of centroids we want to add to the network in a
separate layer and to have a field that contains unique centroid IDs. These IDs
also cannot exist in the set of node IDs that are already part of the map.
