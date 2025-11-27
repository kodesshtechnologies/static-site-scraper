# -----------------------------
# 1. Use official Playwright Python image
#    Includes Chromium, WebKit, Firefox + system dependencies
# -----------------------------
FROM mcr.microsoft.com/playwright/python:v1.40.0-focal

# -----------------------------
# 2. Set working directory
# -----------------------------
WORKDIR /app

# -----------------------------
# 3. Copy project files
# -----------------------------
COPY . .

# -----------------------------
# 4. Install dependencies
# -----------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# 5. Install Playwright browsers
# -----------------------------
RUN playwright install --with-deps

# -----------------------------
# 6. Create folders for output and logs
# -----------------------------
RUN mkdir -p /app/output /app/logs

# -----------------------------
# 7. Default command
#    Render Cron Job will execute this to run the scraper
# -----------------------------
CMD ["python", "main.py"]