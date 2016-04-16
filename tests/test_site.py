# -*- coding: utf-8 -*-
import requests

def test_status_code_is_ok():
# http://docs.python-requests.org/en/master/
    r = requests.get('https://vast-mesa-4779.herokuapp.com/bigLoser/login/')
    assert r.status_code == 200
