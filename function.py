import requests
from bs4 import BeautifulSoup


class CalculateCalorie:
    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self, tempreture):
        result = (10 * self.weight) + (6.25 * self.height) - (5 * tempreture) + 5
        return result


class FindTemp:
    def get_temprature(self, country, city):
        url = f"https://www.timeanddate.com/weather/{country}/{city}"
        responce = requests.get(url)
        content = responce.text
        soup = BeautifulSoup(content, 'html.parser')
        temperature = soup.find('div', class_='h2').text
        new = temperature.replace("°C", "").strip()

        return float(new)

#
# weight = float(input("enter your weight:"))
# height = float(input("enter your height:"))
# age = int(input("enter your age:"))
# country = input("enter country name:")
# city = input("enter city name")
#
temp = FindTemp()
# tempreture = temp.get_temprature(country=country, city=city)
# calculatecalorie = CalculateCalorie(weight=weight, height=height, age=age)
#
# print(calculatecalorie.calculate(tempreture))
