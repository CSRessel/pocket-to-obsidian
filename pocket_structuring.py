import re
from datetime import datetime

# Function to parse an article
def parse_article(html_line):
    url = re.search(r'href="(.*?)"', html_line).group(1)
    title = re.search(r'>(.*?)</a>', html_line).group(1)
    time_added = int(re.search(r'time_added="(.*?)"', html_line).group(1))
    tags = re.search(r'tags="(.*?)"', html_line).group(1)
    return title, url, time_added, tags

def parse_document(lines):
    # Parsing and filtering for software articles
    software_articles = []
    for line in lines:
        if '<li><a href=' in line and 'tags="software"' in line:
            title, url, time_added, tags = parse_article(line)
            # Convert Unix timestamp to readable date format
            readable_date = datetime.utcfromtimestamp(time_added).strftime('%Y-%m-%d %H:%M:%S')
            software_articles.append({"Title": title, "URL": url, "Added Time": readable_date})
    return software_articles

def main():
    with open("sample-pocket-export.html") as infile:
        software_articles = parse_document(infile)
    # Sorting articles by 'Added Time'
    software_articles_sorted = sorted(software_articles, key=lambda x: x['Added Time'])
    print(software_articles_sorted)

if __name__ == "__main__":
    main()
