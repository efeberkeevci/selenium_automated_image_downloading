def download_geberit_product_images(geberit_productcode_list,driver):
	#Go to Geberit page
	driver.get("https://catalog.geberit.com.tr/tr-TR/home")

	for i in geberit_productcode_list:
		
		driver.get("https://catalog.geberit.com.tr/tr-TR/home")
		element = driver.find_element_by_xpath("/html/body/div[2]/header/div/div[3]/form/input")
		element.send_keys(i)
		element.send_keys(Keys.ENTER)

		if driver.find_element_by_css_selector(".mainTileImage"):
			link_to_product = driver.find_element_by_css_selector(".mainTileImage").find_element_by_tag_name("img").get_attribute("src")
			urllib.request.urlretrieve(link_to_product,(i+".jpg"))
		else:
			print("Product not found with the code: ", i)
