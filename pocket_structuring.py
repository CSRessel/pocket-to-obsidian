import re
import csv
from datetime import datetime

def parse_article(html_line):
    """
    Parse an individual article line from the HTML input.
    """
    url = re.search(r'href="(.*?)"', html_line).group(1)
    title = re.search(r'>(.*?)</a>', html_line).group(1)
    time_added = int(re.search(r'time_added="(.*?)"', html_line).group(1))
    tags = re.search(r'tags="(.*?)"', html_line).group(1)
    return title, url, time_added, tags

def extract_articles_from_html(html_content):
    """
    Extract articles from the given HTML content.
    """
    lines = html_content.split("\n")
    articles = []
    for line in lines:
        if '<li><a href=' in line:
            title, url, time_added, tags = parse_article(line)
            readable_date = datetime.utcfromtimestamp(time_added).strftime('%Y-%m-%d %H:%M:%S')
            articles.append({"Title": title, "URL": url, "Time Added": readable_date, "Tags": tags})
    return articles

def write_articles_to_csv(articles, csv_filename):
    """
    Write the list of articles to a CSV file.
    """
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "URL", "Time Added", "Tags"])
        writer.writeheader()
        for article in articles:
            writer.writerow(article)

def main():
    with open("sample-pocket-export.html", "r") as file:
        html_content = file.read()
    articles = extract_articles_from_html(html_content)
    csv_filename = "output.csv"
    write_articles_to_csv(articles, csv_filename)

if __name__ == "__main__":
    main()
