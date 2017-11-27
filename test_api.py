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


