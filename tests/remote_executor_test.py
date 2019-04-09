import unittest
from unittest.mock import patch

from executors.remote_executor import RemoteCommandsExecutor


def communicate():
    output = '1.txt folder1 folder2'
    return output, None

class TestRemoteExecutor(unittest.TestCase):
    def setUp(self):
        self.result_dict = {
            "stdout": '1.txt folder1 folder2',
            "stderr": None,
            "return code": 0
        }
        self.remote_executor = RemoteCommandsExecutor('helen,shanchuk', '****', '192.168.1.6')

    def test_ssh_remote_command(self):
        with patch('executors.remote_executor.subprocess') as subprocess:
            subprocess.Popen.return_value.returncode = 0
            subprocess.Popen.return_value.communicate = communicate
            self.assertEqual(self.remote_executor.ssh_remote_command('ls'), self.result_dict)


if __name__ == "__main__":
    unittest.main()
