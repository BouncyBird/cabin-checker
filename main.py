from bs4 import BeautifulSoup
import requests

url = 'https://web2.myvscloud.com/wbwsc/mnthreeriverswt.wsc/search.html?Action=Start&SubAction=&rnwebsearch_search=Yes&begindate=05%2F29%2F2021&nights=2&category=BAK&type=CAMPERCABINS&subtype=&begintime=12%3A00+am&endtime=12%3A00+am&primarycode=&keyword=&keywordoption=Match+One&sort=SecondaryCode&features=&quantity=1&secondarycode=&display=Graphical&features1=&features2=&features3=&features4=&features5=&features6=&features7=&features8=&timeblocksearch=&blockstodisplay=3&layer=4655&module=RN&multiselectlist_value=%3Cspan+class%3D%22newline%22%3E%3Cstrong%3ECabin+05%3C%2Fstrong%3E+%28BAKER+CABIN+05%29%3A+05%2F29%2F2021+%40++3%3A00+pm+-+05%2F31%2F2021+%40+11%3A00+am%3C%2Fspan%3E&rnwebsearch_buttonsearch=Search'

source = requests.get(url).text

soup = BeautifulSoup(source, "lxml")

links = soup.find_all(
    "a", class_="graphical-button multi-select",)

available = []

for link in links:
    if 'Cabin' in link.attrs['data-title'] and 'Available' in link.attrs['data-title']:
        print(link)
        available.append(link.text)

if available == []:
    print('Sorry, no cabins are available')
else:
    for i in available:
        print(f'Cabin {i} is available!')
