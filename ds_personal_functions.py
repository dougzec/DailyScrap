# def amazon(urls, driver):
    
#     print("# Amazon products prices #")
    
#     for url in urls:
        
#         try:

#             driver.get(url)

#             # Price
#             try:
#                 xpath_price = '//*[@id="a-autoid-7-announce"]/span[2]/span'
#                 price = driver.find_element_by_xpath(xpath_price).text
#             except:
#                 try:
#                     xpath_price = '//*[@id="soldByThirdParty"]/span'
#                     price = driver.find_element_by_xpath(xpath_price).text
#                 except:
#                     xpath_price = '//*[@id="price_inside_buybox"]'
#                     price = driver.find_element_by_xpath(xpath_price).text

#             # Name
#             xpath_name = '//*[@id="productTitle"]'
#             name = driver.find_element_by_xpath(xpath_name).text

#             print(name + ": " + price)
#         except:
#             print('Either the poduct was not found or this webscrap is not good enough...')
        
#     print("\n")