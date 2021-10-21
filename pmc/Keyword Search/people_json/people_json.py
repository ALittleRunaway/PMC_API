import json
import requests

from pmc.settings import settings


module = "people"
format = "json"
source_id = 437
reqURL = f"{settings.hostURL}/{module}/{source_id}/{format}"

req = requests.get(reqURL, headers=None, auth=(settings.user_id, settings.user_password))
with open("people_json.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(json.loads(req.text), indent=4))
