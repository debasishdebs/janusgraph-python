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
from janusgraph_python.core.datatypes.RelationIdentifier import RelationIdentifier


class TestRelationIdentifierDeserialization(unittest.TestCase):
    def setUp(self):
        self.relationID = "74q-9n4-b2t-cr4"
        self.reader = JanusGraphSONReader().build()
        pass

    def test_relationID_deserialization(self):
        relIDGson = "{\"@type\":\"janusgraph:RelationIdentifier\",\"@value\": {\"relationId\": \"" + self.relationID + "\"}}"

        relIDJSON = json.loads(relIDGson)

        expectedRelID = self.reader.toObject(relIDJSON)
        actualRelID = RelationIdentifier(self.relationID)

        self.assertEqual(expectedRelID, actualRelID)
