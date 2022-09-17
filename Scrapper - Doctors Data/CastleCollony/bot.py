import requests
import bs4


def func(value):
    return ''.join(value.splitlines())

def scrap_for_data(x):
    try:
        output = ""
        website = x
        request_result = requests.get(website)
        soup = bs4.BeautifulSoup(request_result.content, "html.parser")
        All_Doctors = soup.find_all(
            "li", class_="SearchResultsModule-results-item")
        for Doctor in All_Doctors:
            Name = Doctor.find("div", class_="PromoSearchResult-title")
            Profile = Name.find("a", class_="Link")
            State = Doctor.find("div", class_="PromoSearchResult-address")
            Special = Doctor.find("div", class_="PromoSearchResult-specialty")
            Phone = Doctor.find(
                "div", class_="PromoSearchResult-phoneNumber-item")
            Hospital = Doctor.find(
                "div", class_="PromoSearchResult-related-mobile")

            Name = Name.getText().strip("\n")
            State = State.getText().strip("\n").replace(",", " ")
            Special = Special.getText().strip("\n").replace(",", " ")
            Phone = Phone.getText().strip("\n").replace(",", " ")
            Hospital = Hospital.getText().strip("\n").replace(",", " ")
            Hospital = func(Hospital)
            Profile = Profile.get("href").strip("\n")
            
            print("==========================================================")
            print("Name: " + Name)
            print("State: " + State)
            print("Special: " + Special)
            print("Phone: " + Phone)
            print("Hospital: " + Hospital)
            print("Profile: " + Profile)
            print("==========================================================")

            output = output + Name + "," + State + "," + Phone + \
                "," + Hospital + "," + Special + "," + Profile + "\n"
    except:
        print("ERROR")

    return output


with open("Links_To_Search.txt", "r") as file:
    with open("Output.csv", "w") as outputfile:
        outputfile.write("Name,State,Phone,Hospital,Speciality,Profile\n")
        for i in file.readlines():
            print("Searching: " + str(i))
            v = scrap_for_data(i.rstrip('\n'))
            try:
                if (len(v) > 1):
                    outputfile.write(v)
                else:
                    print("Searching....")
            except:
                print("Error")


print("Search Completed..........")
