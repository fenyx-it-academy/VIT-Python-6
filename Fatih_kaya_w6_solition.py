"""
1. Rastgele Sayi Tahmini
"""

# from random import randint
# import time
# start_time = time.time()

# computer_choise = randint(0, 100)

# while True:
#     try:
#         your_guess = int(input("Please type your guess: "))
#         if your_guess < computer_choise:
#             print("Your answer is too low. Try again:  ")
#         elif your_guess > computer_choise:
#             print("Your answer is too high. Try again:  ")
#         else:
#             end_time = time.time() - start_time
#             print(f"Your answer is correct! And -- {end_time:0.2f}-- seconds passed!")
#             break
#     except:
#         print("Your guess is not an integer. Try again!")

"""
2. Zar Yüzdesi
"""
# from random import randint

# zar = [0,0,0,0,0,0]

# for i in range(4999):
#     computer_choise = randint(1,6)
#     zar[computer_choise - 1] += 1
#     # print(computer_choise) 

# print(f"""{zar}\n
# 1'in gelme olasılığı -> %{zar[0]*100/5000}\n 
# 2'nin gelme olasılığı -> %{zar[1]*100/5000}\n 
# 3'ün gelme olasılığı -> %{zar[2]*100/5000}\n 
# 4'ün gelme olasılığı -> %{zar[3]*100/5000}\n 
# 5'in gelme olasılığı -> %{zar[4]*100/5000}\n 
# 6'nın gelme olasılığı -> %{zar[5]*100/5000} """)
        
# zar_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# for i in range(4999):
#     computer_choise = randint(1,6)
#     zar_dict[computer_choise] += 1

# print(f"""{zar_dict}\n
# 1'in gelme olasılığı -> %{zar_dict[1]*100/5000}\n 
# 2'nin gelme olasılığı -> %{zar_dict[2]*100/5000}\n 
# 3'ün gelme olasılığı -> %{zar_dict[3]*100/5000}\n 
# 4'ün gelme olasılığı -> %{zar_dict[4]*100/5000}\n 
# 5'in gelme olasılığı -> %{zar_dict[5]*100/5000}\n 
# 6'nın gelme olasılığı -> %{zar_dict[6]*100/5000} """)

"""
3. Basic Import
"""

# # my_dice.py
# from random import randint

# zar_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}



# def rollDice():
#     repeat_number = int(input("Please type repeat number: "))
#     for i in range(repeat_number):
#         computer_choise = randint(1,6)
#         zar_dict[computer_choise] += 1
#     return print(f"""{zar_dict}\n
# 1'in gelme olasılığı -> %{zar_dict[1] * 100 / repeat_number} 
# 2'nin gelme olasılığı -> %{zar_dict[2] * 100 / repeat_number} 
# 3'ün gelme olasılığı -> %{zar_dict[3] * 100 / repeat_number} 
# 4'ün gelme olasılığı -> %{zar_dict[4] * 100 / repeat_number} 
# 5'in gelme olasılığı -> %{zar_dict[5] * 100 / repeat_number} 
# 6'nın gelme olasılığı -> %{zar_dict[6] * 100 / repeat_number} """)

# # rollDice(repeat_number)

# # main.py

# from my_dice import rollDice

# rollDice()
