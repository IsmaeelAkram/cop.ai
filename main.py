import requests
import radios
import shutil
import threading
import time
import os
import chalk
from pprint import pprint

SAMPLE_LENGTH = 10  # in seconds


def setup_and_clean_dirs():
    if not os.path.exists("streams"):
        os.mkdir("streams")
    for borough in radios.by_borough:
        if not os.path.exists(f"streams/{borough}"):
            os.mkdir(f"streams/{borough}")


def stream(borough, radio):
    url = radios.generate_stream_url(radio)
    print(f"Streaming {borough}/{radio}", url)
    r = requests.get(url, stream=True)

    with open(f"streams/{borough}/{radio}.mp3", "wb") as f:
        shutil.copyfileobj(r.raw, f)
    r.close()


setup_and_clean_dirs()
radios.fill_sources()
print(chalk.red("# of sources recognized: "), len(radios.sources))
print(
    chalk.red("# of hardcoded sources: "),
    sum([len(radios.by_borough[borough]) for borough in radios.by_borough]),
)
for source in radios.sources:
    print(
        chalk.red(source.genre),
        chalk.green(source.server_name),
        chalk.cyan(source.server_description),
        chalk.underline(source.listen_url),
    )
