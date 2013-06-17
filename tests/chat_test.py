from jarvis import JarvisFactory
import json
from twisted.trial import unittest
from twisted.test import proto_helpers

class JarvisTestCase(unittest.TestCase):
    def setUp(self):
        factory = JarvisFactory()
        self.proto = factory.buildProtocol(('127.0.0.1', 0))
        self.tr = proto_helpers.StringTransport()
        self.proto.makeConnection(self.tr)


    def _test(self, sentence, expected):
        self.proto.dataReceived(json.dumps({"type": "Chat", "zone": "Test",
                                            "from": "Test",
                                            "body": '%s' % (sentence)
        }))
        jsonAnswer = json.loads(self.tr.value())
        self.assertEqual(jsonAnswer['body'], expected)


    def test_hello(self):
        return self._test(sentence='chat test', expected='chat OK')
