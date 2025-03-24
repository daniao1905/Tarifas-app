import requests
from bs4 import BeautifulSoup
import re

def get_vehicle_tariffs():
    url = "https://www.mk-group.co.jp/osaka/hire/"
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")

    vehicles = {}

    for section in soup.find_all("section", class_="hire_box"):
        name_tag = section.find("h3")
        if not name_tag:
            continue

        vehicle_name = name_tag.get_text(strip=True)
        table = section.find("table")
        if not table:
            continue

        rows = table.find_all("tr")
        tariffs = {}

        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 2:
                time_text = cols[0].get_text(strip=True)
                price_text = cols[1].get_text(strip=True)

                hours_match = re.search(r"(\d+)(?:時間)?", time_text)
                if hours_match:
                    hours = int(hours_match.group(1))
                    price = int(re.sub(r"[^\d]", "", price_text))
                    tariffs[hours] = price

        vehicles[vehicle_name] = tariffs

    return vehicles
