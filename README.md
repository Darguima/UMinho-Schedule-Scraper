# UMinho Schedule Scraper 

Python script to scrape the University of Minho schedules pages to a JSON file to use on [Calendarium](https://calendario.cesium.di.uminho.pt/) of [CeSIUM](https://github.com/cesium).

## Running

### Clone

```bash
# With HTTPS
$ git clone https://github.com/Darguima/UMinho-Schedule-Scraper.git

# With SSH
$ git clone git@github.com:Darguima/UMinho-Schedule-Scraper.git
```

### Install dependencies

This script uses `selenium` to scrape the webpage, so before run it, install:

##### Selenium

```bash
$ pip install selenium
```

##### Geckodriver

A selenium dependency to interact with browsers.

```bash
# Arch
$ pacman -S geckodriver
```

##### Firefox

The browser chosen to run with Selenium was Firefox, so don't forget to install it on your system. But I hope you already have it :)

```bash
# Arch
$ pacman -S firefox
```

##### Subject IDs and Filter Ids

[Calendarium](https://calendario.cesium.di.uminho.pt/) use a subject ID and a filterID. On UMinho Courses pages, a list of all subjects, ordered first by year/semesters and next by alphabetic order, and the subject IDs are given. This is everything we need to complete `shifts.json` and generate a basic `filters.json` to Calendarium.

Check if the file `filters.json` exists, if not, read the [subjects_scraper documentation](./subjects_scraper/README.md) to know how scrape them.

### Running

Now you can just run and watch. The scrape will be stored at `shifts.json`, with the schedule of the 4 years of `Computer Science Engineering`.

```bash
$ python main.py
```

## Are you facing problems?

This script use a lot of HTML elements IDs and classes, and, with the past of the years, UM can for some reason update the website and crash this script. Open an issue and I will try solve it fast as possible, or, if you have time, try solve it and I will check your PR ;)
