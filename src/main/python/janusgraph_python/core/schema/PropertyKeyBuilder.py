# Name: Debasish Kanhar
# Emp ID: 05222V


from .SchemaBuilder import SchemaBuilder
from .Helpers import Helpers as helpers


class PropertyKeyBuilder(SchemaBuilder):
    def __init__(self, connection):
        super(PropertyKeyBuilder, self).__init__(connection)

        self.query += helpers.open_graph_management()

        self.data_type = "String"
        self.card = "SINGLE"
        self.property = None
        pass

    def makePropertKey(self, property_name):
        self.property = property_name
        return self

    def dataType(self, data_type):
        self.data_type = data_type
        return self

    def cardinality(self, card):
        self.card = card
        return self

    def make(self):
        if self.property is None:
            raise AttributeError("makePropertyKey() method needs called before make()")

        q = "if (mgmt.getPropertyKey('{}')) {{" \
            "   {} = mgmt.getPropertyKey('{}'); }}" \
            "else {{" \
            "   {} = mgmt.makePropertyKey('{}').dataType({}.class).cardinality(Cardinality.{}).make(); }}\n".format(
            self.property, self.property, self.property, self.property, self.property, self.dataType, self.card)

        self.query += q

        self.query += helpers.close_graph_management()

        self.create(self.query)

        return self.property
