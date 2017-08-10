# def greet_user():
#     """display a simple greeting."""
#     print("hello")
# greet_user()

# u_name = input("Enter your username: ")
# def greet_user(username):
#     """Displays a user name"""
#     print(username)
# greet_user(u_name)

# u_name = "chillman711"
# def greet_user(user_name):
#     print(user_name)
# greet_user(u_name)

# message = "I'm learning about functions"
# def message_print(mess):
#     """Prints a message"""
#     print(mess)
# message_print(message)
#
# def fav_books(books):
#     """Prints favorite books"""
#     for i in books:
#         print(i)
# b = ['heart of darkness','halo','crash course into python']
# fav_books(b)

# def pet_data(pet_name, pet_type = 'dog',):
#     """Displays pet information"""
#     print("\nI have a "+pet_type)
#     print("My "+pet_type+"'s name is "+pet_name.title())
# # pet_data('dog','cami')
# # pet_data('panda','samantha')
# # pet_data(pet_name = 'cami',pet_type='dog')
# # pet_data(pet_name = 'vishnu',pet_type='snake')
# pet_data('lexi')

# def t_brand(shirt_size, shirt_mess):
#     print("\nMy shirt size is "+ shirt_size +
#         " It should say "+shirt_mess+
#         " on the front")
# t_brand('XL','Est 1990')
#
# def cities(city, location):
#     print(city.title()+ " is located in "+
#         location.title())
# cities('baltimore','maryland')
# cities('san antonio','texas')

# def get_formatted_name(f_name, l_name, m_name = ''):
#     """returns a full name"""
#     if m_name:
#         fullname = f_name + ' '+m_name+' '+l_name
#         #return fullname.title()
#     else:
#         fullname = f_name + ' '+m_name+' '+l_name
#     return fullname.title()
# name = get_formatted_name('julian','itwaru')
# o_name = get_formatted_name('samantha','tisdale','denise')
# print(name)
# print(o_name)

# def get_formatted_name(f_name, l_name, m_name = ''):
#     """returns a full name"""
#     if m_name:
#         fullname = f_name + ' '+m_name+' '+l_name
#         #return fullname.title()
#     else:
#         fullname = f_name + ' '+m_name+' '+l_name
#     return fullname.title()
#
# while True:
#     print("\n(enter 'q' at anytime to quit)")
#     f_name = input("Enter first name ")
#     l_name = input("Enter last name ")
#     if f_name == 'q':
#         break
#     if l_name == 'q':
#         break
#     full = get_formatted_name(f_name, l_name, ' ')
#     print(full)
# city = []
# def city_county(city, county):
#     """returns a city and a country"""
#     cc = city.title() + " " + county.title();
#     #return cc
#
# while True:
#     print("type quit to exit")
#     c_entered = input("Enter a city: ")
#     country_entered = input("Enter a country: ")
#     if c_entered == 'quit':
#         break
#     if country_entered == 'quit':
#         break
# city.append(city_county(c_entered,country_entered))
# for i in city:
#     print(i)
album = {
    'Hybrid_Theory':{
        'song':'one step closer',
        'song':'crawling',
        'song':'without you'
    }
}

for k,v in album.items():
    print(k['song'] + " " + v)
