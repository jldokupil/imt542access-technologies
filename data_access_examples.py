
import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_json_from_api():
    """
    Access Type: API connection over HTTP
    Format: JSON

    Pros:
    - Easy to automate and integrate into pipelines
    - Often returns structured, queryable data
    - Real-time data availability

    Cons:
    - Requires internet access and authentication (in many cases)
    - Rate limits or downtime can affect reliability
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    print("Sample JSON from API:")
    print(data[:2])  # Print a sample

def read_local_csv():
    """
    Access Type: Manual file download and read locally
    Format: CSV

    Pros:
    - No dependency on internet or external services
    - Fast access for small to medium datasets
    - Easy to manipulate with libraries like pandas

    Cons:
    - Manual effort to maintain freshness of data
    - Not ideal for real-time or large-scale access
    """
    try:
        df = pd.read_csv("sample.csv")  # Ensure this file exists locally
        print("Sample from CSV file:")
        print(df.head(2))  # Print a sample
    except FileNotFoundError:
        print("sample.csv not found. Please make sure the file exists in the same directory.")

def scrape_html_webpage():
    """
    Access Type: HTTP to download webpage
    Format: HTML

    Pros:
    - Useful when data is only available visually
    - Can extract structured info from unstructured sources

    Cons:
    - Fragile to webpage layout changes
    - Slower and less structured than API access
    """
    url = "https://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Webpage title from HTML:")
    print(soup.title.text)  # Print a sample (page title)

if __name__ == "__main__":
    fetch_json_from_api()
    read_local_csv()
    scrape_html_webpage()
