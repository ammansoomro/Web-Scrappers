import numpy as np
from requests_html import HTMLSession
from requests_html import HTMLSession
import bs4

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
        css_identifier_price = ".fG8Fp"
        results = response.html.find(css_identifier_result)

        output = ""

        for result in results:
            print("============================================================")
            title = (result.find(css_identifier_title)
                     [0].text).strip().replace(",", "")
            link = result.find(css_identifier_link)[0].attrs['href']
            text = (result.find(css_identifier_text)[
                    0].text).strip().replace(",", "")
            price = (result.find(css_identifier_price)[
                     0].text).strip().replace(",", "")
            print("============================================================")
            print("Title: " + title)
            print("Link: " + link)
            print("Text: " + text)
            print("Price: " + price)
            print("============================================================")
            output += title + "," + price + "," + link + "," + text + "\n"

    except Exception as e:
        print("Searcing...")

    return output


# OPENING AND WRITING IN FILE
filename = input("Enter Output filename:")
with open(filename + ".csv", "w", encoding='utf-8') as outputfile:
    outputfile.write("Title,Price,Link,Text\n")
    Keyword = input("Enter Keyword: ")
    count = 220
    while count < 310:
        Output = google_search(Keyword, count)
        count += 10
        if (len(Output) > 1):
            outputfile.write(Output)


print("Search Complete")
# END OF PROGRAM
