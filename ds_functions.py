def amazon(driver, urls):
    
    print("# Amazon products prices #")
    
    for url in urls:
        
        try:

            driver.get(url)

            # Price
            try:
                xpath_price = '//*[@id="a-autoid-7-announce"]/span[2]/span'
                price = driver.find_element_by_xpath(xpath_price).text
            except:
                try:
                    xpath_price = '//*[@id="soldByThirdParty"]/span'
                    price = driver.find_element_by_xpath(xpath_price).text
                except:
                    xpath_price = '//*[@id="price_inside_buybox"]'
                    price = driver.find_element_by_xpath(xpath_price).text

            # Name
            xpath_name = '//*[@id="productTitle"]'
            name = driver.find_element_by_xpath(xpath_name).text

            print(name + ": " + price)
        except:
            print('Either the poduct was not found or this webscrap is not good enough...')
        
    print("\n")
    
def investing_currency(driver, currencies):
    
    print("# Investing.com - Currencies to BRL #")
    
    if currencies != None:
        for currency in currencies:
            
            driver.get('https://br.investing.com/currencies/{}-brl'.format(currency))
            
            tries = 0
            stop = False
            while (stop == False) and (tries < 10):
                try:
                    currency_value = driver.find_element_by_xpath('//*[@id="last_last"]').text
                    delta = driver.find_element_by_xpath('//*[@id="quotes_summary_current_data"]/div[1]/div[2]/div[1]/span[4]').text
                    print('{}: {} {}'.format(currency, currency_value, delta))
                    stop = True
                    tries += 1
                except:
                    tries += 1
    
    print("\n")
    
def investing_stocks(driver, stocks):
    
    print("# Investing.com - Stocks #")
    
    for stock in stocks:
        


        driver.get('https://br.investing.com/search/?q={}'.format(stock))
        driver.find_element_by_xpath('//*[@id="fullColumn"]/div/div[2]/div[2]/div[1]/a').click()

        tries = 0
        stop = False
        while (stop == False) and (tries < 10):
            try:
                stock_value = driver.find_element_by_xpath('//*[@id="last_last"]').text
                delta = driver.find_element_by_xpath('/html/body/div[5]/section/div[4]/div[1]/div[1]/div[2]/div[1]/span[4]').text
                                                      
                print('{}: {} {}'.format(stock, stock_value, delta))
                stop = True
                tries += 1
            except:
                tries += 1
        
    print("\n")
    
def climatempo(driver,cidades):
    
    cidades_dict = {'Porto Alegre': '363/portoalegre-rs',
                     'Nova Prata': '4457/novaprata-rs', 
                     'Berlin': '7246/berlim-al'}
    
    
    print("# Climatempo #")
    
    for cidade in cidades:
        if cidade in cidades_dict:
            cidade_code = cidades_dict[cidade]
            
            driver.get('https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/{}'.format(cidade_code))

            t_max = driver.find_element_by_xpath('//*[@id="wrapperForecastCard1"]/div[2]/div[1]/div[1]/div[1]/p[2]/span[2]').text
            t_min = driver.find_element_by_xpath('//*[@id="wrapperForecastCard1"]/div[2]/div[1]/div[1]/div[1]/p[1]/span[2]').text
            dados = driver.find_element_by_xpath('//*[@id="wrapperForecastCard1"]/div[2]/div[1]/div[1]/div[2]').text
            dados = dados.split('\n')
            
            
#             driver.find_element_by_xpath('//*[@id="wrapperHourlyForecast"]').screenshot('teste.png')
            print('- {} -'.format(cidade))
    
        
            if cidade != 'Berlin':
                to_print = 'Temp:{}~{}'.format(t_max, t_min) + ' * ' + 'Chuva:{}'.format(dados[8].split(' ')[1]) + ' * ' + 'Umid:{}'.format(dados[6] + '-'+dados[10])
            else:
                to_print = 'Temp:{}~{}'.format(t_max, t_min) + ' * ' + 'Chuva:{}'.format(dados[6].split(' ')[1]) + ' * ' + 'Umid:{}'.format(dados[5] + '-'+dados[8])
        print(to_print)
    print("\n")
