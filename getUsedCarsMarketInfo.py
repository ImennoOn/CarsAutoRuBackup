__author__ = 'MiRo'
import re
import urllib
import urllib2
import os
import cookielib
import xml.etree.ElementTree as ET
import BeautifulSoup
import spidermonkey

def main():
    brandListFile = open('Brand List.txt', 'r')

    region = "&region_id=87"
    startPage = "&_p=1"
    searchURLPrefix = "/all/?currency_key=RUR&price_usd%5B1%5D=&price_usd%5B2%5D=&year%5B1%5D=0&year%5B2%5D=0&client_id=0&body_key=" + region + "&stime=0&available_key=1" + startPage

    file = brandListFile.readline()
    print file

    jar = cookielib.FileCookieJar("cookies")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))


    for brandURL in brandListFile.readlines():
        brandPage = opener.open('http://cars.auto.ru' + brandURL.rstrip('\n') + searchURLPrefix)
        brandPageRaw = brandPage.read()
        soup = BeautifulSoup.BeautifulSOAP(brandPageRaw)
        print soup
        resultsTable = re.findall('class="list">.+?</tbody>', brandPageRaw, re.DOTALL)
        if resultsTable.count() > 0:
            parseTable(resultsTable[14:])
        else:
            break
#    for item in brandList:
#        brandListFile.write(item+'\n')
#    brandListFile.close()

def parseTable(htmlTable):
    tree = ET.XML(htmlTable)

if __name__ == '__main__':
    main()