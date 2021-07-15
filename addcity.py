import os
import django
import time
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Country , City
url = "https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html"
raw_data = pd.read_html(url)
time.sleep(3)

data=raw_data[0]

cities = list()
for i in range(len(data)):
	TEM=tuple(data["cities"].iloc[i])
	cities.append(TEM)
print(cities)

for city in cities:
	#要先根據county_id的內容，去找到county表格裡面的紀錄
	#再把這個紀錄放到下面這個指令的country參數
	CT=Country.objects.get(country_id = city[2])
	temp = City(name=city[1],country = CT,population=city[3])
	temp.save()

print("done")

# c = [{"name":"天龍國" , "id" : 1001},{"name":"支那賤畜" , "id" : 1000}]


# for country in c :
# 	temp = Country(name=country["name"],country_id=country["id"])
# 	temp.save()

# print(Country.objects.all()) <= 改成City的所有紀錄顯示
# print("done")