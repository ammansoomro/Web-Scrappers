import requests
import bs4


def scrap_for_data(y, count):
    output = ""
    keyword = y.lower()
    url = 'https://google.com/search?q=' + keyword + "&start=" + str(count)
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    #################### Scrape Headings of the Results ####################
    heading_object = soup.find_all('h3')
    for info in heading_object:
        if (len(str(info.parent.get('href'))) > 0):
            if (info.getText().lower().find(keyword) > -1):
                print(info.getText().lower().find(keyword))
                print(info.getText())
                output = output + info.getText() + ","
                x = str(info.parent.get('href'))
                end = x.find("&")
                print(x[7:end])
                output = output + x[7:end] + "\n"
                print("------")

    return output


#################### Scrape Headings of the Results ####################
# scrap data from bing for the given keyword
filename = input("Enter Output filename: ")
with open(filename + ".csv", "w", encoding='utf-8') as outputfile:
    try:
        outputfile.write("Title,Link\n")
        mytext = input("Enter your Keyword: ")
        count = 0
        while count < 250:
            v = scrap_for_data(mytext, count)
            count += 10
            print(" ")
            if (len(v) > 1):
                outputfile.write(v)
            else:
                exit(0)
            print(" ")
    except Exception as e:
        print(e)
        print("Error")