import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import wget
from download_geberit_product_images import download_geberit_product_images
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, ssl
import shutil
import requests
import warnings

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
	ssl._create_default_https_context = ssl._create_unverified_context
warnings.filterwarnings("ignore")


def download_geberit_product_images(geberit_productcode_list):
	#Go to Geberit page
	driver.get("https://catalog.geberit.com.tr/tr-TR/home")

	for i in geberit_productcode_list:
		
		element = driver.find_element_by_xpath("/html/body/div[2]/header/div/div[3]/form/input")
		element.send_keys(i)
		element.send_keys(Keys.ENTER)

		try:
			link_to_product = driver.find_element_by_css_selector(".mainTileImage").find_element_by_tag_name("img").get_attribute("src")
			urllib.request.urlretrieve(link_to_product,(i+".jpg"))
		except:
			print("Product not found with the code: ", i)

def download_hansgrohe_product_images(hansgrohe_productcode_list):
	#Gets to the products page
	driver.get("https://pro.hansgrohe-int.com/18558.htm")

	#Presses cookie accept button to enable access to the abovementioned web address
	cookie_accept_button = driver.find_element_by_class_name("closeLink")
	cookie_accept_button.click()

	for i in hansgrohe_productcode_list:
		#Search item
		element = driver.find_element_by_class_name("ui-autocomplete-input")
		element.send_keys(i)
		element.send_keys(Keys.ENTER)
		try:
			#Wait for the element to load
			image_url_element = WebDriverWait(driver, 15).until(
				EC.presence_of_element_located((By.CLASS_NAME,"cloud-zoom"))
				)
			#Get product image
			product_image_url = image_url_element.get_attribute("href")
			urllib.request.urlretrieve(product_image_url,(str(i)+".jpg"))
		except:
			print("Product not found with the code: ", i)

def download_kale_products(all_kale_productcode_list):
	driver.get("https://digitalkatalogws.kale.com.tr/site/Katalog.aspx")

	#Enter cridentials and login
	driver.find_element_by_id("ctl00_ContentPlaceHolder1_rdblSeriUrun_1").click()
	print("Kale ürün görselleri indirilmeye başlanıyor.")
	for i in all_kale_productcode_list:
		search_bar_element = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtUrunKodu")
		search_bar_element.clear()
		search_bar_element.send_keys(i)
		search_bar_element.send_keys(Keys.ENTER)
		time.sleep(2)
		
		try:
			product_image_element = driver.find_element_by_id("ctl00_ContentPlaceHolder1_listViewUrun_ctrl0_ctl00_imgUrun")
			product_image_url = product_image_element.get_attribute("src")
			response = requests.get(product_image_url, stream=True,verify=False)
			with open(str(i)+"jpeg", 'wb') as out_file:
			    shutil.copyfileobj(response.raw, out_file)
		except: 
			print(i, "kodlu ürün Kale Media Center'da bulunamadı)
	print("Envanterdeki kale ürün görselleri indirilmeye başarıyla tamamlandı")


data = pd.read_excel(r'./Netsis Tüm Stok Kartları Kategorili 20072020.xlsx')
df = pd.DataFrame(data, columns=["Stok Kodu", "Kategori 2"])

# SELECT KALE PRODUCTS
select_kale = df.loc[df["Kategori 2"] == "KALE"]
select_canakkale_seramik = df.loc[df["Kategori 2"] == "ÇANAKKALE SERAMİK"]
select_kalekim = df.loc[df["Kategori 2"] == "KALEKİM"]
select_kalebodur = df.loc[df["Kategori 2"] == "KALEBODUR"]
all_kale_productcode_list = select_kale["Stok Kodu"].tolist() + select_canakkale_seramik["Stok Kodu"].tolist(
) + select_kalekim["Stok Kodu"].tolist() + select_kalebodur["Stok Kodu"].tolist()

# SELECT HANSGROHE PRODUCTS
select_hansgrohe = df.loc[df["Kategori 2"] == "HANSGROHE"]
hansgrohe_productcode_list = select_hansgrohe["Stok Kodu"].tolist()
# SELECT GEBERİT PRODUCTS
select_geberit = df.loc[df["Kategori 2"] == "GEBERİT"]
geberit_productcode_list = select_geberit["Stok Kodu"].tolist()


#Opens up Google Chrome
driver_path = "/home/efeberkeevci/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

#Run all three brands' functions
download_geberit_product_images(geberit_productcode_list)
download_hansgrohe_product_images(hansgrohe_productcode_list)
download_kale_products(all_kale_productcode_list)


