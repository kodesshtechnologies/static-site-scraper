from bs4 import BeautifulSoup
from urllib.parse import urljoin
from src.utils import clean


def parse_books(html, base_url):
    soup = BeautifulSoup(html, "lxml")

    book_cards = soup.select("article.product_pod")
    results = []

    for card in book_cards:
        title = clean(card.h3.a["title"])
        price = clean(card.select_one("p.price_color").get_text())
        availability = clean(card.select_one("p.instock.availability").get_text())
        
        rating_class = card.select_one("p.star-rating")
        rating = rating_class["class"][1] if rating_class else ""

        detail_url = urljoin(base_url, card.h3.a["href"])

        results.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating,
            "URL": detail_url,
        })

    # Pagination next button
    next_button = soup.select_one("li.next > a")
    next_url = urljoin(base_url, next_button["href"]) if next_button else None

    print("Next Page URL:", next_url)

    return results, next_url