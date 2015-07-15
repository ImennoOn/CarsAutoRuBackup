import urllib2
import re
import urllib
import xml.etree.ElementTree as ET

def main():
    opener = urllib2.build_opener()
    opener.addheaders = [('Host', 'cars.auto.ru'),
                         ('Connection', 'keep-alive'),
                         ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1'),
                         ('Accept', '*/*'),
                         ('Accept-Encoding', 'gzip,deflate,sdch'),
                         ('Accept-Language', 'en-US,en;q=0.8')]
    urllib2.install_opener(opener)
    mainCarsautoruPage = urllib.urlopen('http://cars.auto.ru/')

    brandListFile = open('Brand List.txt', 'w')
    brandList = getBrandsList(mainCarsautoruPage.read())
    for item in brandList:
        brandListFile.write(item+'\n')
    brandListFile.close()


def getBrandsList(htmlPage):
    allBrandsHereSearch = re.findall(r'<div class="block content auto">.+?</table>', htmlPage, re.DOTALL)
    russianBrands = allBrandsHereSearch[0]
    foreignBrands = allBrandsHereSearch[1]

    brands = "<?xml version=\"1.0\"?>\n<root>" + russianBrands + "\n</div>" + foreignBrands + "\n</div>\n</root>"
    brands = brands.replace('&nbsp','')

    brandsNormalized = ""

    for brandsPart in brands.split(" style=font-weight:bold"):
        brandsNormalized +=brandsPart

    print brandsNormalized

    brandList = []
    tree = ET.XML(brandsNormalized)
    for brandNode in tree.iter('a'):
        brandList.append(brandNode.attrib.get('href'))

    return brandList

if __name__ == '__main__':
    main()