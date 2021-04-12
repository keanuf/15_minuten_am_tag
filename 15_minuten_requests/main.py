from requests_html import HTMLSession


## URLS
# Requests https://2.python-requests.org/en/master/user/quickstart/#redirection-and-history
# Requests html https://requests-html.kennethreitz.org/

headers = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'}

session = HTMLSession()

url = "https://www.ebay-kleinanzeigen.de/s-suchanfrage.html?keywords=honda+nc+700"#&categoryId=&locationStr=91074 Herzogenaurach&locationId=6203&radius=0&sortingField=SORTING_DATE&adType=&posterType=&pageNum=1&action=find&maxPrice=&minPrice="

er = session.get(url, headers=headers)
artikel = er.html.find('article')
for a in artikel:
    print(a.attrs['data-href'])
    print(a.html)
    ## nach css class noch nix gefunden mal schauen ob ich es schaffe ;)
    prize = a.html.find('.aditem-main--middle--price')
    print(prize)