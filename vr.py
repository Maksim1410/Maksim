#Подключаем модуль
import random
attNumber = 0
print("Привет, как тебя зовут")
myName = input()
number = random.randint(1,1000000)
print("Что ж, " +myName+" , я загадываю число от 1 до 1000000.")
for attNumber in range(30):
    print("Попробуй угадать.") #Четыре пробела перед именем функции
    guess = input()
    guess = int(guess)
    if guess < number:
        print("Твое число слишком маленькое.") #Восемь пробелов
    if guess > number:
        print("Твое число слишком большое.") #Восемь пробелов
    if guess == number:
        break
if guess == number:
    attNumber = str(attNumber + 1)
    print("Отлично, "+ myName+"! Ты справился за "+attNumber+" попытки!")
if  guess != number:
    number = str(number)
    print("Увы. Я загадал число "+number+".")
print("Спасибо за участие в моей игре!")
