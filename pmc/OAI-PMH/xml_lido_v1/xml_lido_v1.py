import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET
from pmc.settings import settings

hostURL = "https://paulmellon.emuseum.com"
verb = "GetRecord"
metadataPrefix = "lido"

reqURL = f"{hostURL}/apis/oai/pmh/v2"

req = requests.get(reqURL, headers=None, auth=(settings.user_id, settings.user_password),
                   params={"verb": verb, "metadataPrefix": metadataPrefix}, verify=False)

with open("xml_lido_v1.xml", "w", encoding="utf-8") as f:
    root = ET.fromstring(req.content)
    f.write(minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t"))

