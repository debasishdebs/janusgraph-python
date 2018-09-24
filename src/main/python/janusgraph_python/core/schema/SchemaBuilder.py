# Name: Debasish Kanhar
# Emp ID: 05222V


class SchemaBuilder(object):
    def __init__(self, connection):
        self.query = ""
        pass

    def create(self, query):
        self.query = query
        print(self.query)
        return