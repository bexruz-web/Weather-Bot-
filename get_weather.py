import requests
from bs4 import BeautifulSoup as BS
from config import URl

def get_all_regions():

    response = requests.get(URl)
    soup = BS(response.content, 'html.parser')

    regions = []
    regions_elements = soup.find('ul', class_="list-c").find_all('a')

    for region in regions_elements:
        region_name = region.get_text(strip=True)
        region_link = region['href']
        regions.append(
            {
                region_name: region_link
            }
        )
    return regions
# print(get_all_regions())

def get_weather_data(region_url):
    response = requests.get(region_url)
    soup = BS(response.content, 'html.parser')

    region_name = soup.find('h2').get_text(strip=True)

    current_day = soup.find('div', class_="current-day").get_text(strip=True)
    current_forecast_desc = soup.find('div', class_="current-forecast-desc").get_text(strip=True)

    current_forecast = soup.find('div', class_="current-forecast")
    high_temp = current_forecast.find_all('span')[1].get_text(strip=True)
    low_temp = current_forecast.find_all('span')[2].get_text(strip=True)
    img = current_forecast.find('img')['src']

    details_block = soup.find('div', class_="current-forecast-details")
    sunrise = details_block.find_all('p')[4].get_text(strip=True).replace('Quyosh chiqishi: ', '')
    sunset = details_block.find_all('p')[5].get_text(strip=True).replace('Quyosh botishi: ', '')

    forecast_day = soup.find('div', class_="current-forecast-day")
    morning = forecast_day.find('div', class_="col-1").find('p', class_="forecast").get_text(strip=True)
    during_day = forecast_day.find('div', class_="col-2").find('p', class_="forecast").get_text(strip=True)
    evening = forecast_day.find('div', class_="col-3").find('p', class_="forecast").get_text(strip=True)

    weather_data = {
        'region_name': region_name,
        'current_day': current_day,
        'current_forecast_desc': current_forecast_desc,
        'high_temp': high_temp,
        'low_temp': low_temp,
        'img': img,
        'sunrise': sunrise,
        'sunset': sunset,
        'morning': morning,
        'during_day': during_day,
        'evening': evening,
    }
    return weather_data
# print(get_weather_data("https://obhavo.uz/samarkand"))

def get_three_weather_data(region_url):
    response = requests.get(region_url)
    soup = BS(response.content, 'html.parser')

    three_weather_table = soup.find('table', class_="weather-table")

    three_weather = []
    for row in three_weather_table.find_all('tr')[1:]:
        day = row.find('td', class_='weather-row-day').get_text(strip=True)
        week_day = row.find('td', class_='weather-row-day').find('strong').get_text(strip=True)
        month_day = row.find('td', class_='weather-row-day').find('div').get_text(strip=True)
        icon_url = row.find('td', class_='weather-row-forecast-icon').find('img')['src']
        forecast_day = row.find('span', class_='forecast-day').get_text(strip=True)
        forecast_night = row.find('span', class_='forecast-night').get_text(strip=True)
        description = row.find('td', class_='weather-row-desc').get_text(strip=True)
        precipitation = row.find('td', class_='weather-row-pop').get_text(strip=True)

        day_weather = {
            'month_day': month_day,
            'week_day': week_day,
            'icon_url': icon_url,
            'forecast_day': forecast_day,
            'forecast_night': forecast_night,
            'description': description,
            'precipitation': precipitation
        }

        three_weather.append(day_weather)

    return three_weather



# print(get_weekly_weather_data("https://obhavo.uz/tashkent"))

