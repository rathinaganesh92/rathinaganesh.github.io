from bs4 import BeautifulSoup as BS
from IPython.core.display import HTML
HTML("<b>Rendered HTML</b>")
import requests as req
  
url = "https://www.businesstoday.in/latest/economy"
  
webpage = req.get(url)
trav = BS(webpage.content, "html.parser")
M = 1
for link in trav.find_all('a'):
    
    # PASTE THE CLASS TYPE THAT WE GET
    # FROM THE ABOVE CODE IN THIS AND
    # SET THE LIMIT GRATER THAN 35
    if(str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
       and len(link.string) > 35):
  
        print(str(M)+".", link.string)
        M += 1

page_response = req.get("https://www.moneycontrol.com/india/stockpricequote/auto-23-wheelers/heromotocorp/HHM", timeout=240)
page_content = BS(page_response.content, "html.parser")
HTML(str(page_content.find("h1")))

HTML(str(page_content.find("div",attrs={'id':"content_full"})))