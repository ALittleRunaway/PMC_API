import json
import requests

from pmc.settings import settings


module = "objects"
format = "json"
reqURL = f"{settings.hostURL}/{module}/{format}"

req = requests.get(reqURL, headers=None, auth=(settings.user_id, settings.user_password))
with open("objects_json.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(json.loads(req.text), indent=4))
