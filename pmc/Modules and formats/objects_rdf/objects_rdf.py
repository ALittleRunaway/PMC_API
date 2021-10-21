import xml.etree.ElementTree as ET
from xml.dom import minidom
import requests

from pmc.settings import settings


module = "objects"
format = "rdf"
reqURL = f"{settings.hostURL}/{module}/{format}"

req = requests.get(reqURL, headers=None, auth=(settings.user_id, settings.user_password))
with open("objects_rdf.rdf", "w", encoding="utf-8") as f:
    root = ET.fromstring(req.content)
    f.write(minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t"))