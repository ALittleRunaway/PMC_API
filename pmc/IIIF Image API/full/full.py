import requests
from pmc.settings import settings

hostURL = "https://paulmellon.emuseum.com"
source_id = 317163
size = "full"

reqURL = f"{hostURL}/apis/iiif/image/v2/{source_id}/full/{size}/0/default.jpg"

# this may take a little while
req = requests.get(reqURL, headers=None, auth=(settings.user_id, settings.user_password))
with open("image_full.jpg", "wb") as f:
    f.write(req.content)
