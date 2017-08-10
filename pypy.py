# list_of_names = ['julian','samantha','eddy']
# for i in list_of_names:
#     print(i)
# list_of_names.append('steve')
# for i in list_of_names:
#     print(i)
# langs = {
#     'julian':'java',
#     'samantha':'spanish',
#     'lilo':'java',
#     'steve':'poop'
# }
# album = {
#     'Album':'Hybrid Theory',
#     'songs':['crawling',
#             'without you',
#             'in the end'
#             ]
# }
#
# print("you like "+ album['Album'])
# print("Which has songs like\n")
# for v in album['songs']:
#     print(v)

users = {
    'julian':{
        'first':'Julian',
        'last':'Itwaru',
        'local':'Texas'
    }
}

for k,v in users.items():
    print(k)
    print(v)
