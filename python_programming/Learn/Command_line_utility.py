# import argparse
# import requests
# from tqdm import tqdm

# def download_file(url, local_filename):
#     if local_filename is None:
#         local_filename = url.split('/' )[-1] 
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)
#     return local_filename


# parser = argparse.ArgumentParser()

# parser.add_argument("url", help="url of the file to download")
# parser.add_argument("-o","--output", help="Name of the file",default=None)

# args = parser.parse_args()

# print(args.url)
# print(args.output)

# download_file(args.url, args.output)

import requests
import time
from tqdm import tqdm

def download_file(url, filename):

    start = time.time()

    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))

    with open(filename, "wb") as file, tqdm(
        desc=filename,
        total=total,
        unit='B',
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

    print(f"Downloaded {size:.2f} MB")
    print(f"Speed: {speed:.2f} MB/s")


download_file(
"https://www.intelliamiet.in/trikon/trikon2026/logo.png",
"background1.jpg"
)