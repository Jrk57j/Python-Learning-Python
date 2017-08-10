# cars = ['gti','speed3','golf r','passat']
# print(cars)
# print(cars[1].title())
# #print("My first car was a " +cars[0].title())
# message = "My first car was a "+ cars[0].title()+ "!"
# print(message)
#
# names = ['samantha','chris','nick','jerry']
# print("A few of my friends are "+ names[1].title()+" , "+names[2].title()+" , "+names[3].title()+"\nand my girlfriend is "+names[0].title()+".")
# names.append('evan')
# names.append('richard')
# print(names)
# names.insert(0,'wes')
# print(names)
# #del names[-1]
# #print(names)
# douche = names.pop()
# print(names)
# print()
# print(douche+" is a douche"
# +" this is also how to use pop")
# print(douche)
# names.remove('samantha')
# print(names)

guest_list = ['chirs','jerry','renee','nick','lexi','evan','alex','julia','richard','eddy']

print("the people coming to the cookout are "+ guest_list[0].title()+" "+guest_list[1].title()+" "+guest_list[3].title()+" "+guest_list[5].title()+" "+ guest_list[6].title()+" "+ guest_list[8].title()+" "+guest_list[8].title())
print("the people not coming are " + guest_list.pop(2)+ " "+guest_list.pop(3)+" "+guest_list.pop(5))
guest_list.insert(0,'bradon')
guest_list.insert(4,'cuntface')
guest_list.insert(9,'jlaw')
print(guest_list)
print("I just found out that "+guest_list.pop(9).title()+" and "+guest_list.pop(4).title()+" wont make it")
guest_list.sort()
print(guest_list)
guest_list.reverse()
print(guest_list)
cars = ['gti','speed3','golf r','passat']
print("sorted list")
print(sorted(cars))
print("unsorted list")
print(cars)
cars.sort()
print("list is forever sorts")
print(cars)
print("now in reverse")
cars.reverse()
print(cars)
print(len(cars))
print(len(guest_list))
