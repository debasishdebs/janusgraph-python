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


from .GeoContains import GeoContains
from .GeoWithin import GeoWithin
from ...datatypes.GeoShape import GeoShape


class Geo(object):
    """
    This class defines all the Geo Predicates.
    """

    contains = GeoContains()
    within = GeoWithin()

    @staticmethod
    def geoContains(value):
        """ The class is used for JanusGraph geoContains predicate.

        GeoContains predicate holds true when one object, is contained by another. Considering the example in docs,
        the following statement holds true : India (GeoShape) contains (GeoContains) New Delhi (GeoShape)

        Args:
            value (GeoShape): The GeoShape to query for and return all results which are present inside this GeoShape

        Returns:
            Any
        """
        return Geo.contains.geoContains(value)

    @staticmethod
    def geoWithin(value):
        """ The class is used for JanusGraph geoWithin predicate.

        GeoWithin predicate holds true when one object, is within another. Considering the example in docs,
        the following statement holds true : New Delhi (GeoShape) within (GeoWithin) India (GeoShape)

        Args:
            value (GeoShape): The GeoShape to query for and return all results within this this GeoShape is present.

        Returns:
            Any
        """
        return Geo.within.geoWithin(value)
