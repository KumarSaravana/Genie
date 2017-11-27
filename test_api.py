# -*- coding:utf8 -*-
# !/usr/bin/env python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

url='http://chdsez297507d.ad.infosys.com:9502/analytics/saw.dll?SoapImpl=nQSessionService'
headers = {"Content-Type": "text/xml"}
body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v6="urn://oracle.bi.webservices/v6">
   <soapenv:Header/>
   <soapenv:Body>
      <v6:logon>
         <v6:name>Infosys</v6:name>
         <v6:password>infosys123</v6:password>
      </v6:logon>
   </soapenv:Body>
</soapenv:Envelope>"""

response = requests.post(url,data=body,headers=headers)
print (response.content)


