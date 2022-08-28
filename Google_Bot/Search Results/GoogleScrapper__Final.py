import requests
import bs4


def scrap_for_data(x, y, text):
    output = ""
    website = x
    keyword = y.lower()
    url = "http://" + website+"/?s=" + text
    print(url)
    request_result = requests.get(url)
    print(request_result.status_code)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    # print(soup)
    #################### Scrape Headings of the Results ####################
    heading_object = soup.find_all('h3')
    for info in heading_object:
        if (str(info.parent.get('href')).find(website) > -1):
            if (info.getText().lower().find(keyword) > -1):
                print(info.getText())
                output = output + info.getText() + ","
                x = str(info.parent.get('href'))
                end = x.find("&")
                print(x[7:end])
                output = output + x[7:end] + "\n"
                print("------")

    return output

    #################### Scrape Headings of the Results ####################


with open("potentialLinks.txt", "r") as file:
    with open("WebsitesResult.csv", "w") as outputfile:
        outputfile.write("Title,Link\n")
        mytext = input("Enter your Keyword: ")
        for i in file.readlines():
            print("================== CALL ====================")
            text = mytext
            print(text)
            v = scrap_for_data(i.rstrip('\n'), mytext, text)
            if (len(v) > 1):
                outputfile.write(v)
            else:
                v = "Not Found" + "," + i
                outputfile.write(v)
