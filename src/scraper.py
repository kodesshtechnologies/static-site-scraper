import time
import logging
from playwright.sync_api import sync_playwright
from src.config import BASE_URL, WAIT_TIME, TIMEOUT, HEADLESS
from src.parser import parse_books


def scrape_all_pages():
    all_books = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()

        page.set_default_timeout(TIMEOUT)

        logging.info(f"Opening website: {BASE_URL}")
        print(f"🌐 Opening: {BASE_URL}")

        page.goto(BASE_URL, wait_until="networkidle")
        time.sleep(WAIT_TIME / 1000)

        current_url = BASE_URL
        page_num = 1

        while True:
            print(f"📄 Scraping page {page_num}...")
            logging.info(f"Scraping page {page_num}: {current_url}")

            html = page.content()
            books, next_url = parse_books(html, BASE_URL)
            all_books.extend(books)

            print(f"→ Extracted {len(books)} books")
            logging.info(f"Extracted {len(books)} books from page {page_num}")

            if not next_url:
                logging.info("No more pages. Scraping finished.")
                print("⛔ No more pages.")
                break

            page.goto(next_url, wait_until="networkidle")
            time.sleep(WAIT_TIME / 1000)

            current_url = next_url
            page_num += 1

        browser.close()

    return all_books