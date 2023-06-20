from bs4 import BeautifulSoup
import requests
from logger import Logger
from plot_generator import PlotGenerator
from contestant import Contestant
from points import Points

START_ID = 0
STOP_ID = 100000

BASE_URL = "https://diemthi.hcm.edu.vn/home/show"

PLOT = PlotGenerator()

def crawl(start, stop, isspec=False):
    for i in range(start, stop + 1):
        data = {
            "sobaodanh": str(i)
        }

        result = requests.post(BASE_URL, json=data)
        if (result.status_code != 200):
            continue
        
        Logger.log_message(f"Crawling: id = {i}")
        soup = BeautifulSoup(result.text)
        try:
            information = soup.body.find("div", class_="container").table.find_all("tr")[1]
            
            table_row = information.find_all("td")
            full_name = table_row[0].text.split("_")[-1].strip("\r\n ").title()
            point_information = table_row[1].text.strip("\r\n ").split(" ")


            points = []
            for point in point_information:
                try:
                    points.append(float(point.replace(",", ".")))
                except ValueError:
                    continue
                    
            while (len(points) < 4):
                points.append(0.0)
            contestant = Contestant(i, full_name, Points(points[0], points[1], points[2], points[3], isspec))
            PLOT.add_contestant(contestant)
            
            
        except AttributeError as error:
            Logger.log_error(error.name)
            Logger.log_message(f"Can't get data with id: {data['sobaodanh']}")
            Logger.log_message("Terminate this batch. Move to next batch or exit if don't have any batch left.")
            return

if __name__ == "__main__":
    crawl(9000, 9999)
    crawl(90000, 99999)
    crawl(100000, 199999)
