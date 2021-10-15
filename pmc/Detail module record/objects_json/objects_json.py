import requests
import json
from pmc.settings import settings

hostURL = "https://paulmellon.emuseum.com"
module = "objects"
format = "json"
source_id = 399568

reqURL = f"{hostURL}/{module}/{source_id}/{format}"

req = requests.get(reqURL, headers=None, auth=(settings.user_id, settings.user_password))
with open("objects_json.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(json.loads(req.text), indent=4))