class RemoteExecutorParser:
    @staticmethod
    def parse(stdout, stderr, return_code):
        result_dict = {
            "stdout": stdout,
            "stderr": stderr,
            "return code": return_code
        }
        return result_dict
