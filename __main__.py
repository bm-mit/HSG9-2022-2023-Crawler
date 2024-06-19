
import os
import sys
import csv
from time import sleep
import threading
import requests
from logger import Logger
from concurrent.futures import ThreadPoolExecutor, as_completed


BASE_URL = "https://s6.tuoitre.vn/api/diem-thi-lop-10.htm"
HEADERS = {"Origin": "https://tuoitre.vn"}

THREAD_TASKS = [
    [[9001, 9999, 'result1.csv'],
    [90000, 99999, 'result1.csv']],
    [[100000, 109999, 'result2.csv']],
    [[110000, 119999, 'result3.csv']],
    [[129999, 130000, 'result4.csv']]
]

def crawl(start, stop, file):
    f = open(file, "a", encoding="utf-8")
    writer = csv.writer(f)
    session = requests.Session()
    session.headers.update(HEADERS)


    for id in range(start, stop + 1):
        params = {"keywords": str(id), "year": "2024"}
        try:
            response = session.get(BASE_URL, params=params)
            if response.status_code != 200:
                Logger.log_warning(f"FAILED - ID: {id}")
                continue
            data = response.json()['data'][0]
            print(data["HO_TEN"])
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
def execute_tasks(tasks):
    with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
        futures = [executor.submit(crawl, *task) for task in tasks]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Task failed: {e}")

if __name__ == "__main__":
    threads = []
    with ThreadPoolExecutor(max_workers=len(THREAD_TASKS)) as executor:
        for task_group in THREAD_TASKS:
            executor.submit(execute_tasks, task_group)

    print("All tasks are completed.")
