from selenium import webdriver
import urllib.request

links_to_products = []
#Opens up Google Chrome
driver_path = "/home/efeberkeevci/Desktop/aytas_yapi/aytas_yapi_website/node_modules/chromedriver/lib/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

#Gets to the products page
driver.get("https://pro.hansgrohe-int.com/18558.htm")

#Presses cookie accept button to enable access to the abovementioned web address
cookie_accept_button = driver.find_element_by_class_name("closeLink")
cookie_accept_button.click()


pagenum = 1

#Loops through all 123 item result pages and then loops through every item in a page
while True:
	page_link = "https://pro.hansgrohe-int.com/getArticleOverview.html?p="+str(pagenum)
	driver.get(page_link)
	products = driver.find_element_by_class_name("clearfix").find_elements_by_tag_name("li")
	if len(products) == 0:
		break
	for product in products:
                #Saves links to product pages
		link_to_product = product.find_element_by_tag_name("a").get_attribute("href")
		links_to_products.append(link_to_product)
	pagenum+=1
	
#TODO:Need to put into folder structure in parallel with database structure

#Visits every product page, saves product image and product datasheet. Filename includes product name
for product_page_link in links_to_products:
        #Go to product page
	driver.get(product_page_link)
	#Get product name
	product_name= driver.find_element_by_class_name("productInformation").find_element_by_tag_name("h2").get_attribute("innerHTML")

	#Get product image
	product_image_url = driver.find_element_by_class_name("cloud-zoom").get_attribute("href")
	urllib.request.urlretrieve(product_image_url,(product_name+"_image.jpg"))
	#Get product datasheet

	product_datasheet_url =	product_image_url = driver.find_element_by_class_name("w2Download").get_attribute("href")
	urllib.request.urlretrieve(product_datasheet_url,(product_name+"_datasheet.pdf"))
