# SrealityScraper

This project is supposed to be simple demonstration of leveraging scrapy to scrape srealitky.cz flats into postgresql database. Then FastAPI is used to display the information in html format.

## How to use

Just run `docker-compose up`.

## Folder structure
- `LICENSE` - standard MIT licennse
- `requirements.txt` - requirements for api and scraper together
- `docker-compose.yml` - docker compose for db, api, and scraper
- `Dockerfile` - standard Dockerfile used for api and scraper
- `sreality_scrapper` - scraping code that leverages Scrapy
- `sreality_display_api` - API code that leverages FastAPI and SQLAlchemy

## Possible improvements
- deal with duplicates in the sql table insertions after running scrapper more times (even twice in row)
- adjust scrapy to use some counting pipeline so we can specify how many items we want (currently only pages can be specified..)
- store all image urls in separate table (during presentation only one can be used)
- have separate Dockerfile for API and Scraper (and separate requirements)
- document code more
- make database environment variables for scraper and api shared