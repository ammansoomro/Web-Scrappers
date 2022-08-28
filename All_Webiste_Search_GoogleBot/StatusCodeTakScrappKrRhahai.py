import requests
import bs4


def scrap_for_data(x, y, text):
    try:
        output = ""
        website = x
        keyword = y.lower()
        url = "http://" + website+"/?s=" + text
        print(url)
        request_result = requests.get(url)
        #################### Scrape Headings of the Results ####################
        if request_result.status_code == 521:
            return output
        
        if request_result.status_code == 522:
            return output
        
        if request_result.status_code == 523:
            return output
        
        
        output = output + str(request_result.status_code) + ","
        output = output + website + "\n"
        print("------")
    except:
        print("ERROR")

    return output

    #################### Scrape Headings of the Results ####################


with open("potentialLinks.txt", "r") as file:
    with open("WebsitesResult.csv", "w") as outputfile:
        outputfile.write("Status,Link\n")
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
