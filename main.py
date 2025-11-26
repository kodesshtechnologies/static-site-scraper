import os
import json
import pandas as pd
from src.scraper import scrape_all_pages

os.makedirs("output", exist_ok=True)

if __name__ == "__main__":
    print("🚀 Starting Books To Scrape Crawler...")

    data = scrape_all_pages()

    # Save CSV
    csv_path = "output/books.csv"
    pd.DataFrame(data).to_csv(csv_path, index=False)

    # Save JSON
    json_path = "output/books.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"🎉 Scraping finished!")
    print(f"📁 CSV saved → {csv_path}")
    print(f"📁 JSON saved → {json_path}")
    print(f"📚 Total books scraped: {len(data)}")