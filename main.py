#!/usr/bin/python

from selenium import webdriver

import json

from modules.course_scraper import course_scraper
from subjects_scraper.subjects_scraper import subjects_scraper

print("Welcome to UMinho Schedule Scraper!")

def get_subject_codes():
    filters_file = open("filters.json", "r")

    subject_codes = {}
    for subject in json.load(filters_file):
        subject_codes[subject["name"].lower()] = {
        "id": subject["subjectId"],
        "filterId": subject["id"]
        }

    filters_file.close()

    return subject_codes

try:  
    subject_codes = get_subject_codes()
    print("\n-> Using subject codes from `filters.json`")
except FileNotFoundError:
    print("\n`filters.json` not founded. ")
    print("Read about 'Subject IDs and Filter Ids' or `subjects_scraper` on documentation\n")

    if input("Run subjects scraper? [y/N] ").lower() != "y":
        print("\nLeaving ...")
        exit()
    else:
        print("\nRunning subjects scraper: ====\n")
        subjects_scraper()
        print("\n==============================")
    
    subject_codes = get_subject_codes()

driver = webdriver.Firefox()

print("\nScraping schedules from Licenciatura em Engenharia Informática:")
classes = course_scraper(driver, "Licenciatura em Engenharia Informática", subject_codes)

print("\nScraping schedules from Mestrado em Engenharia Informática:")
classes += course_scraper(driver, "Mestrado em Engenharia Informática", subject_codes)

with open("shifts.json", "w") as outfile:
    json.dump(classes, outfile, indent=2, ensure_ascii=False)

print(f"\nDone. Scraped {len(classes)} shifts from the schedules!")
print(f"Check them at shifts.json\n")

driver.close()

