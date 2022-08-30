with open("Keywords.txt", "r") as file:
    with open("Keyword_To_Website.csv", "w") as outputfile:
        for i in file.readlines():
            try:
                i = i.replace(" ", "-").strip("\n")
                word = "https://www.castleconnolly.com/specialty/"+i+"/washington-dc" + "\n"
                outputfile.write(word)

                i = i.replace(" ", "-").strip("\n")
                word = "https://www.castleconnolly.com/specialty/"+i+"/kansas-city-ks" + "\n"
                outputfile.write(word)
            except:
                print("Error")