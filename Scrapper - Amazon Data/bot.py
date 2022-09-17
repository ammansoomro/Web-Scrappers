from bs4 import BeautifulSoup
import requests

# Function to extract Product Title
def get_title(soup):
	
	try:
		# Outer Tag Object
		title = soup.find("span", attrs={"id":'productTitle'})

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
		price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()

	except AttributeError:
		price = ""	

	return price

# Function to extract Product Rating
def get_rating(soup):

	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""	

	return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
	try:
		review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
		
	except AttributeError:
		review_count = ""	

	return review_count

# Function to extract Availability Status
def get_availability(soup):
	try:
		available = soup.find("div", attrs={'id':'availability'})
		available = available.find("span").string.strip()

	except AttributeError:
		available = ""	

	return available	

if __name__ == '__main__':

	# Headers for request
	HEADERS = ({'User-Agent':
	            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	            'Accept-Language': 'en-US, en;q=0.5'})

	# The webpage URL
	URL = ['https://www.amazon.com/Console-Horizon-Forbidden-Bundle-PlayStation-5/dp/B0B16656Z2/ref=sr_1_1?keywords=playstation+5&qid=1663388862&sprefix=play%2Caps%2C374&sr=8-1','https://www.amazon.com/PlayStation-5-Console/dp/B09DFCB66S/ref=sr_1_2?keywords=playstation+5&qid=1663388923&sprefix=play%2Caps%2C374&sr=8-2','https://www.amazon.com/Fortnite-Anime-Legends-PlayStation-5/dp/B0BDT7SY1X/ref=sr_1_3?keywords=playstation+5&qid=1663388923&sprefix=play%2Caps%2C374&sr=8-3','https://www.amazon.com/PlayStation-DualSense-Wireless-Controller-Starlight-Blue/dp/B09NLJGTHL/ref=sr_1_5?keywords=playstation+5&qid=1663388923&sprefix=play%2Caps%2C374&sr=8-5','https://www.amazon.com/Amazon-Basics-Clear-Smartphone-iPhone/dp/B099X2T3FJ/ref=sr_1_1_sspa?keywords=iphone+cover&qid=1663391155&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQVhGSTY3RklCRE1OJmVuY3J5cHRlZElkPUEwNDk0NDEyMVJVRk5QTlQ3SDRWOCZlbmNyeXB0ZWRBZElkPUEwMDQ4ODQxM0NaMUtEOENBWk9UVyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=','https://www.amazon.com/amFilm-Screen-Protector-iPhone-Tempered/dp/B01415QHYW/ref=sxin_14_ac_d_bv?ac_md=0-0-QnVkZ2V0IFBpY2s%3D-ac_d_bv_bv_bv&content-id=amzn1.sym.14453ffd-7768-40d0-9a7f-8d0063113f56%3Aamzn1.sym.14453ffd-7768-40d0-9a7f-8d0063113f56&cv_ct_cx=iphone+cover&keywords=iphone+cover&pd_rd_i=B01415QHYW&pd_rd_r=91331708-4d42-42b9-a82e-5e8de4cc402b&pd_rd_w=Tz1Xw&pd_rd_wg=w6oby&pf_rd_p=14453ffd-7768-40d0-9a7f-8d0063113f56&pf_rd_r=7FAH2TBSHWSXJQ1FD0D1&psc=1&qid=1663391155&sr=1-1-270ce31b-afa8-499f-878b-3bb461a9a5a6','https://www.amazon.com/Pelican-Protector-Heavy-Duty-Compatible-Protection/dp/B0B8KSKB2N/ref=sr_1_8?keywords=iphone+cover&qid=1663391155&sr=8-8','https://www.amazon.com/OtterBox-Commuter-Case-iPhone-Pro/dp/B08DY9HNYD/ref=sr_1_11?keywords=iphone+cover&qid=1663391155&sr=8-11']

for(url) in URL:
	# HTTP Request
	webpage = requests.get(url, headers=HEADERS)

	# Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")

	# Function calls to display all necessary product information
	print("Product Title =", get_title(soup))
	print("Product Price =", get_price(soup))
	print("Product Rating =", get_rating(soup))
	print("Number of Product Reviews =", get_review_count(soup))
	print("Availability =", get_availability(soup))
	print()
	print()