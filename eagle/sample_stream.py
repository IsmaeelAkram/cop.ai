import requests
import radios
import random
import shutil

SAMPLE_LENGTH = 60  # in seconds

radio = random.choice(radios.radios_by_borough["bk"])
url = radios.generate_stream_url(radio)
print(url)

# Using requests, stream audio from url for SAMPLE_LENGTH seconds and save it to an mp3 file
# https://stackoverflow.com/a/39217788
r = requests.get(url, stream=True)
with open("sample_stream.mp3", "wb") as f:
    shutil.copyfileobj(r.raw, f)
