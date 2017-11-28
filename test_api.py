def func_api():
    import requests
    import xml.etree.ElementTree as ET
    from xml.dom import minidom
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

func_api();
