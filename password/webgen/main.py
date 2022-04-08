from bs4 import BeautifulSoup 
import requests
import re
import lxml
def new_egg(search_term):
    search_term = search_term.replace(" ","")
    new_egg_url = f"https://www.newegg.com/p/pl?d={search_term}"
    new_egg_items = {}
    new_egg_page = requests.get(new_egg_url).text
    soup = BeautifulSoup(new_egg_page, "html.parser")
    #finding the items 
    div = soup.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    #finds all items that are similar to the div variable 
    item = div.find_all(text=re.compile(search_term))
    #looking for parent tag
    for items in item:
        parent = items.parent
        #setting link to none incase there is not a link
        link = None
        #if there is not a link just continue running the program
        if parent.name != "a":
            continue
        #link tag
        link = parent['href']
        #this finds the individual item container
        new_parent = items.find_parent(class_='item-container')
        #this finds the price within the container
        try:
            price = new_parent.find(class_="price-current").find("strong").string
            #adds this to a dictionary
            new_egg_items[items] = {"price": int(price.replace(",","")), "link": link}
        except:
            pass
   #do later: take the items we found and sort them from lowest to highest, print out in a cleaner format that is readable
    sorted_items = sorted(new_egg_items.items(), key=lambda x: x[1]['price'])[:1]
    #new_list = list(sorted_items)

    for item in sorted_items:
        print("NEW EGG ")
        print("-------------")
        print(item[0])
        print(f"${item[1]['price']}")
        print(item[1]['link'])
        print("-------------")


def microcenter(search_term):
    
    url = f"https://www.microcenter.com/search/search_results.aspx?Ntt={search_term}&Ntx=mode+MatchPartial&Ntk=all&sortby=match&N=0&myStore=false"
    micro_center_page = requests.get(url).text
    soup = BeautifulSoup(micro_center_page, "html.parser")
    div = soup.find(class_="details")
    item = div.find_all(text=re.compile(search_term))
    
    for items in item:
        price_tag= div.find(itemprop="price").text

        print("MICROCENTER")
        print("-------------")
        print()
        print(items)
        print(price_tag)

def main():
    search_term = input("enter the item you are looking for: ")
    new_egg(search_term)
    microcenter(search_term)
    

if __name__ == '__main__':
    main()
