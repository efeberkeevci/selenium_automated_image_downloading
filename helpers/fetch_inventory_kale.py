from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import urllib.request
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
	ssl._create_default_https_context = ssl._create_unverified_context

def download_product(product_url):
	driver.get(product_url)
	#Get product name
	product_name = driver.find_elements_by_tag_name("tr")[0].find_element_by_tag_name("td").find_elements_by_tag_name("span")[0].get_attribute("innerHTML").strip()
	#Get product code
	product_code = driver.find_element_by_id("listViewUrunler_ctrl0_ctl00_lblUrunAdi").get_attribute("innerHTML")
	#Get product image
	product_image_url = driver.find_element_by_id("listViewUrunler_ctrl0_ctl00_linkJPG").get_attribute("href")
	print(product_image_url)
	handler = urllib.request.urlretrieve(product_image_url,(product_name+"_image.jpg"))

product_types_and_product_links_dictionary = {}
driver_path = "/home/efeberkeevci/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
#driver.get("https://pro.hansgrohe-int.com/")
#products_navbar = driver.find_element_by_xpath('//a[text() = "Products by category"]').getAttribute("href")
#products_navbar.click()
driver.get("https://digitalkatalogws.kale.com.tr/site/Katalog.aspx")

#Enter cridentials and login
driver.find_element_by_id("btnGiris").click()

#Choose Products by Product Type

#select show products only button
show_products_only_radio_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"ctl00_ContentPlaceHolder1_rdblSeriUrun_1")))
show_products_only_radio_button.click()

#select product type one by one
product_types_element = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlUrunTipi").find_elements_by_tag_name("option")

for product_type_index in range(46):
	product_types_select_element = Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlUrunTipi"))
	if product_type_index==0:
		continue
	product_types_select_element.select_by_index(product_type_index)
	product_types_and_product_links_dictionary[product_type_index] = []
	driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnAra").click()
	items = driver.find_elements_by_class_name("serieItemTemplate")
	for item in items:
		product_url = item.find_element_by_tag_name("a").get_attribute("href")
		product_types_and_product_links_dictionary[product_type_index].append(product_url)
		download_product(product_url)

#Download and save all products on KALE Digital Katalog
for product_type in product_types_and_product_links_dictionary.keys():
	for product in product_type:
		download_product(product)



