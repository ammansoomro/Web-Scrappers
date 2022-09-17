import numpy as np
from requests_html import HTMLSession
from requests_html import HTMLSession

loss = 0


def google_search(query, count):
    response = get_results(query, count)
    return parse_results(response, query)


def get_results(query, count):
    response = get_source("https://google.com/search?q=" +
                          query + "&start=" + str(count))
    return response


def get_source(url):
    session = HTMLSession()
    response = session.get(url)
    return response


def parse_results(response, keyword):
    try:
        css_identifier_result = ".tF2Cxc"
        css_identifier_title = "h3"
        css_identifier_link = ".yuRUbf a"
        css_identifier_text = ".VwiC3b"
        results = response.html.find(css_identifier_result)

        output = ""

        for result in results:
            print("============================================================")
            title = (result.find(css_identifier_title)
                     [0].text).strip().replace(",", "")
            link = result.find(css_identifier_link)[0].attrs['href']
            text = (result.find(css_identifier_text)[
                    0].text).strip().replace(",", "")
            print("Title: " + title)
            print("Link: " + link)
            print("Text: " + text)
            print("============================================================")
            searchwords = keyword.lower().split(" ")
            length = len(searchwords)
            newEntry = title + "," + link + "," + text + "\n"

            ################### NUMPY TESTING ################################
            SearchingWords = keyword.lower().split(" ")
            SearchingQuery = title + " " + link + " " + text
            SearchingQuery = SearchingQuery.lower().replace(
                ',', " ").replace('.', " ").replace("-", " ").split(" ")
            SearchingWords = np.array(SearchingWords)
            SearchingQuery = np.array(SearchingQuery)
            if (np.intersect1d(SearchingWords, SearchingQuery).size == SearchingWords.size):
                output = output + newEntry
            ################### NUMPY TESTING ################################

    except Exception as e:
        print("Searcing...")

    return output


# OPENING AND WRITING IN FILE
filename = input("Enter Output filename:")
with open(filename + ".csv", "w", encoding='utf-8') as outputfile:
    outputfile.write("Title,Link,Text\n")
    Keyword = input("Enter Keyword: ")
    count = 0
    while count < 250:
        Output = google_search(Keyword, count)
        count += 10
        if (len(Output) > 1):
            outputfile.write(Output)
        elif loss == 4:
            print("Search Complete")
            exit(0)
        else:
            loss += 1


print("Search Complete")
# END OF PROGRAM
