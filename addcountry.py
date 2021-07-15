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

data=raw_data[1]

country_id = list(data["countries"]["id"])
country_name = list(data["countries"]["name"])
countries = zip(country_id,country_name)
for c in countries:
	TEM=Country(name=c[1],country_id=c[0])
	TEM.save()
	print(c)



# c = [{"name":"天龍國" , "id" : 1001},{"name":"支那賤畜" , "id" : 1000}]


# for country in c :
# 	temp = Country(name=country["name"],country_id=country["id"])
# 	temp.save()

# print(Country.objects.all())
# print("done")