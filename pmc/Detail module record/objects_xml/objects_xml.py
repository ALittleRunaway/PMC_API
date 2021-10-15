import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET
from pmc.settings import settings

hostURL = "https://paulmellon.emuseum.com"
module = "objects"
format = "xml"
source_id = 399568

reqURL = f"{hostURL}/{module}/{source_id}/{format}"

req = requests.get(reqURL, headers=None, auth=(settings.user_id, settings.user_password))
with open("objects_xml.xml", "w", encoding="utf-8") as f:
    root = ET.fromstring(req.content)
    f.write(minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t"))
