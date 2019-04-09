import argparse
from iperf.iperf_server import IperfServer
from iperf.iperf_client import IperfClient


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-ipc", "--ip_client", action="store", dest="ip_client", help="client ip address")
    arg_parser.add_argument("--client_username", action="store", dest="client_username", help="client username")
    arg_parser.add_argument("--client-pswd-flag", nargs="?", dest="client_pswd_flag", const='-f', default='-p', required=False,
                            help="Specify password from file for client")
    arg_parser.add_argument("--client_password", action="store", dest="client_password", help="client password")
    arg_parser.add_argument("-ips", "--ip_server", action="store", dest="ip_server", help="server ip address")
    arg_parser.add_argument("--server_username", action="store", dest="server_username", help="server username")
    arg_parser.add_argument("--server-pswd-flag", nargs="?", dest="server_pswd_flag", const='-f', default='-p', required=False,
                            help="Specify password from file for server")
    arg_parser.add_argument("--server_password", action="store", dest="server_password", help="server password")
    return arg_parser.parse_args()


def main():
    try:
        print('aaa')
        args = get_args()
        print(args)
        server = IperfServer(args.server_username, args.server_password, args.ip_server)
        client = IperfClient(args.client_username, args.client_password, args.ip_client)
        server.iperf_start(args.server_pswd_flag)
        result = client.iperf_start(args.ip_server, args.client_pswd_flag)
        print(result)

    except Exception as e:
        print(e)

    finally:
        server.kill()


if __name__ == "__main__":
    main()
