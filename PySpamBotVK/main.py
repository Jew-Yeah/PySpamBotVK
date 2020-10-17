# -*- coding: utf-8 -*-
from os import system
from libs.VK_functions import *


system("title PySpamBotVK")
system("color 2")

while True:
    print("Hi, dear User!")
    print("Choose your action: ")
    print("1 - change list of VK-profiles")
    print("2 - change list of VK-groups for spam")
    print("3 - change text of spam-letter")
    print("4 - start spam")
    print("5 - exit from program")
    try:
        action = int(input(">> "))
    except:
        system("cls")
        continue
    if action == 1:
        print("Your spam-accounts:")
        File = open("resources//accounts.txt")

        for data in File.readlines():

          user_id,login,password = data.split(":")
          print(user_id,login,password)

        File.close()

        print("Choose your action:")
        print("0 - back")
        print("1 - delete all")
        print("2 - add new accounts")
        try:
            action = int(input(">> "))
        except:
            system("cls")
            continue
        if action == 0:
            system("cls")
            continue
        elif action == 1:
            File = open("resources//accounts.txt","w")
            File.close()
            system("cls")
        elif action == 2:
            user_id,login,password = input("ID: "),input("LOGIN: "),input("PASSWORD: ")
            # добавить проверку на существоние пользователя с такими данными
            File = open("resources//accounts.txt","a")
            File.write((":".join([user_id,login,password])+"\n"))
            File.close()
            system("cls")
    elif action == 2:
        pass
    elif action == 3:
        print("Please, write your spam-message: ")
        message = input(">> ")
        File = open("resources//message.txt","w")
        File.write(message)
        File.close()
        system("cls")
    elif action == 4:

        Users_Array = []
        File = open("resources//accounts.txt")

        for data in File.readlines():

          user_id,login,password = data.split(":")
          User = VK_User(user_id,login,password)
          Users_Array.append(User)

        File.close()

    elif action == 5:
        break
    else:
        system("cls")
        continue
