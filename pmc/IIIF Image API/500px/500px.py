import requests

from pmc.settings import settings


source_id = 317163
size = "500,"
reqURL = f"{settings.hostURL}/apis/iiif/image/v2/{source_id}/full/{size}/0/default.jpg"

req = requests.get(reqURL, headers=None, auth=(settings.user_id, settings.user_password))
with open("image_500px.jpg", "wb") as f:
    f.write(req.content)
