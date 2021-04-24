import json
import sys

import requests

CONFIG_URL = 'http://dummy.restapiexample.com/api/v1/employees'
template_start = '::set-output name=matrix::{\"include\":'
template_end = '}'


if __name__ == '__main__':
    resp = requests.get(CONFIG_URL)

    if resp.ok:
        tenants = [{'tenant': tenant['id']} for tenant in resp.json()['data']]
    else:
        tenants = [{'tenant': i} for i in range(3)]

    print(
        template_start + json.dumps(tenants) + template_end,
        file=sys.stdout
    )
