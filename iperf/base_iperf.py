class BaseIperf:
    def __init__(self, user_name, password, ip):
        self.user_name = user_name
        self.password = password
        self.ip = ip

    def iperf_start(self, *args):
        raise NotImplemented















