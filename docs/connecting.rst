=========================
Connecting to JanusGraph
=========================

The library provides a client to connect to JanusGraph running in
Gremlin Server mode.

For information about Gremlin Server, refer to `JanusGraph docs
<https://docs.janusgraph.org/latest/server.html>`_.


-------------------------
Build JanusGraph Client
-------------------------

The client provided to connect to JanusGraph takes care of registering the
required serializers and deserializers like GeoShape, RelationIdentifier
and any objects specific to JanusGraph.

Currently implemented for GeoShape for Point and Circle. Needs to be extended.


.. code-block:: python

    from janusgraph_python.driver.ClientBuilder import JanusGraphClient
    # Create JanusGraph connection providing required parameters.
    connection = JanusGraphClient().connect(url="0.0.0.0", port="8182", graph="g").get_connection()
    # Create Traversal with JanusGraph connection object
    g = Graph().traversal().withRemote(connection)


-----------------------------------------
Register Custom Serializer/Deserializer
-----------------------------------------

JanusGraph Python client provides API to register your custom Serializer/Deserializer

    - Serializer: Serializes a Python object into corresponding JanusGraph object.
                    Currently implemented for `Point <janusgraph_python.serializer.PointSerializer.html>`_,
                    `Circle <janusgraph_python.serializer.CircleSerializer.html>`_ and
                    `RelationIdentifier <janusgraph_python.serializer.RelationIdentifierSerializer.html>`_

    - Deserializer: Deserializes response from Gremlin Server into corresponding Python objects.
                    Currently implemented for above mentioned data types
                    `see docs <janusgraph_python.GeoShapeDeserializer.html>`_ .


*NOTE: For scope of example, we are registering Circle Serializer and Deserializer which is implemented.

*NOTE: It is safe to add Serializer and Deserializer for a particular object together, else we
might run into unforeseen errors.

.. code-block:: python

    from janusgraph_python.serializer.CircleSerializer import CircleSerializer, Circle
    from janusgraph_python.serializer.GeoShapeDeserializer import GeoShapeDeserializer

    # All Geoshapes in JanusGraph are identified by `Geoshape`
    # while Relation Identifier by `RelationIdentifier`
    geoshape_identifier = "Geoshape"

    # The Deserializer class to deserialize into Python object
    geoshape_deserializer = GeoShapeDeserializer
    # The Python object which needs to be deserialized into JanusGraph object.
    obj_to_register = Circle
    # The class to Serialize Python object into its GraphSON correspondent
    circle_serializer = CircleSerializer

    # Register Serializer and Deserializer with JanusGraphReader and Writer service
    from janusgraph_python.structure.io.GraphsonWriter import JanusGraphSONWriter
    from janusgraph_python.structure.io.GraphsonReader import JanusGraphSONReader

    reader = JanusGraphSONReader().register_deserializer(geoshape_identifier, geoshape_deserializer)
    writer = JanusGraphSONWriter().register_serializer(obj_to_register, circle_serializer)

    # Apply the connected reader and writer service while creating JanusGraph connection
    from gremlin_python.structure.graph import Graph
    from janusgraph_python.driver.ClientBuilder import JanusGraphClient

    client = JanusGraphClient().connect(url="0.0.0.0", port="8182",
                                        graph="g", graphson_reader=reader, graphson_writer=writer)
    connection = client.get_connection()
    g = Graph().traversal().withRemote(client)

