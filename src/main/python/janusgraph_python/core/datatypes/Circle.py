# Copyright 2018 JanusGraph Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Circle(object):
    def __init__(self, longitude, latitude, radiusInKM):
        """
            The actual class representing Geographical Circle.

        Args:
            latitude (float): The latitude of circle's center.
            longitude (float): The longitude of circle's center
            radiusInKM (int): The radius of circle in KM.
        """

        self.latitude = float(latitude) * 1.0
        self.longitude = float(longitude) * 1.0
        self.radius = radiusInKM

        status = self.__are_valid_coordinates()

        if not status:
            raise ValueError("Invalid Coordinates/Radius passed. "
                             "Latitude needs to be b/w [-90, 90] and Longitude b/w [-180, 180] and Radius > 0")

        pass

    def getShape(self):
        """
            Return the Shape of Geometrical shape
        Returns:
            str
        """
        return "CIRCLE"

    def toString(self):
        """
            Returns the String representation of Circle object.
        Returns:
            str
        """
        return "CIRCLE(lat: {}, lon: {}, r: {})".format(self.getLatitude(), self.getLongitude(), self.getRadius())

    def getLatitude(self):
        """
            Get latitude of Circle center.
        Returns:
            float
        """
        return self.latitude

    def getLongitude(self):
        """
            Get longitude of circle center.
        Returns:
            float
        """
        return self.longitude

    def getCoordinates(self):
        """
            Get the coordinated of circle center
        Returns:
            list
        """
        return [self.latitude, self.longitude]

    def getRadius(self):
        """
            Get the radius of circle
        Returns:
            int
        """
        return self.radius

    def __are_valid_coordinates(self):
        """
            Check for validity of coordinated passed to object in creation time.
        Returns:
            bool
        """

        return abs(self.getLatitude()) <= 90.0 and abs(self.getLongitude()) <= 180.0 and self.getRadius() > 0

    def __eq__(self, other):
        """
            Overrides default class equality method.
        Args:
            other (Circle): The other object to compare against.

        Returns:
            bool
        """

        if type(other) is str and other == self.toString():
            return True

        elif type(other) is Circle:
            return (other.getLatitude().__eq__(self.getLatitude())) and \
                   (other.getLongitude().__eq__(self.getLongitude())) and \
                   (other.getRadius().__eq__(self.getRadius()))

        elif other is None:
            return False

        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.toString()
