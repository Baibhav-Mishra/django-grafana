import re
from .const import region_list, cluster_list, gpu_list
# region = ['India', 'US']
# cluster = ['main', 'backup']
# gpu_type = ['a100', 'h100', 'v100']


def find_list(list: list, line: str) -> str:
    for i in list:
        if line.find(i) != -1: return i
    return ''


def get_log_data(file_path):

    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
    pattern1 = re.compile(r"_[a-z0-9]{32}", re.IGNORECASE)
    data = []
    id_list = []
    # print(re.search(pattern1, 'm_c9400da0adb64aa982a4541ed9d68c1c'))
    f = open(file_path)

    for line in f:
        match_timestamp = re.search(pattern, line)
        if match_timestamp is None: break
        match_id = re.search(pattern1, line)

        d = {
            "Timestamp" :match_timestamp.group(0),
            "Region": find_list(region_list, line),
            "Cluster": find_list(cluster_list, line),
            "GPU": find_list(gpu_list, line),
            "ID": '',
            "Log": line
            }

        if match_id:
            start, end = match_id.span()
            id = line[start+1:end]
            id_list.append(id)
            d["ID"] = id

        data.append(d)

    f.close()
    # print(l)
    return id_list, data

    # print(len('c9400da0adb64aa982a4541ed9d68c1c'))
# where "Region" in (${Region:singlequote}) && "ID" == "H"

# print(get_log_data('logs.txt'))
# http://127.0.0.1:8000/api/data/${IDs}