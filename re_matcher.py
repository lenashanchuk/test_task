import re


def re_matcher(pattern, stdout):
    regexp_obj = re.compile(pattern)
    matching_result = None
    for line in stdout.splitlines():
        match = regexp_obj.match(line)
        if match:
            matching_result = match.groupdict()
    return matching_result


