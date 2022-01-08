""" bs4 scraper for jumia"""
import bs4 as bs
from urllib import request as urlr
from re import findall
# import time

# start = time.time()


def jumia(search):
    """
    user search string - jumia.com/catalog/?q={search string}
    """
    # st =["laptops","laptop"]
    # if search == "laptop":
    #     jumURL="https://www.jumia.com.ng/computers-tablets/?sort=lowest-price&rating=3-5&price=6000-1350000#catalog-listing"
    # else:
    # search = search.replace(' ', '+')
    # jumURL=["https://www.jumia.com.ng/catalog/?q={}&sort=rating&shipped_from=country_local#catalog-listing".format(search),
    #         "https://www.jumia.com.ng/catalog/?q={}&sort=rating&page=2&shipped_from=country_local#catalog-listing".format(search),
    #         "https://www.jumia.com.ng/catalog/?q={}&sort=rating&page=3&shipped_from=country_local#catalog-listing".format(search)
    #         # "https://www.jumia.com.ng/catalog/?q={}&sort=lowest-price&shipped_from=country_local#catalog-listing".format(search)]
    jumURL=[f"https://www.jumia.com.ng/catalog/?q={search}&sort=rating&shipped_from=country_local#catalog-listing",
            f"https://www.jumia.com.ng/catalog/?q={search}&sort=rating&page=2&shipped_from=country_local#catalog-listing",
            f"https://www.jumia.com.ng/catalog/?q={search}&sort=rating&page=3&shipped_from=country_local#catalog-listing"
            ]
    products = []
    
    for i in jumURL:
        site = urlr.Request(i, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64),"Accept-Encoding":"gzip'})
        source = urlr.urlopen(site,timeout=20).read()
        soup = bs.BeautifulSoup(source,'lxml')
        body = soup.body
    
    ## this function will return a dictionary with product-name, product-link, price and product-image
        prdlist = body.find_all(class_="prd _fb col c-prd")
        for j in range(len(prdlist)):
        
            plink = prdlist[j].find(class_="core", href=True)

            link = plink.get("href")
            # TODO find change price to int before sort cause of issue with numbers written in 10's 
            price = plink.find(class_="prc").find(text=True)
            
            img = plink.find("img",class_="img")["data-src"]
            pname = plink.get("data-name")
            
            products.append({"name":pname,"link":link,"price":price,"image":img})
            p = sorted(products, key=lambda i: i["price"],reverse=False)

    return products


laptops = jumia("laptop")
# end = time.time()
print(laptops[1])


# print("The time of execution of above program is :", end-start)
# for u in laptops:
#     for k,v in u.items():
#         print(findall("rice",v.lower()))
            # laptops.remove()
# for i in range(len(laptops)):
#     print(laptops[i]["image"])
#     print(laptops[i]["price"])
# for p in laptops:
#     for prd in p.values():
#         # print(label)
#         print(prd)

# print(laptops.image)


