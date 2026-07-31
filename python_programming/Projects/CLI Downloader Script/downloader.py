import argparse
import requests
import time
import os
from urllib.parse import urlparse
from tqdm import tqdm


def download_file(url, output):

    # agar filename nahi diya to URL se nikaal lo
    if output is None:
        parsed = urlparse(url)
        output = os.path.basename(parsed.path)

    start = time.time()

    response = requests.get(url, stream=True)
    total = int(response.headers.get("content-length", 0))

    with open(output, "wb") as file, tqdm(
        desc=output,
        total=total,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:

        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))

    end = time.time()

    size = total / 1024 / 1024
    speed = size / (end - start)

    print(f"\nDownloaded {size:.2f} MB")
    print(f"Speed: {speed:.2f} MB/s")


# CLI arguments
parser = argparse.ArgumentParser(description="Simple CLI File Downloader")

parser.add_argument("url", help="URL of the file to download")
parser.add_argument("-o", "--output", help="Output filename", default=None)

args = parser.parse_args()

download_file(args.url, args.output)