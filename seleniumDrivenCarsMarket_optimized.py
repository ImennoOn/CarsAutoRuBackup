from selenium.common.exceptions import NoSuchElementException

__author__ = 'MiRo'
from selenium import webdriver
import codecs
import xml.etree.ElementTree as ET

def main():
    brandList = ('mercedes','nissan')
    for brand in brandList:
        outputFile = codecs.open('__'+brand,'w', 'utf-8-sig')

        brandURL = '/cars/used/'+brand+'/'
        region = '&region_id=87'
        pagePrefix = '&_p='
        pageNumber = 1
        has_next_page = True
        searchURLPrefix = '/all/?currency_key=RUR&price_usd%5B1%5D=&price_usd%5B2%5D=&year%5B1%5D=0&year%5B2%5D=0&client_id=0&body_key=' + region + '&stime=0&available_key=1'
        driver = webdriver.Chrome()

        while has_next_page != False:
            driver.get('http://cars.auto.ru' + brandURL.rstrip('\n') + searchURLPrefix + pagePrefix + str(pageNumber))
            try:
                has_next_page = True if (len(driver.find_element_by_xpath('//*[@id="cars_sale"]/div[1]/div/div/div[1]/a/span').text)>5) else False
            except NoSuchElementException:
                has_next_page = False
                print 'No next pages'

            number_of_cars = len(driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr'))
            afterAdv = 0

            car_model = driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr/td[1]/a')
            car_price = driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr/td[2]/nobr')
            car_year = driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr/td[3]')
            car_motor = driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr/td[4]')
            car_motor_type = driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr/td[5]/div')
            car_mileage = driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr/td[6]/nobr')
            car_condition = driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr/td[8]/img')
            car_color = driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr/td[9]/div')
            car_city = driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr/td[10]')
            car_inplace = driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr/td[12]')
            for i in range(0,number_of_cars-1):
                name = car_model[i].text
                if len(name)>20:
                    afterAdv = -1
                    print 'adv'
                else:
                    price = car_price[i+afterAdv].text
                    year = car_year[i+1+afterAdv].text
                    motor = car_motor[i+1+afterAdv].text
                    motor_type = car_motor_type[i+afterAdv].text
                    mileage = car_mileage[i+afterAdv].text
                    condition = car_condition[i+afterAdv].get_attribute('title')
                    color = car_color[i+afterAdv].get_attribute('style').split(');')[0].split('rgb(')[1]
                    city =  car_city[i+1+afterAdv].text
                    inplace = car_inplace[i+1+afterAdv].text
                    href = car_model[i].get_attribute('href')
                    outputFile.write(name + ';'+price+';'+year+';'+motor+';'+motor_type+';'+mileage+';'+condition+';'+color+';'+city+';'+inplace+';'+href+'\n')

            if has_next_page == True:
                pageNumber +=1

        outputFile.close()
        driver.close()
    driver.quit()

def cars_on_page(driver):
    return 0

if __name__ == '__main__':
    main()