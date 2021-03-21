from pyowm import OWM
from pyowm.utils.config import get_default_config

version = 1.1

def pogru():
  global banner
  place = input(banner+"\nВведите город/страну: ")

  config_dict = get_default_config()
  config_dict['language'] = 'ru'

  owm = OWM( 'ba2897bac6149400afc4876fff57e7d7', config_dict  )

  mgr = owm.weather_manager()
  observation = mgr.weather_at_place(place)
  w = observation.weather

  temp = w.temperature('celsius')['temp']
  print(banner+ '\nВ городе: ' + str(w.detailed_status) + "\nТемпература в районе: " + str(temp) + '°C' +'\n\nНажмите ENTER для выхода в главное меню')
  input()

def info():
    global banner, version
    print(banner+"\nВерсия "+str(version)+"\n\nЗа все действия с программой отвечаете только вы!\n\nСоздатель Telegram - @avencores\n\nНажмите ENTER чтобы выйти")
    input()

while True:
    banner = ("\n" * 100)+ """
__        __         _   _                 _                                        _ _
\ \      / /__  __ _| |_| |__   ___ _ __  (_)_ __    _   _  ___  _   _ _ __    ___(_) |_ _   _
 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__| | | '_ \  | | | |/ _ \| | | | '__|  / __| | __| | | |
  \ V  V /  __/ (_| | |_| | | |  __/ |    | | | | | | |_| | (_) | |_| | |    | (__| | |_| |_| |
   \_/\_/ \___|\__,_|\__|_| |_|\___|_|    |_|_| |_|  \__, |\___/ \__,_|_|     \___|_|\__|\__, |
                                                     |___/                                |___/
Telegram Channel: t.me/hzfnews
VK: vk.com/hzforum1

    """
    print(banner)
    menu = input('1 - Посмотреть погоду\n\n3 - Важная информация!\n\n0 Выход\n')
    if menu == "0": exit()
    if menu == "1": pogru()
    if menu == "3": info()
