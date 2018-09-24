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


import unittest
import json

from janusgraph_python.core.datatypes.Point import Point
from janusgraph_python.structure.io.GraphsonWriter import JanusGraphSONWriter


class TestCircleSerialization(unittest.TestCase):

    def setUp(self):
        self.latitude = 80
        self.longitude = 100

        self.point = Point(self.longitude, self.latitude)

        self.writer = JanusGraphSONWriter().build()
        pass

    def test_point_serialization(self):
        graphSON = self.writer.writeObject(self.point)

        expectedJSONStr = "{\"@type\":\"janusgraph:Geoshape\",\"@value\":{\"type\":\"Point\", \
                            \"coordinates\":[{\"@type\":\"g:Double\",\"@value\":" + str(self.latitude) + "},\
                            {\"@type\":\"g:Double\",\"@value\":" + str(self.longitude) + "}]}}"

        actualGson = json.loads(graphSON)

        expectedGson = json.loads(expectedJSONStr)

        self.assertEqual(actualGson, expectedGson)

        pass
