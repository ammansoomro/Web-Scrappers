import requests
from bs4 import BeautifulSoup

def send_get_request(link):  
    # Make a request
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Create top_items as empty list
    all_links = []

    # Extract and store in top_items according to instructions on the left
    links = soup.select('a')
    for ahref in links:

        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        all_links.append({"href": href})
    a=[]
    ans=[]
    all_links
    for i in all_links:
        y=i["href"]
        a.append(y)
    for i in a:
        v=i[0:3]
        if v == "tel":
            ans.append(i)
            
    
    return ans[0:1]


# In[44]:


def send_get_name(link):
    # Make a request
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Name
    name=[]
    title=soup.find_all("div",attrs={"class":"summary-standard-header"})
    for x in title:
        name.append(x.find("div")) 
    name

    name1=[]
    for x in name:
        name1.append(x.get_text())
    name2=[]
    for x in name1:
        name2.append(x)
    name2
    kk=[]
    for j in name2:
        kk=j.split(",")
    
    kk
    return kk


import csv
ans=[]
with open("HealthGrades.txt", "r") as file:
    for i in file:
        number=send_get_request(i)
        print("Number :", number)
        print("--------------------------------\n")
        with open("record.csv",'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(number)
            

 

            


# In[ ]:





# In[ ]:




