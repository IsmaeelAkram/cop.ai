import requests
import radios
import random
import shutil

SAMPLE_LENGTH = 60  # in seconds

radio = radios.radios_by_borough["bk"][1]  # ALT-nypd-bk-62-68
url = radios.generate_stream_url(radio)
print(url)

# Using requests, stream audio from url for SAMPLE_LENGTH seconds and save it to an mp3 file
# https://stackoverflow.com/a/39217788
r = requests.get(url, stream=True)
with open("ALT-nypd-bk-62-68.mp3", "wb") as f:
    shutil.copyfileobj(r.raw, f)
