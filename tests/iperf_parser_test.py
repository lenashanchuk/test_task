import unittest
import json

from parsers.iperf_parser import IperfParser


class TestIperfParser(unittest.TestCase):
    def setUp(self):
        self.res_dict = {
            "error": None,
            "result": json.dumps({
                "local_ip": " 10.6.60.38 ",
                "server_ip": " 10.6.193.161 ",
                "interval": "0.0-11.9 sec",
                "transfer": "768 KBytes",
                "bandwidth": "527 Kbits/sec"
            }, indent=4),
            "status": 0
        }
        self.error = {
            "error": f"Error ERROR",
            "result": None,
            "status": 1
            }
        self.code_res = {
            "error": "Error with return code 1",
            "result": None,
            "status": 1
            }
        self.stdout = b'------------------------------------------------------------\n' \
                      b'Client connecting to first, TCP port 5001\nTCP window size:  128' \
                      b' KByte (default)\n-----------------------------------------------' \
                      b'-------------\n[  6] local 10.6.60.38 port 56983 connected with' \
                      b' 10.6.193.161 port 5001\n[ ID] Interval       Transfer     Bandwidth' \
                      b'\n[  6]  0.0-11.9 sec   768 KBytes   527 Kbits/sec\n'

    def test_parse(self):
        self.assertEqual(IperfParser.parse(None, 'ERROR', 1), self.error)
        self.assertEqual(IperfParser.parse(None, None, 1), self.code_res)
        self.assertEqual(IperfParser.parse(self.stdout, None, 0), self.res_dict)


if __name__ == "__main__":
    unittest.main()
