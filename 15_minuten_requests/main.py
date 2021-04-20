from requests_html import HTMLSession


## URLS
# Requests https://2.python-requests.org/en/master/user/quickstart/#redirection-and-history
# Requests html https://requests-html.kennethreitz.org/

headers = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'}

session = HTMLSession()

kleinanzeigen_url = "https://www.ebay-kleinanzeigen.de"
url = "https://www.ebay-kleinanzeigen.de/s-suchanfrage.html?keywords=honda+nc+700"#&categoryId=&locationStr=91074 Herzogenaurach&locationId=6203&radius=0&sortingField=SORTING_DATE&adType=&posterType=&pageNum=1&action=find&maxPrice=&minPrice="

er = session.get(url, headers=headers)
artikel = er.html.find('article')

def get_items_of_link(artikel):
    data = []
    for a in artikel:
        link = kleinanzeigen_url + a.attrs['data-href']
        prize = a.find(".aditem-main--middle--price") # find nicht vom html objekt dann klappt es auch
        description = a.find(".aditem-main--middle--description")
        data.append({'link':link, 'prize':prize[0].text, 'description':description[0].text})
    return data

print(get_items_of_link(artikel)[0])

### links der folgenden Seiten abrufen noch ein Todo
for a in er.html:
    print(a)
