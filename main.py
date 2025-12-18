import requests
from bs4 import BeautifulSoup
import json

def main():

    headers = {
    "User-Agent": "learning-web-scraping/1.0"
    }

    URL = "https://en.wikipedia.org/wiki/Khabib_Nurmagomedov"

    response = requests.get(URL, headers=headers)
    print(response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table", "wikitable")
    matches = tables[1]
    trs = matches.find_all("tr")

    opponents = []

    for tr in trs:
        tds = tr.find_all("td")
        if not tds:
            continue

        opponent_node = tds[2]
        opponent_name = opponent_node.string

        if opponent_name is None:
            opponent_name = opponent_node.a.string
            
        opponents.append(opponent_name.strip("\n"))

    print(opponents)
    opponents_json = json.dumps(opponents)
    print(opponents_json)
        



    # example

    # with open("khabib.html", "w", encoding="utf-8") as f:
    #         contents = f.read()
    #         print(contents)

    with open("khabib_opponents.json", "w", encoding="utf-8") as f:
        f.write(opponents_json)



main()

