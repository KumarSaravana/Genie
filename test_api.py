# !/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'text'
    return res

def processRequest(req):
    if req.get("result").get("action") != "yahooWeatherForecast":
        return {}
    #baseurl = "https://query.yahooapis.com/v1/public/yql?"
    query = "Hi World"
    return {
        "speech": query,
        "displayText": query,
        # "data": data,
        # "contextOut": [],
        "source": "https://github.com/KumarSaravana/Genie"
    }
    #func_api()
    #if yql_query is None:
    #    return {}
    #yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
    #result = urlopen(yql_url).read()
    #data = json.loads(result)
    #res = makeWebhookResult(data)
    return query

def func_api():
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

    #Parse response
    response = requests.post(url,data=body,headers=headers)
    #print (response.content)

    tree = ET.fromstring(response.content)

    url='http://chdsez297507d.ad.infosys.com:9502/analytics/saw.dll?SoapImpl=webCatalogService'
    sessionID=tree.find('.//{urn://oracle.bi.webservices/v6}sessionID').text


    getSubItems_body="""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v6="urn://oracle.bi.webservices/v6">
       <soapenv:Header/>
       <soapenv:Body>
          <v6:getSubItems>
             <v6:path>/shared</v6:path>
             <v6:mask></v6:mask>
             <v6:resolveLinks></v6:resolveLinks>
             <v6:options>
                <v6:filter>
                   <!--Zero or more repetitions:-->
                   <v6:itemInfoFilters>
                      <v6:name></v6:name>
                      <v6:value></v6:value>
                   </v6:itemInfoFilters>
                   <v6:dummy></v6:dummy>
                </v6:filter>
                <v6:includeACL></v6:includeACL>
                <v6:withPermission></v6:withPermission>
                <v6:withPermissionMask></v6:withPermissionMask>
                <v6:withAttributes></v6:withAttributes>
                <v6:withAttributesMask></v6:withAttributesMask>
             </v6:options>
             <v6:sessionID>"""+sessionID+"""</v6:sessionID>
          </v6:getSubItems>
       </soapenv:Body>
    </soapenv:Envelope>"""

    response = requests.post(url,data=getSubItems_body,headers=headers)
    tree = ET.fromstring(response.content)   

    #print (response.content)

    path=tree.find('.//{urn://oracle.bi.webservices/v6}path').text

    print(path)

    speech = "Report path is " + path

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "https://github.com/KumarSaravana/Genie"
    }

#func_api();
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
