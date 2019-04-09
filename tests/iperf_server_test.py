import unittest
import json
from unittest.mock import patch

from iperf.iperf_server import IperfServer


def communicate():
    stdout = b'------------------------------------------------------------\n' \
             b'Client connecting to first, TCP port 5001\nTCP window size:  128' \
             b' KByte (default)\n-----------------------------------------------' \
             b'-------------\n[  6] local 10.6.60.38 port 56983 connected with' \
             b' 10.6.193.161 port 5001\n[ ID] Interval       Transfer     Bandwidth' \
             b'\n[  6]  0.0-11.9 sec   768 KBytes   527 Kbits/sec\n'
    return stdout, None

class TestIperfServer(unittest.TestCase):
    def setUp(self):
        self.iperf_server = IperfServer('helen,shanchuk', '****', '192.168.1.6')
        self.res_dict = {
            "error": None,
            "result": json.dumps({
                "local_ip": " 10.6.60.38 ",
                "server_ip": " 10.6.193.161 ",
                "interval": "0.0-11.9 sec",
                "transfer": "768 KBytes",
                "bandwidth": "527 Kbits/sec",
            }, indent=4),
            "status": 0
        }


    def test_iperf_start(self):
        with patch('executors.remote_executor.subprocess') as subprocess:
            subprocess.Popen.return_value.returncode = 0
            subprocess.Popen.return_value.communicate = communicate
            self.assertEqual(self.iperf_server.iperf_start(), self.res_dict)

if __name__ == "__main__":
    unittest.main()
