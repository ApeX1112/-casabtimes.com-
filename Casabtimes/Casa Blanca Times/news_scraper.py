import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://alhoukouma.gov.ma"
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.content, "html.parser")
news_articles = soup.find_all("div", class_="article-content")

# HTML template for displaying news
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latest News</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }}
        .news-item {{
            margin-bottom: 20px;
        }}
        .title {{
            font-weight: bold;
            font-size: 1.2em;
        }}
        .date {{
            color: #666;
            font-size: 0.8em;
        }}
        .content {{
            margin-top: 10px;
        }}
    </style>
</head>
<body>
    <h1>Latest News</h1>
    {}
</body>
</html>
"""

# Initialize an empty list to store news items
news_items_html = []

# Extract relevant information from each news article
for article in news_articles:
    title = article.find("h2").text.strip()
    date = article.find("span", class_="date").text.strip()
    content = article.find("div", class_="content").text.strip()

    # Create HTML for each news item
    news_item_html = f"""
    <div class="news-item">
        <div class="title">{title}</div>
        <div class="date">{date}</div>
        <div class="content">{content}</div>
    </div>
    """
    news_items_html.append(news_item_html)

# Combine all news items into the final HTML content
final_html = html_template.format("\n".join(news_items_html))

# Save the HTML content to a file
with open("latest_news.html", "w", encoding="utf-8") as file:
    file.write(final_html)

print("Latest news scraped and saved to 'latest_news.html'")
