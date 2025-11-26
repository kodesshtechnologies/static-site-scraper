import logging
import os

# Create folders if missing
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean(text: str) -> str:
    if not text:
        return ""
    return " ".join(text.strip().split())     # remove extra spaces