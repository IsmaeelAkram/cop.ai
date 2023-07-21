import requests
import radios
import shutil
import threading
import time
import os
from pprint import pprint

SAMPLE_LENGTH = 10  # in seconds


def stream(borough, radio):
    url = radios.generate_stream_url(radio)
    print(f"Streaming {borough}/{radio}", url)
    r = requests.get(url, stream=True)

    with open(f"streams/{borough}/{radio}.mp3", "wb") as f:
        shutil.copyfileobj(r.raw, f)
    r.close()


# Create all directories
if not os.path.exists("streams"):
    os.mkdir("streams")
for borough in radios.by_borough:
    if not os.path.exists(f"streams/{borough}"):
        os.mkdir(f"streams/{borough}")

threads = []
for borough in radios.by_borough:
    for radio in radios.by_borough[borough]:
        t = threading.Thread(target=stream, args=(borough, radio), daemon=True)
        threads.append((borough, radio, t))
        t.start()

time.sleep(SAMPLE_LENGTH)
for borough, radio, thread in threads:
    thread.join()
    print("Stopped thread")
