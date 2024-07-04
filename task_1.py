import requests
import json
from googleapiclient.discovery import build
from bs4 import BeautifulSoup

# get GOOGLE SEARCH RESULTS
# Define your API key and Custom Search Engine ID
API_KEY = 'XYZ1234'
CSE_ID = '5655WYXZ1234:abc1234xyz'

def google_search(query, api_key, cse_id, num=10):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query, cx=cse_id, num=num).execute()
    return res['items']

# ---------------------------------------------------------------------------------------------

# SCRAPE INDIVIDUAL URLS
def scrape_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return {
                'url': url,
                'title': soup.title.string if soup.title else 'No title',
                'content': soup.get_text()
            }
    except Exception as e:
        return {'url': url, 'error': str(e)}

#---------------------------------------------------------------------------------------------------------

# SAVE TO JSON
def save_to_json(data, filename='results.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ---------------------------------------------------------------------------------------------

# Example usage
query = 'weeknd'
results = google_search(query, API_KEY, CSE_ID)
urls = [item['link'] for item in results]
scraped_data = [scrape_url(url) for url in urls]
save_to_json(scraped_data)
