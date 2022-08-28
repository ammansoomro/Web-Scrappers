import requests
import bs4


def scrap_for_data(x, y, text):
    try:
        flag = 0            if (str(info.parent.get('href')).find(website) > -1):

        output = ""
        website = x
        keyword = y.lower()
################################## SEARCH  ##################################
        url = "http://" + website+"/?s=" + text
        print(url)
        request_result = requests.get(url)
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

        print("STATUS CODE: " + str(request_result.status_code))
        soup = bs4.BeautifulSoup(request_result.content, "html.parser")
        links = soup.find_all("a")
        for link in links:
            if ("FBA".lower() in link.text.lower()):
                print("Found")
                output = output + link.text.strip().replace(",", "") + \
                    "," + link['href'] + "\n"
                flag = flag + 1
            else:
                continue

        if (flag > 1):
            return output
        
        flag = 0
        # print("------")
################################## SEARCH  ##################################
        url = "http://" + website+"/search.html?group=0&key=" + text
        print(url)
        request_result = requests.get(url)
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
            if ("FBA".lower() in link.text.lower()):
                print("Found")
                output = output + link.text.strip().replace(",", "") + "," + "http://" + \
                    website + link['href'] + "\n"
                flag = flag + 1
            else:
                continue

        if (flag > 1):
            return output
        
        flag = 0
################################## SEARCH  ##################################
        url = "http://" + website+"/filterSearch?q=" + text
        print(url)
        request_result = requests.get(url)
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
            if ("FBA".lower() in link.text.lower()):
                print("Found")
                output = output + link.text.strip().replace(",", "") + "," + "http://" + \
                    website + link['href'] + "\n"
                flag = flag + 1
            else:
                continue

        if (flag > 1):
            return output
        
        flag = 0

################################## SEARCH  ##################################
################################## SEARCH  ##################################
        url = "http://" + website+"/search/?search=" + text
        print(url)
        request_result = requests.get(url)
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
            if ("FBA".lower() in link.text.lower()):
                print("Found")
                output = output + link.text.strip().replace(",", "") + "," + "http://" + \
                    website + link['href'] + "\n"
                flag = flag + 1
            else:
                continue

        if (flag > 1):
            return output
        
        flag = 0
################################## SEARCH  ##################################
################################## SEARCH  ##################################
        url = "http://" + website+"/search?q=" + text
        print(url)
        request_result = requests.get(url)
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
            if ("FBA".lower() in link.text.lower()):
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
        url = "http://" + website+"/search/?search=" + text
        print(url)
        request_result = requests.get(url)
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
            if ("FBA".lower() in link.text.lower()):
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
        url = "http://" + website+"/srch?search=" + text
        print(url)
        request_result = requests.get(url)
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
            if ("FBA".lower() in link.text.lower()):
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
        url = "http://" + website+"/?do=googlesearch#gsc.tab=0&gsc.q=" + text + "&gsc.sort="
        print(url)
        request_result = requests.get(url)
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
            if ("FBA".lower() in link.text.lower()):
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
        url = "http://" + website+"?product_cat=&s=" + text + "&post_type=product"
        print(url)
        request_result = requests.get(url)
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
            if ("FBA".lower() in link.text.lower()):
                print("Found")
                print(link)
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
        url = "http://" + website+"/search?q=" + text
        print(url)
        request_result = requests.get(url)
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
            if ("FBA".lower() in link.text.lower()):
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
        url = "http://" + website+"/" + text
        print(url)
        request_result = requests.get(url)
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
            if ("FBA".lower() in link.text.lower()):
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


with open("potentialLinks.txt", "r") as file:
    with open("Output.csv", "w") as outputfile:
        outputfile.write("Title,Link\n")
        mytext = "Amazon FBA"
        for i in file.readlines():
            print("================== CALL ====================")
            text = mytext
            v = scrap_for_data(i.rstrip('\n'), mytext, text)
            try:
                if (len(v) > 1):
                    outputfile.write(v)
                else:
                    i = i.rstrip('\n') + "/?s=" + mytext + "\n"
                    v = "Not Found" + "," + i
                    outputfile.write(v)
            except:
                print("Error")


print("\n\n ###################### Search Completed ######################\n\n")
