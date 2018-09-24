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
from janusgraph_python.structure.io.GraphsonReader import JanusGraphSONReader
from janusgraph_python.core.datatypes.Point import Point
from janusgraph_python.core.datatypes.Circle import Circle


class TestGeoShapeDeserializer(unittest.TestCase):
    def setUp(self):
        self.latitude = 80.0
        self.longitude = 100.0
        self.radius = 5

        self.reader = JanusGraphSONReader().build()
        pass

    def test_point_deserialization(self):
        pointGSON = "{\"@type\": \"janusgraph:Geoshape\", " \
                    "\"@value\": {\"coordinates\": [" + str(self.latitude) + ", " + str(self.longitude) + "]}}"

        pointJSON = json.loads(pointGSON)

        expectedPoint = self.reader.toObject(pointJSON)

        actualPoint = Point(self.longitude, self.latitude)

        self.assertEqual(expectedPoint, actualPoint)
        pass

    def test_circle_deserialization(self):

        circleGSON = "{\"" \
                     "@type\":\"janusgraph:Geoshape\"," \
                     "\"@value\":" \
                        "{\"geometry\":" \
                            "{\"@type\":\"g:Map\"," \
                            "\"@value\":" \
                        "[\"type\",\"Circle\"," \
                        "\"coordinates\",{" \
                                            "\"@type\":\"g:List\"," \
                                            "\"@value\":[" \
                                                "{\"@type\":\"g:Double\",\"@value\": " + str(self.latitude) + "}," \
                                                "{\"@type\":\"g:Int32\",\"@value\":" + str(self.longitude) + "}" \
                                                        "]" \
                                            "}, " \
                        "\"radius\", {\"@type\":\"g:Double\",\"@value\":" + str(self.radius) + "}, \
                        \"properties\",{\"@type\":\"g:Map\",\"@value\":[\"radius_units\",\"km\"]}]}}}"

        circleJSON = json.loads(circleGSON)

        expectedCircle = self.reader.toObject(circleJSON)

        actualCircle = Circle(self.longitude, self.latitude, self.radius)

        self.assertEqual(expectedCircle, actualCircle)
