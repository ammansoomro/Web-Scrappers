from bs4 import BeautifulSoup
import requests

# Function to extract Product Title


def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find(
            "span", attrs={"class": 'a-size-medium a-color-base a-text-normal'})

        # Inner NavigableString Object
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip()

        # # Printing types of values for efficient understanding
        # print(type(title))
        # print(type(title_value))
        # print(type(title_string))
        # print()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price


def get_price(soup):
    try:
        price = soup.find("span", attrs={'class': 'a-offscreen'})
        price = str(price)
        price = price.replace('<span class="a-offscreen">',
                              '').replace('</span>', '')
    except AttributeError:
        price = ""

    return price
# Function to extract Product Rating


def get_rating(soup):

    try:
        rating = soup.find(
            "i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()

    except AttributeError:

        try:
            rating = soup.find(
                "span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""

    return rating

# Function to extract Number of User Reviews


def get_review_count(soup):
    try:
        review_count = soup.find(
            "span", attrs={'class': 'a-size-base s-underline-text'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count

# Function to extract Availability Status


def get_Image(soup):
    try:
        image = soup.find("img", attrs={'class': 's-image'}).attrs['src']
    except AttributeError:
        image = ""

    return image


if __name__ == '__main__':

    # Headers for request
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL
    Keyword = input("Enter Keyword: ")
    Keyword = Keyword.replace(" ", "+")
    URL = "https://www.amazon.com/s?k=" + Keyword
    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, 'html.parser')
    results = soup.find_all('div', attrs={'class': 'sg-row'})
    for result in results:
        # Extract data
        title = get_title(result)
        price = get_price(result)
        rating = get_rating(result)
        review_count = get_review_count(result)
        Image = get_Image(result)

        if (title != ""):
            # Printing the data
            print('Product Title =', title)
            print('Product Price =', price)
            print('Product Rating =', rating)
            print('Number of Reviews =', review_count)
            print('Image =', Image)
            print()
