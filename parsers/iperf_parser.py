import json
from re_matcher import re_matcher


class IperfParser:

    @ staticmethod
    def parse(stdout, stderr, return_code):
        if stderr:
            status = return_code
            stderr = f'Error {stderr}'
            json_result = None

        elif return_code:
            status = return_code
            stderr = f'Error with return code {return_code}'
            json_result = None

        else:
            status = 0
            stderr = None
            stdout_res = stdout.decode("utf-8")
            regular_search_ips = (
                r'\[(.{3})\]\s+local(?P<local_ip>.*?)port' 
                r'.*?connected with(?P<server_ip>.*?)port'
            )
            regular_search_other = (
                r'\[(.{3})\]\s+(?P<interval>.*?sec)'
                r'\s+(?P<transfer>.*?Bytes|bits)'
                r'\s+(?P<bandwidth>.*?/sec)'
            )
            ip_dict = re_matcher(regular_search_ips, stdout_res)
            iperf_dict = re_matcher(regular_search_other, stdout_res)
            res_dict = {**ip_dict, **iperf_dict}
            json_result = json.dumps(res_dict, indent=4)
        result_dict = {
              "error": stderr,
              "result": json_result,
              "status": status
              }
        return result_dict
