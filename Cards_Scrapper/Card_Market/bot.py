import requests
import bs4


def func(value):
    return ''.join(value.splitlines())


def scrap_for_data(x):
    try:
        count = 0
        output = ""
        website = x
        request_result = requests.get(website)
        soup = bs4.BeautifulSoup(request_result.content, "html.parser")
        Table = soup.find("div", class_="table-body")
        for row in Table.findChildren("div", recursive=False):
            # Name
            Name = row.contents[3].contents[0].contents[0].a.contents[0]
            Name = Name.replace(",", " ").strip()
            print(Name)
            # Link
            Link = row.contents[3].contents[0].contents[0].a['href']
            print(Link)
            # In Stock
            try:
                inStock = row.contents[4].contents[0].contents[0]
                print(inStock)
            except:
                inStock = "N/A"
            # Price
            Price = row.contents[5].contents[0]
            Price = Price.replace(",", ".").strip()
            print(Price)
            # Rarity
            try:
                Rarity = row.contents[3].contents[0].contents[2].contents[0].span['data-original-title']
                Rarity = Rarity.replace(",", " ").strip()
                print(Rarity)
            except:
                Rarity = "N/A"
            # Origin
            try:
                Origin = row.contents[2].contents[0]['title']
                Origin = Origin.replace(",", " ").strip()
                print(Origin)
            except:
                Origin = "N/A"
            # Output
            output += Origin + "," + Name + "," + Price + "," + Rarity + "," + inStock + "," + "https://www.cardmarket.com" + Link + "\n"

    except Exception as e:
        print("Error: " + str(e))

    return output


with open("Links_To_Search.txt", "r") as file:
    OutputName = input("Output Name: ")
    with open(OutputName + ".csv", "w") as outputfile:
        outputfile.write("Origin,Name,Price,Rarity,Stock,Link\n")
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
