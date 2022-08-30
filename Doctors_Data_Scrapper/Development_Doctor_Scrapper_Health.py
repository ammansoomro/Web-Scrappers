import requests
import bs4
from lxml import etree


def scrap_for_data(x):
    try:
        output = ""
        website = x
        request_result = requests.get(website)
        soup = bs4.BeautifulSoup(request_result.content, "html.parser")
        Name = soup.find(
            "h1", {'data-qa-target': 'ProviderDisplayName'})
        Phone = soup.find(
            "a", {'class': 'summary-standard-phone-link'})
        Phone02 = soup.find(
            "a", {'class': 'click-to-call-button-primary'})
        Phone03 = soup.find(
            "a", {'class': 'summary-standard-toggle-phone-number-button'})
        Gender = soup.find(
            "span", {'data-qa-target': 'ProviderDisplayGender'})
        print("==========================================================")
        print(Name.getText())
        print(str(Phone).split(" "))
        print(str(Phone02).split(" "))
        print(Phone03)
        print(Gender.getText())
        print("==========================================================") 
        print(" ")
    except Exception as e:
        print(e)

    return output


with open("HealthGrades.txt", "r") as file:
    with open("Output.csv", "w") as outputfile:
        outputfile.write("Name\n")
        for i in file.readlines():
            v = scrap_for_data(i.rstrip('\n'))
            try:
                if (len(v) > 1):
                    outputfile.write(v)
                else:
                    i = i.rstrip('\n')
                    v = "Not Found" + "," + i
                    outputfile.write(v)
            except:
                print("Error")


print("Search Completed..........")
