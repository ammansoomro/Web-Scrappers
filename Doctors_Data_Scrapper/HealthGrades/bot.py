import requests
import bs4


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
        Address = soup.find(
            "address", {'class': 'location-row-address'})
        State = soup.find(
            "a", {'class': 'breadcrumb-link link--secondary',
                  'data-qa-target': 'breadcrumb-city-directory'})
        print("==========================================================")
        print("Name:" + Name.getText())
        Doctor_Name = "Not Found"
        Doctor_Name = Name.getText().replace(",", " ").strip("\n")
        try:
            Phone_01 = "Not Found"
            Phone_01 = str(Phone).replace(",", " ").strip("\n")
        except Exception as e:
            print(e)
        try:
            Phone_02 = "Not Found"
            Phone_02 = str(Phone02).replace(",", " ").strip("\n")
        except Exception as e:
            print(e)
        try:
            Phone_03 = "Not Found"
            Phone_03 = str(Phone03).replace(",", " ").strip("\n")
        except Exception as e:
            print(e)
        try:
            Doctor_Gender = "Not Found"
            Doctor_Gender = Gender.getText().replace(",", " ").strip("\n")
        except Exception as e:
            print(e)
        try:
            Doctor_Address = "Not Found"
            Doctor_Address = Address.getText().replace(",", " ").strip("\n")
        except Exception as e:
            print(e)
        try:
            Doctor_State = "Not Found"
            Doctor_State = State.getText().replace(",", " ").strip("\n")
        except Exception as e:
            print(e)
        print("==========================================================")
        output = output + Doctor_Name + "," + Phone_01 + "," + Phone_02 + "," + \
            Phone_03 + "," + Doctor_Gender + "," + Doctor_Address + "," + Doctor_State + "\n"
    except Exception as e:
        print(e)

    return output


with open("HealthGrades.txt", "r") as file:
    Filename = input("Enter File Name")
    with open(Filename+".csv", "w") as outputfile:
        outputfile.write("Name,Phone01,Phone02,Phone03,Gender,Address,State\n")
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
