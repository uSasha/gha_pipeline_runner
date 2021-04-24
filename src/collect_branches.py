import json
import sys

import requests

CONFIG_URL = 'http://dummy.restapiexample.com/api/v1/employees'
template_start = '::set-output name=matrix::{\"include\":'
template_end = '}'


if __name__ == '__main__':
    resp = requests.get(CONFIG_URL)

    data = resp.json()['data']
    tenants = [{'tenant': tenant['id']} for tenant in data]

    print(
        template_start + json.dumps(tenants) + template_end,
        file=sys.stdout
    )
