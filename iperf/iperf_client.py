from executors.remote_executor import RemoteCommandsExecutor
from iperf.base_iperf import BaseIperf
from parsers.iperf_parser import IperfParser
from singleton import singleton


@singleton
class IperfClient(BaseIperf):
    def __init__(self, user_name, password, ip):
        super().__init__(user_name, password, ip)

    def iperf_start(self, ip_address, flag='-p'):
        remote_client_executor = RemoteCommandsExecutor(self.user_name, self.password, self.ip)
        result_dict = remote_client_executor.ssh_remote_command(f'iperf -c {ip_address}', flag)
        stdout, stderr, return_code = result_dict.values()
        result = IperfParser.parse(stdout, stderr, return_code)
        return result



