import csv
import threading
import requests
from logger import Logger

BASE_URL = "https://s6.tuoitre.vn/api/diem-thi-lop-10.htm"
HEADERS = {"Origin": "https://tuoitre.vn"}

THREAD_TASKS = [
    [[9001, 9999, 'result1.csv'], [90000, 99999, 'result1.csv']],
    [[100000, 109999, 'result2.csv']],
    [[110000, 119999, 'result3.csv']],
    [[129999, 130000, 'result4.csv']]
]

def crawl(start, stop, file):
    f = open(file, "a")
    writer = csv.writer(f)
    session = requests.Session()
    session.headers.update(HEADERS)

    for id in range(start, stop + 1):
        params = {"keywords": str(id), "year": "2024"}

        try:
            response = session.get(BASE_URL, params=params)
            data = response.json()['data'][0]
            
            points = (
                data['id'],
                data['HO_TEN'],
                data['TOAN'],
                data['VAN'], 
                data['NGOAI_NGU'],
                data['CHUYEN'],
                sum((data['TOAN'], data['VAN'], data['NGOAI_NGU'])),
                sum((data['TOAN'], data['VAN'], data['NGOAI_NGU'], 2 * data['CHUYEN'] if data['CHUYEN'] > 0 else 0)),
            )

            writer.writerow(points)

            Logger.log_message(f"SUCCESS - ID: {id}")
        except:
            Logger.log_warning(f"FAILED - ID: {id}")

    f.close()

def thread(tasks):
    for task in tasks:
        crawl(*task)

if __name__ == "__main__":
    threads = []

    for task in THREAD_TASKS:
        t = threading.Thread(target=thread, args=(task,))
        threads.append(t)
        t.start()

        Logger.log_message(f"STARTED - THREAD: {task}")
    
    for t in threads:
        t.join()

