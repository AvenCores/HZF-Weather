from pyowm import OWM
from pyowm.utils.config import get_default_config

version = 2.0

def pogru():
  global banner
  place = input(banner+"\nВведите город/страну: ")

  config_dict = get_default_config()
  config_dict['language'] = 'ru'

  owm = OWM( 'ba2897bac6149400afc4876fff57e7d7', config_dict  )

  mgr = owm.weather_manager()
  observation = mgr.weather_at_place(place)
  w = observation.weather

  temp_max = w.temperature('celsius')['temp_max']
  temp_medium = w.temperature('celsius')['temp']
  temp_min = w.temperature('celsius')['temp_min']
  speed = w.wind()['speed']
  hum = w.humidity
  cloud = w.clouds
  print(banner+ '\nВ городе ' + place + ' сейчас: ' + str(w.detailed_status) + "\nМаксильмальная температура в районе: " + str(temp_max) + "°С" + "\nСредняя температура в районе: " + str(temp_medium) + "°С" + "\nМинимальная температура в районе: " + str(temp_min) + "°С" +"\nСкорость ветра: " + str(speed) + " м/с" + "\nВлажность: " + str(hum) + "%" + "\nОблачность: " + str(cloud) + "%" +'\n\nНажмите ENTER для выхода в главное меню')
  input()

def info():
    global banner, version
    print(banner+"\nВерсия "+str(version)+"\n\nЗа все действия с программой отвечаете только вы!\n\nСоздатель Telegram - @avencores\n\nНажмите ENTER чтобы выйти")
    input()

while True:
    banner = ("\n" * 100)+ """
__        __         _   _                 _                                       _ _
\ \      / /__  __ _| |_| |__   ___ _ __  (_)_ __    _   _  ___  _   _ _ __    ___(_) |_ _   _
 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__| | | '_ \  | | | |/ _ \| | | | '__|  / __| | __| | | |
  \ V  V /  __/ (_| | |_| | | |  __/ |    | | | | | | |_| | (_) | |_| | |    | (__| | |_| |_| |
   \_/\_/ \___|\__,_|\__|_| |_|\___|_|    |_|_| |_|  \__, |\___/ \__,_|_|     \___|_|\__|\__, |
                                                     |___/                                |___/
Telegram Channel: t.me/hzfnews
VK: vk.com/hzforum1
    """
    print(banner)
    menu = input('1 - Посмотреть погоду\n\n2 - Важная информация!\n\n0 Выход\n')
    if menu == "0": exit()
    if menu == "1": pogru()
    if menu == "2": info()
