import requests
from bs4 import BeautifulSoup

url = 'https://es.wikipedia.org/wiki/Anexo:Videos_m%C3%A1s_vistos_en_YouTube'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Most Viewed YouTube Videos on Wikipedia:")
    videos_table = soup.find('table', {'class': 'wikitable'})
    for row in videos_table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) > 1:
            video_title = cols[0].get_text(strip=True)
            video_channel = cols[1].get_text(strip=True)
            video_views = cols[2].get_text(strip=True)
            video_publication_date = cols[3].get_text(strip=True)
            print(f"Title: {video_title}, Channel: {video_channel}, Views: {video_views}")
    print("Data successfully retrieved and parsed.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")