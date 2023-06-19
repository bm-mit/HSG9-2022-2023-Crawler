from bs4 import BeautifulSoup
import requests

START_ID = 0
STOP_ID = 100000

BASE_URL = "https://diemthi.hcm.edu.vn/home/show"

if __name__ == "__main__":
    f= open("output.out", "w+")
    for i in range(START_ID, STOP_ID + 1):
        data = {
            "sobaodanh" : str(i)
        }
        result = requests.post(BASE_URL, json=data)
        if (result.status_code != 200):
            continue
        try:
            soup = BeautifulSoup(result.text)
            infomation = soup.body.table.find_all('tr')[1]
            name, dob, point = [i.contents[0].strip("\n\r ") for i in infomation.find_all('td')]
            print(i, name, dob, point, file=f, sep=" | ")
        except:
            print(f"Can't get data with id: {data['sobaodanh']}")
