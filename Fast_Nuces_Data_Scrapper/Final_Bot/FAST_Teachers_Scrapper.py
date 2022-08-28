import requests
import bs4


def scrap_for_data(x):
    try:
        output = ""
        website = x
        request_result = requests.get(website)
        soup = bs4.BeautifulSoup(request_result.content, "html.parser")
        All_Teachers_Data = soup.find_all("div", class_="single-team-area")
        for Teacher_Data in All_Teachers_Data:
            TeacherName = Teacher_Data.find("div", class_="tlp-position")
            TeacherImage = Teacher_Data.find(
                "img", class_="img-responsive rt-team-img")
            TeacherImage = str(TeacherImage.get("src"))
            TeacherImage = requests.get(TeacherImage).content
            TeacherEmail = Teacher_Data.find("li", class_="tlp-email")
            TeacherEmail = TeacherEmail.find("span")
            TeacherName = TeacherName.find("a")

            Name = str(TeacherName.get("title")).strip().replace(",", "")
            Email = str(TeacherEmail.getText())
            Position = str(TeacherName.getText())
            Profile = str(TeacherName.get("href"))

            # Writing: Teacher Name, Teacher Email, Teacher Position and Teacher Profile to an array of output
            output = output + Name + "," + Email + "," + Position + "," + Profile + "\n"
            print(Name)

            # Saving Teachers Profile Picture to Images Folder
            with open('TeacherImages/' + str(Name) + '.jpg', 'wb') as handler:
                handler.write(TeacherImage)
    except:
        print("ERROR")

    return output


with open("Links_To_Search.txt", "r") as file:
    with open("Output.csv", "w") as outputfile:
        outputfile.write("Name,Email,Position,Profile\n")
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
