# 到处爬 cidr 段并生成正确的格式

import os
import json

GOOGLE = 'google'
GOOGLE_CLOUD = 'google_cloud'

def get_google(data):
    res = []
    prefixes = data.get('prefixes', [])
    for prefix in prefixes:
        cidr = prefix.get('ipv4Prefix', '')
        if cidr:
            res.append(cidr)
    return res

for file_dir in os.listdir('source'):
    file_path = os.path.join('source', file_dir)
    res = []
    with open(file_path) as json_file:
        data = json.load(json_file)
        if GOOGLE in file_dir or GOOGLE_CLOUD in file_dir:
            res = get_google(data)
            res_file_name = file_dir.split('.')[0] + '_list'

    with open('list/' + res_file_name, 'a') as res_file:
        res_file.writelines([s + '\n' for s in res])

