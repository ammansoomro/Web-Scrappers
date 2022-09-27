from calendar import c
import requests
import json
# Import bs4
import bs4

url = "https://www.twitch.tv/esl_csgo"
# Get Status Code of the Site
def getStatusCode(url):
    response = requests.get(url)
    return response.status_code

# Get the Title of the Site
def getTitle(url):
    response = requests.get(url)
    return response.text
# Scrape No of Views of the Stream
def getViews(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    result = soup.find("div", class_="Layout-sc-nxg1ff-0 gcwIMz")
    print(result)


# Print TItle and Status Code
def main():
    print("Status Code: " + str(getStatusCode(url)))
    getViews(url)
if __name__ == "__main__":
    main()
    