import osimport reimport requestsfrom bs4 import BeautifulSoupfrom requests import getdef parse_car(name: str):    response = get(f"https://www.olx.uz/oz/list/q-{name}/?search%5Border%5D=created_at:desc")    soup = BeautifulSoup(response.text, 'html.parser')    element = soup.find_all('div', class_='css-l9drzq')    result_dict, res, num = [], [], 1    for i in element[:8]:        res_link = i.find('a', class_='css-qo0cxu')        res.append(res_link['href'])    # image    # swiper_wrapper = soup.find('div', class_='swiper-wrapper')    #    # images = swiper_wrapper.find_all('img')    #    # os.makedirs('images', exist_ok=True)    # for img in images:    #     img_url = img.get('src')    #     if img_url:    #         if img_url.startswith('//'):    #             img_url = 'https:' + img_url    #    #         img_name = f'{img_url.split("/")[-2]}.jpg'    #         img_path = os.path.join('images', img_name)    #    #         img_data = requests.get(img_url).content    #         with open(img_path, 'wb') as f:    #             f.write(img_data)    for i in res:            link = f"https://www.olx.uz{i}"            soup1 = BeautifulSoup(get(link).text, 'html.parser')            try:                price_car = soup1.find('h3', class_='css-90xrc0').text  # css-1povu0j            except AttributeError:                price_car = 'Narxi mavjud emas!'            div_element_ul = soup1.find('ul', class_='css-rn93um')            re_text = re.search(r"Model:\s*(.*?)Kuzov", div_element_ul.text)            if re_text:                model = re_text.group(1)            else:                model = "Model nomi ko'rsatilmagan!"            re_text_year = re.search(r"Ishlab chiqarilgan yili:\s*(.*?) Bosgan", div_element_ul.text)            if re_text_year:                year = re_text_year.group(1)            else:                year = "Yili berilmagan!"            re_text_km = re.search(r"Bosgan yo‘li: \s*(.*?)Uzatmalar", div_element_ul.text)            if re_text_km:                km = re_text_km.group(1)            else:                km = "Bosib o'tilgan yo'l berilmagan!"            re_text_karobka = re.search(r"Uzatmalar qutisi: \s*(.*?)Rang", div_element_ul.text)            if re_text_karobka:                karobka = re_text_karobka.group(1)            else:                karobka = "Uzatma berilmagan!"            re_text_color = re.search(r"Rang: \s*(.*?)Dvigatel", div_element_ul.text)            if re_text_color:                color = re_text_color.group(1)            else:                color = "Uzatma berilmagan!"            re_text_fuel = re.search(r"Yoqilg‘i turi: \s*(.*?)Mashina", div_element_ul.text)            if re_text_fuel:                fuel = re_text_fuel.group(1)            else:                fuel = "Yoqilg'i turi berilmagan!"            re_text_status = re.search(r"Mashina holati: \s*(.*?)Mulkdorlar", div_element_ul.text)            if re_text_status:                status_car = re_text_status.group(1)            else:                status_car = "Holati berilmagan!"            car_info = {                'model': model,                'Created_at': soup1.find('span', class_='css-19yf5ek').text,                'price': price_car,                'year': year,                'km': km,                'karobka': karobka,                'color': color,                'fuel': fuel,                'status_car': status_car,                'link': i,            }            result_dict.append(car_info)    return result_dict