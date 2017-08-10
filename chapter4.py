# witcher = ['gerlt','triss','yenefer','dead guy']
# for name in witcher:
#     print(name.title()+" person in the game witcher")
#     print("still in the loop\n")
#print("\noutside the loop")

# pizzas = ['shrimp scampi','meat lovers','classic cheese']
# for list_of_pizza in pizzas:
#     print("I love "+list_of_pizza)
# print("These are my favorite kinds of pizzas!\n")
#
# pets = ['dog','snake','snapping turtle']
# for list_of_pets in pets:
#     print("A "+list_of_pets+" would make a good pet")
# print("any of these animals would make a great pet")
# # for numbers in range(1,61):#range is 0 based index so 1-59 will print could put range(1,60+1) or range(1,61)
# #     print(numbers)
# num= list(range(1,11))
# print(num)
# evens = list(range(0,11,2))
# print(evens)
# for even in evens:
#     print(even)
# square = []
# for values in range(0,11):
#     val = values**2#takes the values and squares everything then stores it into val
#     square.append(val)#val is then appened or added to the list of square after each iteration. added it behind the last appened value
# print(square)
# print(min(square))
# print(max(square))
# print(sum(square))
# print("\n")
# other_squares = [value**2 for value in range(1,11)]
# print(other_squares)

#execrises

# nums = [numbers for numbers in range(1,21)]
# print(nums)
# lotonums = [fuck for fuck in range(0,1000001)]
# #print(lotonums)
# #for i in lotonums:
# #    print(i)
# print(min(lotonums))
# print(max(lotonums))
# print(sum(lotonums))
#
# odd=[]
# for i in range(1,30,2):
#     value = i
#     odd.append(value)
# cube=[]
# for i in range(1,11):
#     value = i**3
#     cube.append(value)
# three = []
# for i in range(0,31,3):
#     value = i
#     three.append(value);
# print(odd)
# print("\n")
# print(cube)
# print("\n")
# print(three)
#
# ccubes = [cbs**3 for cbs in range(1,10)]
# print(ccubes)

# players = ['julian','wes','christopher','cami','steve','joe']
# print(players[0:3])#slices the list from index 0 to index3
# print("\n")
# print(players[:4])#prints everything upto 4th index
# print("\n")
# print(players[2:])#print everything starting from the 2nd index
# print("\n")
# print(players[-3:])#starts from the i-3 index and prints to end of list
# print("\n")
# print("These are the players in my team")
# for i in players[:3]:
#     print(i)


square = (40,40)
rectangle = (40,50)
triangle = (30,30,60)
print("The dimensions of the square are")
for i in square:
    print(i)
print("\n")
print("The dimensions of the rectangle are")
for i in rectangle:
    print(i)
print("\n")
print("The dimensions of the triangle are")
for i in triangle:
    print(i)
print("\n")
square = (50,50)
print("The new square diemensions are")
for i in square:
    print(i)
