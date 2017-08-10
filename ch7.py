# message = input("Tell me something: ")
# print("\n"+message)

# name = input("Please tell me your name ")
# print("\nHello "+ name)

# prompt = "if you tell us who you are, we can personalize the messages you see."
# prompt +="\nWhat is your first Name? "
# name = input(prompt)
# print(name)

# height = input("How tall are you? ")
# height = int(height)
# if height >= 72:
#     print("\n You're tall")
# else:
#     print("\n You're short")

# prompt = "enter a number and ill let you know if it is"
# prompt += " odd or even: "
# num = input(prompt)
# num = int(num)
# if num %2 == 0:
#     print("\nYour number is even")
# else:
#     print("\nYour number is odd")

# car = input("What kind of rental car would you like? ")
# print("Let me see if we have that.")
# print("....")
# if car.upper() == "GTI":
#     print("\nWe will have it ready for you soon")
# else:
#     print("\nSorry we do not have that in stock")

# prompt = input("And how many people will we be seating tonight? ")
# num_of_people = int(prompt)
# if num_of_people >= 8:
#     print("\nIm sorry. You will have to wait to be seated")
# else:
#     print("\nRight this way!")

# prompt = ("give me a number and ")
# prompt +=("i will tell you if its a multiple of ten ")
# num = input(prompt)
# num = int(num)
# if num % 10 == 0:
#     print("\nThis is a multiple of 10")
# else:
#     print("\nthat number is not a multiple of 10")

# cur_num = 1
# while cur_num <=5:
#     print(cur_num)
#     cur_num+=1

# prompt = ("\n tell me something, when you are done. type quit ")
# prompt +=(" to exit the program\n")
# # message = " "
# # while message.strip() != "quit":
# #     message = input(prompt)
# #     print("\n"+message)
# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print("Message is: "+message)

# prompt = "What city have you been too? "
# print("\nEnter quit when you are finished.")
# while True:
#     city = input(prompt)
#     if city == "quit":
#         break
#     else:
#         print(city)
# cur_num = 0;
# while cur_num < 51:
#     cur_num+=1
#     if cur_num % 2 == 0:
#         continue
#     print(cur_num)

prompt = "Please enter the toppings you want: "
print("\n enter 'exit' to terminate.")
active = True
while active:
    topping = input(prompt)
    if topping == "exit":
        active = False
    else:
        print("\n"+topping + " Will be added to your pizza")
left off at 128
