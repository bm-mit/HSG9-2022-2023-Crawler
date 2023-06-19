from bs4 import BeautifulSoup
import requests
from logger import Logger

START_ID = 0
STOP_ID = 100000

BASE_URL = "https://diemthi.hcm.edu.vn/home/show"

def crawl(start, stop):
    for i in range(start, stop + 1):
        data = {
            "sobaodanh": str(i)
        }

        result = requests.post(BASE_URL, json=data)
        if (result.status_code != 200):
            continue

        try:
            soup = BeautifulSoup(result.text)
            infomation = soup.body.table.find_all('tr')[1]
            name, dob, point = [i.contents[0].strip(
                "\n\r ") for i in infomation.find_all('td')]
            
        except AttributeError:
            Logger.log_message(f"Can't get data with id: {data['sobaodanh']}")
            Logger.log_message("Terminate this batch. Move to next batch or exit if don't have any batch left.")

if __name__ == "__main__":
    crawl(9000, 9999)
    crawl(90000, 99999)
    crawl(100000, 199999)