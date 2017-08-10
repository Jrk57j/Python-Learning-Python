#alien_O={'color':'red','points':5,'x-position':0,'y-position':25}
# alien_O={'color':'red','points':5}
# print(alien_O['color'])
# score = alien_O['points']+alien_O['points']
# print("Your score is "+str(score))
# alien_O['x_position'] = 0
# alien_O['y_position'] = 25
# print(str(alien_O['y_position'])+" position on the screen via y axis")
# print(alien_O)
# alien_P = {}
# alien_P['color'] = "purple"
# alien_P['points'] = 30
# alien_P['x_position'] = 50
# alien_P['y_position'] = 60
# print(alien_P)
# alien_P['color'] = "zebra"
# print(alien_P)
# alien_P['speed'] = "medium"
# print("original position for alien_P is "+str(alien_P['x_position']) + " " + str(alien_P['y_position'])+ " "+ "speed is "+ alien_P['speed'])
# if alien_P['speed'] == 'slow':
#     x_increment = 1
# elif alien_P['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_P['x_position'] = alien_P['x_position'] + x_increment
# print("new positin is "+str(alien_P['x_position']))
# del(alien_P['speed'])
# print(alien_P)
# # alien_P['speed'] = "fast"
# # print(alien_P)
fave_prog = {
    'julian':'python',
    'chris':'php',
    'eddy':'c',
    'evan':'java',
    'richard':'nothing'
    }
# #print(fave_prog)
# print("Julian's favorite language is "+
#     fave_prog['julian'].title())
# chris = {
#     'name':'chris',
#     'address':'someplace utsa',
#     'city':'san antonio',
#     'number':'1800eatadick'
#     }
#print(chris)
# print("a good friend of mine is "+
#     chris['name']+" and he lives at "+
#     chris['address']+
#     " and he number is "+
#     chris['number'])

# fave_numbers = {'julian':69,'life':42,'chris':108,'samantha':5}
# print("Julain's favorite number is : "+ str(fave_numbers['julian']))
# print("Lifes's favorite number is : "+ str(fave_numbers['life']))
# print("Chris's favorite number is : "+ str(fave_numbers['chris']))
# print("Samantha's favorite number is : "+ str(fave_numbers['samantha']))
#
# fave_num = {'name':'julian','num':43,'o_name':'chris','o_num':203}
# print(fave_num)
# print(fave_num['name']+" "+str(fave_num['num']))

# glossary = {
#     'elif':'elif: a weird way to say else if',
#     'dictonary':'dictonary: a dynamic storage in python',
#     'slice':'slice: a way to start at a position in a list',
#     'sort':'sort: a way to sort the data',
#     'pizza':'pizza: a delicious food'
#     }
# print(glossary['elif']+"\n")
# print(glossary['dictonary']+"\n")
# print(glossary['slice']+"\n")
# print(glossary['sort']+"\n")
# print(glossary['pizza']+"\n")

# user_O = {
#     'username':'chillman711',
#     'fname':'julian',
#     'lname':'itwaru'
#     }
# for key, value in user_O.items():
#     print("\nKey: "+key)
#     print("Value: "+value)
# for k,v in fave_prog.items():
#     print("\nName " +k.title())
#     print("Prog " + v.title())
# print("\n")
# for i in fave_prog.keys():
#     print(i.title())

homies = ['eddy','chris', 'julian']
for i in sorted(fave_prog.keys()):
    if i in homies:
        print("Hello "+ i.title()+
        " I see your favorite language is "+
        fave_prog[i].title()+"!")
print("\nThe languages mentioned are:")
for v in sorted(fave_prog.values()):
    print(v)
left off at page  108
