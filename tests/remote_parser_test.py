import unittest

from parsers.remote_executor_parser import RemoteExecutorParser


class TestRemoteParser(unittest.TestCase):
    def setUp(self):
        self.result_dict = {
            "stdout": b'result',
            "stderr": None,
            "return code": 0
        }

    def test_parse(self):
        self.assertEqual(RemoteExecutorParser.parse(b'result', None, 0), self.result_dict)


if __name__ == "__main__":
    unittest.main()
