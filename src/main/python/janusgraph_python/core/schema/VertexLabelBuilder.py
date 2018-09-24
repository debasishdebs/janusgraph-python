# Name: Debasish Kanhar
# Emp ID: 05222V


from .SchemaBuilder import SchemaBuilder
from .Helpers import Helpers as helpers


class VertexLabelBuilder(SchemaBuilder):
    def __init__(self, connection):
        super(VertexLabelBuilder, self).__init__(connection)

        self.query += helpers.open_graph_management()

        self.label = None
        pass

    def makeVertexLabel(self, label):
        self.label = label
        return self

    def make(self):
        if self.label is None:
            raise AttributeError("makeVertexLabel() method needs called before make()")

        q = "if (mgmt.getVertexLabel('{}')) {{" \
            "       {} = mgmt.getVertexLabel('{}'); }}" \
            "else {{" \
            "{} = mgmt.makeVertexLabel('{}').make(); }}\n".format(self.label,
                                                                  self.label, self.label, self.label, self.label)

        self.query += q

        self.query += helpers.close_graph_management()

        self.create(self.query)

        return self.label
