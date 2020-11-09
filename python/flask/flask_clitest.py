#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
import json

head_data = {
	"Content-Type": "application/json; charset=UTF-8",
	"X-Auth-Token": "test-token"
}

payload = json.dumps( """
{
"Version": "3.0",
"SrcType":"vpim",
"MsgType":" pushRes",
"PimVersion": "V19.1",
"PimId": "81f1d9d0-ca13-4eea-a4ce-9bd89a50c9d1",
"ResType":"NetworkDevice",
"FileTime":"2020-07-31T08:00:00",
"FileNameList": [
"/Huawei/VIM/CM/20200731/ CM_PIM_NFV-RP-HNGZ-00A-HW-01_SWITCH_V2.0.0_20200731T080000.json.gz",
"/Huawei/VIM/CM/20200731/ CM_PIM_NFV-RP-HNGZ-00A-HW-01_FIREWALL_V2.0.0_20200731T080000.json.gz",
"/Huawei/VIM/CM/20200731/ CM_PIM_NFV-RP-HNGZ-00A-HW-01_PORT_V2.0.0_20200731T080000.json.gz"
],
"FileNumber":"8"
}
""" )

url = "http://127.0.0.1:5000/pimCmCallBack"

r = requests.put( url, data=payload, headers=head_data )
print( r )
print( r.text )
