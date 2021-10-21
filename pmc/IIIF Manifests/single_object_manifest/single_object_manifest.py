import json
import requests

from pmc.settings import settings


source_id = 400392
reqURL = f"{settings.hostURL}/apis/iiif/presentation/v2/1-objects-{source_id}/manifest"

req = requests.get(reqURL, headers=None, auth=(settings.user_id, settings.user_password))
with open("single_object_manifest.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(json.loads(req.text), indent=4))
