# Name: Debasish Kanhar
# Emp ID: 05222V


from .SchemaBuilder import SchemaBuilder
from .Helpers import Helpers as helpers


class EdgeLabelBuilder(SchemaBuilder):
    def __init__(self, connection):
        super(EdgeLabelBuilder, self).__init__(connection)

        self.query += helpers.open_graph_management()

        self.label = None
        self.multiplicity = "MULTI"
        pass

    def makeEdgeLabel(self, label):
        self.label = label
        return self

    def multiplicity(self, mult):
        self.multiplicity = mult
        return self

    def make(self):
        if self.label is None:
            raise AttributeError("makeVertexLabel() method needs called before make()")

        q = "if (mgmt.getEdgeLabel('{}')) {{" \
            "   {} = mgmt.getEdgeLabel('{}'); }}" \
            "else {{" \
            "   {} = mgmt.makeEdgeLabel('{}').multiplicity({}).make(); }}\n".format(
                self.label, self.label, self.label, self.label, self.label, self.multiplicity)

        self.query += q

        self.query += helpers.close_graph_management()

        self.create(self.query)

        return self.label
