from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import urllib.request

product_types_and_product_links_dictionary = {}
driver_path = "/home/efeberkeevci/Desktop/aytas_yapi/aytas_yapi_website/node_modules/chromedriver/lib/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

download_product("https://digitalkatalogws.kale.com.tr/site/KatalogDetay.aspx?UrunID=7155&TB_iframe=true&height=500&width=800")

def download_product(product_url):
	driver.get(product_url)

	#Get product name
	product_name = driver.find_elements_by_tag_name("tr").find_element_by_tag_name("td").find_elements_by_tag_name("span").get(0).get_attribute("innerHTML")
	#Get product code
	product_code = driver.find_element_by_id("listViewUrunler_ctrl0_ctl00_lblUrunAdi").get_attribute("innerHTML")
	#Get product image
	product_image_url = driver.find_element_by_id("listViewUrunler_ctrl0_ctl00_linkJPG")
	urllib.request.urlretrieve(product_image_url,(product_name+"_image.jpg"))