from selenium.common.exceptions import NoSuchElementException

__author__ = 'MiRo'
from selenium import webdriver
import codecs
import xml.etree.ElementTree as ET

def main():
    brandList = ('mercedes','nissan')
    for brand in brandList:
        outputFile = codecs.open('_'+brand,'w', 'utf-8-sig')

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
                pageNumber +=1
            except NoSuchElementException:
                has_next_page = False
                print 'No next pages'

            number_of_cars = len(driver.find_elements_by_xpath('//*[@id="cars_sale"]/table/tbody/tr'))
            for iter in range(2,number_of_cars+1):
                car_model = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[1]/a')
                car_name = car_model.text
                if len(car_name) < 20:
                    car_href = car_model.get_attribute('href')
                    car_price = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[2]/nobr').text
                    car_year = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[3]').text
                    car_motor = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[4]').text
                    car_motor_type = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[5]/div').text
                    car_mileage = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[6]/nobr').text
                    car_condition = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[8]/img').get_attribute('title')
                    car_color = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[9]/div').get_attribute('style').split(');')[0].split('rgb(')[1]
                    car_sity = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[10]').text
    #                car_customs = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[11]/').get_attribute('title')
                    car_inplace = driver.find_element_by_xpath('//*[@id="cars_sale"]/table/tbody/tr['+str(iter)+']/td[12]').text
    #                print '\n\nName ', car_name, '\nHref: ', car_href, '\nPrice: ', car_price, '\nYear: ', car_year
    #                print 'Motor: ', car_motor, '\nMotor type: ', car_motor_type, '\nMileage: ', car_mileage, '\nCondition: ', car_condition
    #                print 'Color: ', car_color, '\nSity: ', car_sity, '\nCustoms: ', car_customs, '\nInplace: ', car_inplace
                    outputFile.write(car_name + ';'+car_price+';'+car_year+';'+car_motor+';'+car_motor_type+';'+car_mileage+';'+car_condition+';'+car_color+';'+car_sity+';'+car_inplace+';'+car_href+'\n')

        outputFile.close()
        driver.close()
    driver.quit()

def cars_on_page(driver):
    return 0

if __name__ == '__main__':
    main()