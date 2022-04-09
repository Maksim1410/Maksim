print ("Угадай число от 1 до 3")
number = input()
while True:
    if number == 1:
        print ("Ты выйграл")
        break
    if number == 2:
        print ("Ты проиграл")
    if number == 3:
        print ("Ты проиграл")
print ("Хочешь сыграть еще раз?")
ahah = input()
if ahah == ("да"):
    True
if ahah == ("нет"):
    print("Хорошо")