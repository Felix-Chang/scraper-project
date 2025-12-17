import requests as re

def main():

    headers = {
    "User-Agent": "learning-web-scraping/1.0"
    }

    URL = "https://en.wikipedia.org/wiki/Khabib_Nurmagomedov"

    response = re.get(URL, headers=headers)
    print(response.status_code)
    print(response.text)

    # example

    # with open("khabib.html", "w", encoding="utf-8") as f:
    #         contents = f.read()
    #         print(contents)

    with open("khabib_2.html", "w", encoding="utf-8") as f:
        f.write(response.text)



main()

