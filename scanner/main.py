import json
import pathlib
import subprocess
from sys import stdout

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
IMAGES_TO_SCAN = SCRIPT_DIR.joinpath("images_to_scan.json")
SCAN_RESULT_DIR = SCRIPT_DIR.parent.resolve().joinpath("scan_results")

def parse_images_to_scan():
    with open(IMAGES_TO_SCAN) as f:
        return json.load(f)

def scan_image(image_name):
    p = subprocess.run(["docker", "scan", f"{image_name}:latest", "--json"], stdout=subprocess.PIPE)
    return p.stdout.decode()

def delete_image(image_name):
    print(f"Deleting {image_name}")
    p = subprocess.run(["docker", "image", "rm", image_name], stdout=subprocess.PIPE)
    print(p.stdout.decode())
    print(f"Deleted {image_name}")

def dump_image_scan_results(image_name, results):
    with open(SCAN_RESULT_DIR.joinpath(f"{image_name}.json"), "w") as f:
        f.write(results)

def process_image(image):
    print(f"Processing {image['image_name']}")
    results = scan_image(image["image_name"])
    dump_image_scan_results(image["image_name"], results)
    print(f"Processed {image['image_name']}")

if __name__ == "__main__":
    images_to_scan = parse_images_to_scan()
    for image in images_to_scan:
        process_image(image)
        delete_image(image["image_name"])

