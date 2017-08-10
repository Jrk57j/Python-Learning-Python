#if statements and now with pep8 standards
# cars = ['audi','bmw','volkswagen','ford']
# #testing with for-loop and if else
# for i in cars:
#     if i == 'volkswagen':
#         print(i.upper())
#     else:
#         print(i.title())
# #testing with if else
# age = 27
# legal = 21
# if age > legal:
#     print("Come on in")
# else:
#     print("go home")
# #testing statements
# print(age > legal)
# print(age < legal)
# print(age == legal)
# print(age > legal and 5 > 3)
# print(age > legal or 5 < 3)

# toppings = ['green peppers','bacon','feta','spinach','chicken','pineapple']
# print("feta" in toppings)
# print("artichoke" in toppings)
# print("\n")
# my_tops = ['green peppers','bacon','spinach']
# print("Are my toppings in you selections")
# for i in my_tops:
#     if(i in toppings):
#         print(i+" yes")
#     else:
#         print("no")
# print("\n")
# friend_top = ['feta','meth','pineapple']
# for i in friend_top:
#     if(i in toppings):
#         print(i+" yes")
#     else:
#         print(i+" im calling the cops")

# banned_users = ['evan','richard','eddy','nick']
# allowed_users = ['julian','chris','samantha','jerry','renne','richard']
# for i in allowed_users:
#     if i not in banned_users:
#         print(i+" you may proceed")
#     else:
#         print(i+" youre not allowed in here")
# print("\n")
# user = "steve"
# o_user = "eddy"
# if user not in banned_users:
#     print(user+" you may proceed\n")
# else:
#     print(user+" gtfo\n")
# if o_user not in banned_users:
#     print(o_user+" you may proceed\n")
# else:
#     print(o_user+" gtfo\n")

# age = 19
# if(age < 10):
#     print("admission is free\n")
# elif(age < 20):
#     print("your admission is 8 dollars\n")
# else:
#     print("your admission is 20 dollars\n")

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 10
# else:
#     price = 15
# print("Your admission will cost: "+ str(price)+".")

# toppings = ['mushrooms','ham','bacon','sausage','anchonvies','green peppers']
# extra_toppings = ['mushrooms','ham','bacon']
# print("would you like some extra toppings?")
# if 'bacon' in toppings:
#     print("adding bacon to your pizza")
# if "ham" in toppings:
#     print("adding ham to your pizza")
# if "anchonvies" in toppings:
#     print("adding anchonvies to you pizza")
# print("finishing your pizza now\n")
#
# for i in extra_toppings:
#     if(i in toppings):
#         print("add "+ i +" to your pizza")
# print("finishing your pizza now\n")


# alien_color = ['red','purple','pasta']
# ak1 = 'red'
# ak2 = "purple"
# ak3 = "pasta"
# # if ak3 in alien_color[0]:
# #     print("5 points")
# # elif ak3 in alien_color[1]:
# #     print("20 points")
# # else:
# #     print("onomnnomnom")
# if ak1 == "green":
#     print("20 points\n")
# if ak1 == "red":
#     print("You kill frank, -1,000,000 points!\n")
# if ak2 == "purple":
#     print("killed purple guy, 400 points\n")
# if ak3 == "pasta":
#     print("Dinner time, health regan + stam buff\n")

# age = 15
# if age < 2:
#     print("youre a baby")
# elif age <= 2 and age > 4:
#     print("youre a toddler")
# elif age <= 5 and age < 13:
#     print("youre a child")
# elif age <= 13 and age > 19:
#     print("youre a young adult")
# elif age <= 19 and age < 50:
#     print("youre an adult")
# else:
#     print("you old as fuck")
#

#back to pizza
# avaiable_toppings = ['mushrooms','green peppers','bacon','chicken','beef'
#                      'ham','squid','smoked mystery meat']
# requested_toppings = ['mushrooms','bacon','chicken','death']
# for i in requested_toppings:
#     if i in avaiable_toppings:
#         print("adding "+ i +" to your pizza")
#     else:
#         print("Im sorry we do not "+ i+" as a topping")

user_name = ['tim','erica','steve','admin','bacon', 'ROSS']
for i in user_name:
    if i == "admin":
        print ("Would you like to see the status report admin\n")
    elif i != "admin":
        print("Hello "+ i+"\n")
new_users = ['kim','rachel','ross','steve']
for i in new_users:
    if i in user_name:
        print("cannot use "+ i.upper()+ " user name is already taken")
#come back to last project questions
