# Name: Debasish Kanhar


class toGeoJSON(object):
    TYPE_KEY = "@type"
    VALUE_KEY = "@value"
    DATA_TYPE = "g:Double"

    def __init__(self, geoshape):
        """

        Args:
            geoshape:
        """

        self.shape = geoshape
        self.shapeStr = self.shape.getShape()

        self.geoJSON = dict()

        self.GEOMETRY = "geometry"
        self.GEOMETRY_TYPE = self.shapeStr.capitalize()
        pass

    def convert(self):
        """

        Returns:
            geoJSON (dict)
        """

        if self.GEOMETRY_TYPE.lower() == "point":
            self.geoJSON["type"] = self.GEOMETRY_TYPE
            self.geoJSON["coordinates"] = list()

            coordinates = self.shape.getCoordinates()

            coordinateJSON = self.__serialize_coordinates_to_geo_json(coordinates)
            self.geoJSON["coordinates"] = coordinateJSON

        else:
            # self.geoJSON["geometry"] = dict()

            geometryData = dict()

            geometryData["type"] = self.GEOMETRY_TYPE
            geometryData["coordinates"] = list()

            coordinates = self.shape.getCoordinates()

            coordinateJSON = self.__serialize_coordinates_to_geo_json(coordinates)
            geometryData["coordinates"] = coordinateJSON

            radius = self.shape.getRadius()
            geometryData["radius"] = self.__serialize_radius_to_geo_json(radius)

            geometryData["properties"] = dict()
            geometryData["properties"]["radius_units"] = "km"

            self.geoJSON["geometry"] = geometryData

        return self.geoJSON

    def __serialize_radius_to_geo_json(self, radius):
        radiusJSON = dict()
        radiusJSON[self.TYPE_KEY] = self.DATA_TYPE
        radiusJSON[self.VALUE_KEY] = radius
        return radiusJSON

    def __serialize_coordinates_to_geo_json(self, coordinates):
        coordinateJSON = list()

        for i in range(len(coordinates)):
            crdJSON = dict()
            crdJSON[self.TYPE_KEY] = self.DATA_TYPE
            crdJSON[self.VALUE_KEY] = coordinates[i]

            coordinateJSON.append(crdJSON)

        return coordinateJSON