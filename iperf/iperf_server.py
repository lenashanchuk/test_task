from executors.remote_executor import RemoteCommandsExecutor
from iperf.base_iperf import BaseIperf
from parsers.iperf_parser import IperfParser
from singleton import singleton


@singleton
class IperfServer(BaseIperf):
    def __init__(self, user_name, password, ip):
        super().__init__(user_name, password, ip)

    def iperf_start(self, flag='-p'):
        remote_server_executor = RemoteCommandsExecutor(self.user_name, self.password, self.ip)
        result_dict = remote_server_executor.ssh_remote_command('iperf -s', flag)
        print(result_dict)
        stdout, stderr, return_code = result_dict.values()
        result = IperfParser.parse(stdout, stderr, return_code)
        return result

    def kill(self):
        remote_server_executor = RemoteCommandsExecutor(self.user_name, self.password, self.ip)
        remote_server_executor.ssh_remote_command('"killall -9 iperf"')



