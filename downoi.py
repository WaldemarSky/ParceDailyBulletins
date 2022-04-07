import requests
from requests.exceptions import HTTPError
import os
import datetime
import fake_useragent

ua = fake_useragent.UserAgent()
user = ua.random

url_login = 'https://www.cmegroup.com/content/login/saml_login'
url_load = 'https://www.cmegroup.com/ftp/bulletin/DailyBulletin_pdf_'

directory_folder = os.path.dirname(os.path.abspath(__file__))

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
}

data_auth = {
    'Host': 'www.cmegroup.com',
    'Referer': 'https://auth.cmegroup.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '6855',
    'Origin': 'https://auth.cmegroup.com',
    'Connection': 'keep-alive',
    'Cookie': 'ak_bmsc=1FC7B6783EC6D4FA0FBBD191F6539832~000000000000000000000000000000~YAAQiwVJF/Mg+XN7AQAAyPnpdwzgmCsholgMO9aTF4TMxTDiva3gunj71f78OW/lSrruJlRInFgHADPKcZcqYPeuN1M71honlraSP3u7PxbuM5JGReY3IX2mcYrUY2Q2jdziHr/EmyUmxFyJZb+yD1IiWGuPLTK6dt4Iz6boIjfWWpBZVJih5+lBkM7zmsjmdLCQSRIC3TvXVazBytNEWh5kQRzMWyJPjYEn/Z4IicSfRIVBH/YoaHyyf6gjG+qx1u0bPhT6Oe59lMGu8Ik4kRQk88HsD7LqXJwWJkVCzP5L+O6fbu0ht4z8vN2AM/z+LezfLEh5zrr6hVtI6Hqxp2HYifjs5F0mAQgfp8Ao8eZaeSIGCRZJ2LMmGN5dmk/GoQlT; bm_sv=A5A42AD539078AB88AC71FCDBC92F1F2~6Okdew5cLVWjUOv4svUxd4l2EPSn3D6jV25C3fisw0QHI2iSHtYdSTkamedw2U/WPhNU2cCI42tPrczzo4s1EVreTk5IYeRKdSw/1Gbe+qqBHeReL3vNb/mO5vqlB3i4b630sYr3Jn10ajbi++km93xuo9JRtN0y48vi/qAIFL8=; _gcl_au=1.1.1725981831.1629804446; cmeUTMSource=; cmeUTMMedium=; cmeUTMTerm=; cmeUTMCampaign=; cmeUTMContent=; _ga_L69G7D7MMN=GS1.1.1629804445.1.1.1629807946.0; _ga=GA1.2.496679902.1629804447; _evga_5cd7={%22uuid%22:%22064d762220672030%22}; kppid=m6Wg5wl3xMZ; _gid=GA1.2.187835700.1629804462; _fbp=fb.1.1629804462612.1039201278; _CEFT=Q%3D%3D%3D; login-token=; cmeRegion=west; AWSELB=C13F494F04E721EF25D9DA7AA8D5AC435E2C0AE1CCDA50E8DBC5E21D1A09D0BDE838D04E6E9270ED1ED5BD39ECBC1DA8D293BDF7B0608C6925B357D5C0C4C9A2E2C7C4601A9BAACD0E857652E8917C4EC0DE5CBBB0; pi_opt_in502091=true; visitor_id502091=543315680; visitor_id502091-hash=334656d933ada7f0afc2078c84c30cff78bb95bc00bff0824e8335088065fc58772aeb5ea5193f674a6dd10ce67a5480bc021d44; __atuvc=7%7C34; __atuvs=6124df0df0b332e7006; cmeConsentCookie=true; _gat_UA-6562664-1=1; _gat_UA-63130032-1=1; _dc_gtm_UA-6562664-1=1; _gat_superDomainTracker=1; redirectionCookie=%7B%22location%22%3A%22%2F%22%2C%22flow%22%3A%22login%22%7D; saml_request_path=%2Fcontent%2Fcmegroup%2Fen%2Flogin-confirmed.html',
    'Upgrade-Insecure-Requests': '1'
}


def keep_window_open():
    a = ""
    while a != "~~":
        a = input("Для выхода из программы введите '~~'")


def red_from_file(file, numberch):
    result = ''
    for i in range(numberch):
        ch = file.read(1)
        ch = ch.decode('UTF-8')
        result += ch
    return result


def FindFilePos(file):
    file.seek(-2, 2)
    while True:
        a = file.read(1)
        if a == b'\n':
            break
        file.seek(-2, 1)


try:
    with requests.Session() as se:
        se.headers = header
        # auth = se.post(url_login, data=data_auth)
        logfile = open(f"{directory_folder}\log.txt", 'ab+')
        # pos = logfile.seek(-13, 2)
        FindFilePos(logfile)
        year = red_from_file(logfile, 4)
        print(year)
        month = red_from_file(logfile, 2)
        day = red_from_file(logfile, 2)
        counter = int(red_from_file(logfile, 4)) + 1
        current_day = datetime.date(year=int(year), month=int(month), day=int(day)) + datetime.timedelta(1)
        logfile.close()

        while current_day < datetime.datetime.now().date():
            print(f"Обработка даты: {current_day}")

            if current_day.month == 1 and current_day.day == 1:
                counter = 1

            current_date_str = r"{}{}{}{}".format(current_day.year, "{0:02d}".format(current_day.month),
                                                  "{0:02d}".format(current_day.day), counter)
            current_url = r"{}{}.zip".format(url_load, current_date_str)

            r = se.get(current_url)
            print(r)
            if r.status_code == 200:
                with open(r"{}\DailyBulletin_pdf_{}.zip".format(directory_folder, current_date_str), 'wb') as f:
                    f.write(r.content)
                    print(r"Файл DailyBulletin_pdf_{}.zip успешно сохранен".format(current_date_str))
                    counter += 1
                    logfile = open(f"{directory_folder}\log.txt", 'at+')
                    logfile.write(current_date_str)
                    logfile.write('\n')
                    logfile.close()
            elif r.status_code == 404 and counter_cycle < 3:
                print(r"Обработка файла DailyBulletin_pdf_{}.zip не удалась".format(current_date_str))
                counter_cycle += 1
                continue
            counter_cycle = 0
            current_day = current_day + datetime.timedelta(1)
        logfile.close()



except Exception as err:
    print(f"Что-пошло не так при работе программы: {err}")
    keep_window_open()

else:
    print("Программа завершена")
    keep_window_open()
