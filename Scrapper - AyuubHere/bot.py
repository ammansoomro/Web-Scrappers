from re import T
import bs4
import requests

searchWords = ["/?s=", "/search.html?group=0&key=", "/filterSearch?q=",
               "/search/?search=", "/usearch/", "/search?q=", "/search/?search=", "/srch?search=", "/", "/advanced-search/?term=", "/module/iqitsearch/searchiqit?s=", "/web/q/#query=", "/?"]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}


def scrap_for_data(x, y, text):
    try:
        flag = 0
        output = ""
        website = x
        keyword = text.lower()
        text = text.replace(" ", "+").lower()
        print("Searching for " + keyword + " on " + website)
################################## SEARCH  ##################################
        for webQuery in searchWords:
            url = "http://" + website + webQuery + text
            request_result = requests.get(url, headers=headers)
            print(url)
            if request_result.status_code == 521:
                output = output + "Error: Website Down" + \
                    "," + website + "\n"
                return output

            if request_result.status_code == 522:
                output = output + "Error: Website Down" + \
                    "," + website + "\n"
                return output

            if request_result.status_code == 523:
                output = output + "Error: Website Down" + \
                    "," + website + "\n"
                return output

            if request_result.status_code == 403:
                output = output + "Error 403: Bot Protected" + \
                    "," + website + "\n"
                return output

            if request_result.status_code == 503:
                output = output + "Error 503: Bot Protected" + \
                    "," + website + "\n"
                return output

            if request_result.status_code == 406:
                return output

            soup = bs4.BeautifulSoup(request_result.content, "html.parser")
            links = soup.find_all("a")
            for link in links:
                if (keyword in link.text.lower()):
                    output = output + link.text.strip().replace(",", "") + \
                        "," + link['href'] + "\n"
                    flag = flag + 1
                else:
                    continue

            if (flag > 1):
                return output

            flag = 0
################################## SEARCH  ##################################
################################## SEARCH  ##################################
        url = "http://" + website+"/?do=googlesearch#gsc.tab=0&gsc.q=" + text + "&gsc.sort="
        request_result = requests.get(url, headers=headers)
        print(url)
        if request_result.status_code == 521:
            output = output + "Error: Website Down" + \
                "," + website + "\n"
            return output

        if request_result.status_code == 522:
            output = output + "Error: Website Down" + \
                "," + website + "\n"
            return output

        if request_result.status_code == 523:
            output = output + "Error: Website Down" + \
                "," + website + "\n"
            return output

        if request_result.status_code == 403:
            output = output + "Error 403: Bot Protected" + \
                "," + website + "\n"
            return output

        soup = bs4.BeautifulSoup(request_result.content, "html.parser")
        links = soup.find_all("a")
        for link in links:
            if (keyword in link.text.lower()):
                print("Found")
                output = output + link.text.strip().replace(",", "") + \
                    "," + link['href'] + "\n"
                flag = flag + 1
            else:
                continue

        if (flag > 1):
            return output

        flag = 0
################################## SEARCH  ##################################
################################## SEARCH  ##################################
        url = "http://" + website+"/search/" + text + "/1/"
        print(url)
        request_result = requests.get(url, headers=headers)
        if request_result.status_code == 521:
            output = output + "Error: Website Down" + \
                "," + website + "\n"
            return output

        if request_result.status_code == 522:
            output = output + "Error: Website Down" + \
                "," + website + "\n"
            return output

        if request_result.status_code == 523:
            output = output + "Error: Website Down" + \
                "," + website + "\n"
            return output

        if request_result.status_code == 403:
            output = output + "Error 403: Bot Protected" + \
                "," + website + "\n"
            return output

        soup = bs4.BeautifulSoup(request_result.content, "html.parser")
        links = soup.find_all("a")
        for link in links:
            if (keyword in link.text.lower()):
                print("Found")
                output = output + link.text.strip().replace(",", "") + \
                    "," + link['href'] + "\n"
                flag = flag + 1
            else:
                continue

        if (flag > 1):
            return output

        flag = 0
################################## SEARCH  ##################################
        # print("------")

    except:
        print("ERROR")

    return output


text = input("Enter Search Word: ")
outputfileName = input("Enter Output File Name: ")
with open("Links.txt", "r") as file:
    with open(outputfileName+".csv", "w") as outputfile:
        outputfile.write("Title,Link\n")
        for i in file.readlines():
            print("================== CALL ====================")
            v = scrap_for_data(i.rstrip('\n'), text, text)
            try:
                if (len(v) > 1):
                    outputfile.write(v)
                else:
                    i = i.rstrip('\n') + "/?s=" + text + "\n"
                    v = "Not Found" + "," + i
                    outputfile.write(v)
            except:
                print("Error")


print("\n\n ###################### Search Completed ######################\n\n")
