import requests
import radios
import shutil
import threading
import time
import os
import chalk
from pprint import pprint

SAMPLE_LENGTH = 10  # in seconds


def setup_dirs():
    if not os.path.exists("streams"):
        os.mkdir("streams")
    for source in radios.sources:
        if not os.path.exists(f"streams/{source.genre}"):
            os.mkdir(f"streams/{source.genre}")


# Fetch sources from icecast
radios.fill_sources()
# Setup dirs
setup_dirs()

# Recognize sources
print(chalk.red("# of sources recognized: "), len(radios.sources))
print(
    chalk.red("# of hardcoded sources: "),
    sum([len(radios.by_borough[borough]) for borough in radios.by_borough]),
)
for source in radios.sources:
    print(
        chalk.red(source.genre),
        "\t",
        chalk.green(source.server_name),
        "\t",
        chalk.cyan(source.server_description),
        "\t",
        chalk.underline(source.listen_url),
        "\t",
    )


def stream(source: radios.Source):
    try:
        print(chalk.red("✅ Streaming"), source.server_name)
        r = requests.get(source.listen_url, stream=True)
        r.raise_for_status()
        with open(f"streams/{source.genre}/{source.server_name}.mp3", "wb") as f:
            shutil.copyfileobj(r.raw, f)
    except Exception as e:
        print(chalk.red("❌ Error streaming "), source.genre)
        print(e)


# Stream from sources to mp3
streaming_threads = []
for source in radios.sources:
    thread = threading.Thread(target=stream, args=(source,))
    thread.start()
    streaming_threads.append(thread)
time.sleep(SAMPLE_LENGTH)
for thread in streaming_threads:
    thread.join()
