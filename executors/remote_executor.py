import subprocess
from parsers.remote_executor_parser import RemoteExecutorParser


class RemoteCommandsExecutor:
    def __init__(self, user_name, password, ip):
        self.user_name = user_name
        self.password = password
        self.ip = ip

    def ssh_remote_command(self, command, flag='-p'):
        ssh_command = f"exec sshpass {flag} '" + self.password + "' ssh " + self.user_name+"@"+self.ip + " \"" + command + " \""
        process = subprocess.Popen(ssh_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, err = process.communicate()
        return_code = process.returncode
        result = RemoteExecutorParser.parse(output, err, return_code)
        return result



    def scp_remote_command(self, remote_path, home_path):
        scp_command = ("exec sshpass -p '" + self.password + "' scp" + home_path + self.user_name + "@" + self.ip + ":"
                       + remote_path)
        process = subprocess.Popen(f"{scp_command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = process.communicate()
        return_code = process.returncode
        result = RemoteExecutorParser.parse(output, err, return_code)
        return result

