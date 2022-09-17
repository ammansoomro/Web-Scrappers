import requests
import bs4

def scrap_for_data(x):
    request_result = requests.get(x)
    soup = bs4.BeautifulSoup(request_result.content, "html.parser")
    Title = soup.find_all("h1", class_="profile-name text-overflow")
    for x in Title:
        break
    return x.text.strip()

Start_Range = int(input("Enter the start range: "))
End_Range = int(input("Enter the end range: "))
OutputName = input("Output Name: ")
with open(OutputName + ".csv", "w") as outputfile:
    outputfile.write("Email\n")
    for x in range(Start_Range, End_Range):
        try:
            print(str(x) + " | " + str(End_Range) + " - Remaining: " + str(End_Range - x))
            output = scrap_for_data("https://www.roblox.com/users/" + str(x) + "/profile")
            outputfile.write(str(output) + "@gmail.com\n")
        except:
            pass