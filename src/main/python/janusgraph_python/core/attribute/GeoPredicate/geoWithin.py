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


from gremlin_python.process.traversal import P
from janusgraph_python.core.datatypes.GeoShape import GeoShape


class GeoWithin(object):
    """
    This Class is used to for Geometric Contains based query though the order of comparision is reversed.
    Returns true if one object is within the other.
    """

    def toString(self):
        """
            Returns the string representation of geoWithin Predicate
        Returns:
            str
        """
        return "geoWithin"

    def geoWithin(self, value):
        """
            Calls the Gremlin Python's P serializer to query based on geoWithin predicate.
        Args:
            value (GeoShape):

        Returns:
            P
        """

        withinP = P(self.toString(), value)

        return withinP
