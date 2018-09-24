# Name: Debasish Kanhar
# Emp ID: 05222V

from ..core.schema.PropertyKeyBuilder import PropertyKeyBuilder
from ..core.schema.VertexLabelBuilder import VertexLabelBuilder
from ..core.schema.EdgeLabelBuilder import EdgeLabelBuilder


class JanusGraphManagement(object):
    def __init__(self, connection):
        self.connection = connection
        pass

    def propertyKeyBuilder(self):
        builder = PropertyKeyBuilder(self.connection)
        return builder

    def vertexLabelBuilder(self):
        builder = VertexLabelBuilder(self.connection)
        return builder

    def edgeLabelBuilder(self):
        builder = EdgeLabelBuilder(self.connection)
        return builder
