from bs4 import BeautifulSoup
import requests
import os
# ====================================== Title ======================================


def get_title(item, count):
    try:
        itemNo = "search#productTile"+str(count)+"#product-name"
        title = item.find("span", attrs={"data-qa": itemNo})
        title = title.contents[0]
    except AttributeError:
        title = ""
    return title
# ====================================== Platform ======================================


def get_link(item, count):
    try:
        itemNo = "search#productTile"+str(count)
        link = item.find("div", attrs={"data-qa": itemNo})
        link = "https://store.playstation.com" + link.a["href"]
    except AttributeError:
        link = ""
    return link
# ====================================== Link ======================================


def get_platform(item, count):
    try:
        itemNo = "search#productTile"+str(count)+"#game-art#tag0"
        platform = item.find("span", attrs={"data-qa": itemNo})
    except AttributeError:
        platform = ""
    return platform
# ====================================== Price ======================================


def get_price(item, count):
    try:
        itemNo = "search#productTile"+str(count)+"#price#display-price"
        price = item.find("span", attrs={"data-qa": itemNo})
        price = price.contents[0]
    except AttributeError:
        price = ""
    return price
# ====================================== Image ======================================


def get_Image(item,count,keyword):
    try:
        itemNo = "search#productTile"+str(count)+"#game-art#image"
        image = item.find("span", attrs={'data-qa': itemNo})
        image = image.contents[1].contents[0].attrs['src']
        image = requests.get(image).content
        with open(keyword + "/"+ str(count) + '.png', 'wb') as handler:
            handler.write(image)
    except AttributeError:
        image = ""
# ====================================== Product Type ======================================


def get_ProductType(item, count):
    try:
        itemNo = "search#productTile"+str(count)+"#product-type"
        product_type = item.find("span", attrs={'data-qa': itemNo})
        product_type = product_type.contents[0]
    except AttributeError:
        return False
    return True


if __name__ == '__main__':
    # Headers for request
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
    Keyword = input("Enter Keyword: ").replace(" ", "+")
    URL = "https://store.playstation.com/en-gb/search/" + Keyword
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    results = soup.find('ul', class_='psw-grid-list psw-l-grid')
    items = results.find_all('li')
    count = 0
    path = os.getcwd()
    path = os.path.join(path, Keyword)
    os.mkdir(path)
    print(path)
    with open(Keyword + "/" + Keyword + ".csv", "w") as outputfile:
        outputfile.write("Index,Title,Price,Link\n")    
        for item in items:
            product_type = get_ProductType(item, count)
            if (product_type):
                pass
            else:
                title = get_title(item, count)
                price = get_price(item, count)
                link = get_link(item, count)
                # platform = get_platform(item, count)
                get_Image(item,count,Keyword)
                print("Count: " + str(count))
                print("Title: " + title)
                print("Price: " + price)
                print("Link: " + link)
                print("=====================================")
                row = str(count)
                outputfile.write(row + "," + title + "," + price + "," + link + "\n")
            count = count + 1
