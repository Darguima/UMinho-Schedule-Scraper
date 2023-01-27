#!/usr/bin/python

from selenium import webdriver

from modules.course_scraper import course_scraper

from json import dump as json_dump

print("Welcome to UMinho Schedule Scraper!")

driver = webdriver.Firefox()

print("\nScraping schedules from Licenciatura em Engenharia Informática:")
classes = course_scraper(driver, "Licenciatura em Engenharia Informática")

print("\nScraping schedules from Mestrado em Engenharia Informática:")
classes += course_scraper(driver, "Mestrado em Engenharia Informática", first_university_year=4)

with open("shifts.json", "w") as outfile:
    json_dump(classes, outfile, indent=2, ensure_ascii=False)

print(f"\nDone. Scraped {len(classes)} shifts from the schedules!")
print(f"Check them at shifts.json\n")

driver.close()

