from requests_html import HTMLSession
import argparse

## URLS
# Requests https://2.python-requests.org/en/master/user/quickstart/#redirection-and-history
# Requests html https://requests-html.kennethreitz.org/

# Todo
# - pagination der ersten Seite folgen und abrufen

kleinanzeigen_url = "https://www.ebay-kleinanzeigen.de"

def get_items_of_link(artikel):
    data = []
    for a in artikel:
        link = kleinanzeigen_url + a.attrs['data-href']
        prize = a.find(".aditem-main--middle--price") # find nicht vom html objekt dann klappt es auch
        description = a.find(".aditem-main--middle--description")
        #print(prize)
        try:
            data.append({'link':link, 'prize':prize[0].text, 'description':description[0].text})
        except IndexError:
            next
    return data

def get_pagination(seite):
    data = []
    pagination = seite.html.find(".pagination-pages")
    links_p = pagination[0].find("a")
    for link in links_p:
        yield f'{kleinanzeigen_url}{link.attrs["href"]}'
    #return ret

def recursive_through_sites(pag, url, headers, session):    
    er = session.get(url, headers=headers)
    #print(er.text)
    artikel = er.html.find('article')
    #pag = get_pagination(er)
    for a in get_items_of_link(artikel):
        print(f"{a['link']} | {a['prize']}")
    for seite in pag:
        print(seite)
        recursive_through_sites(pag, seite, headers, session)
        #print(get_pagination(er))
        #er = session.get(get_pagination(er), headers=headers)
        #artikel = er.html.find('article')
        #for a in get_items_of_link(artikel):
        #    print(f"{a['link']} | {a['prize']}")

parser = argparse.ArgumentParser(description='schnell Abfrage der kleinanzeigen auf kommando Ebene')
parser.add_argument('such',action='extend', nargs="+", type=str, help='suchstringeingeben')
args = parser.parse_args()
if args.such:
    #print("also hier sind wir")
    #print(args.such)
    search_string = ("+").join(args.such[1:])

print(f'Suche mit dem Serch String: {search_string}')

if search_string:
    headers = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'}
    session = HTMLSession()
    url = f"https://www.ebay-kleinanzeigen.de/s-suchanfrage.html?keywords={search_string}"#&categoryId=&locationStr=91074 Herzogenaurach&locationId=6203&radius=0&sortingField=SORTING_DATE&adType=&posterType=&pageNum=1&action=find&maxPrice=&minPrice="
    print(url)
    er = session.get(url, headers=headers)
    #print(er.text)
    ## Das gewurstel verbessern
    artikel = er.html.find('article')
    pag = get_pagination(er)
    recursive_through_sites(pag,url,headers, session)
