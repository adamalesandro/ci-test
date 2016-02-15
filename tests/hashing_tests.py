import unittest
from sgnl.hashing import sha1, sha256


class HashingTest(unittest.TestCase):

    raw_string = "The fox jumps over the log."

    def test_sha1(self):
        self.assertEqual(sha1(self.raw_string), "5b953387af6fecf49f37a9459bd83a526d7faf2b")

    def test_sha256(self):
        self.assertEqual(sha256(self.raw_string), "9d7b9ab1823303f4c0f212d4518a8155edde03186e2e226a6a65aeabb95d5c4e")