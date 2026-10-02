"""Minimal example: run the infoempleo-jobs-scraper Actor and print the results.

Usage: APIFY_TOKEN=... python run.py   (pip install apify-client)
"""
import os
import sys

from apify_client import ApifyClient

token = os.environ.get("APIFY_TOKEN")
if not token:
    sys.exit("Set the APIFY_TOKEN environment variable first.")

client = ApifyClient(token)

run_input = {
    "keywords": "programador",
    "location": "Madrid",
    "publishedWithin": "7",
    "maxItems": 50,
    "includeDescriptions": False,
}

run = client.actor("bibian/infoempleo-jobs-scraper").call(run_input=run_input)

count = 0
for item in client.dataset(run.default_dataset_id).iterate_items():
    count += 1
    print(f"{item['title']} | {item.get('companyName')} | {item.get('city')} ({item.get('region')}) | {item.get('salaryMin')}-{item.get('salaryMax')} {item.get('salaryPeriod')}")
print(f"{count} results")
