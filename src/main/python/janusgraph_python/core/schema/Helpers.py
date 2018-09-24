# Name: Debasish Kanhar
# Emp ID: 05222V


class Helpers(object):
    @staticmethod
    def open_graph_management():
        query = "mgmt = graph.openManagement();\n"
        return query

    @staticmethod
    def close_graph_management():
        query = "mgmt.commit();\n"
        return query