import requests
import bs4


def scrap_for_data(x, y, text):
    try:
        output = ""
        website = x
        keyword = y.lower()
        url = 'https://google.com/search?q=' + text
        request_result = requests.get(url)
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
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
    except:
        print(" ")

    return output

    #################### Scrape Headings of the Results ####################


with open("potentialLinks.txt", "r") as file:
    filename = input("Enter Output filename: ")
    with open(filename + ".csv", "w") as outputfile:
        outputfile.write("Title,Link\n")
        mytext = input("Enter your Keyword: ")
        for i in file.readlines():
            print("================== CALL ====================")
            text = i.rstrip('\n') + " " + mytext
            print(text)
            try:
                v = scrap_for_data(i.rstrip('\n'), mytext, text)
            except:
                print(" ")

            try:
                if (len(v) > 1):
                    outputfile.write(v)
                else:
                    v = "Not Found" + "," + i
                    outputfile.write(v)
            except:
                print(" ")
