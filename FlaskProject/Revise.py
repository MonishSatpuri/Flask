# print("A" , "B" , "C", sep="~")
# print("Monish", "is", "a", "Good", "Guy", end=".")


# str = '1234567890'
# print(len(str))
# print(str[:-7])     #evaluated to (0-3)
# print(str[5:7])        # 67


# name="Honey"
# print(name.upper())     #HONEY
# print(name.lower())     #honey
# print(name.isupper())   #False same reason as below
# print(name.islower())   #False cuz it checks "Honey"


# name='---Honeyyyy!!!'
# print(name.rstrip('!'))     #---Honey
# print(name.lstrip('-'))     #Honey!!!


# name='Monish is a good boy but Monish is also a red flag, Monish is cool too'
# print(name.replace("Monish", "Honey"))  #All Monish replaced by Honey


# string="Hello World, It's ME, Monish!"
# print(string.split(","))    #['Hello World', "It's ME", "Monish"]


# name='honey is a GoodBoy HA Ha'
# print(name.capitalize())        #Honey is a good boy ha ha


# name='Honey'
# a=(name.center(55))
# print(a)                            #Honey
# print(len(a))                   # 55


# name='Hooney'
# print(name.count('o'))          #2


# name='hello world'
# print(name.endswith('o', 0, 5))     #TRUE


# name='honey'
# print(name.find('ney'))         #2


# name='Honey'
# print(name.endswith('y', 3, 5))


# name="Honey"
# for i in name:
#     if i=='y':
#         print("END of name!")
#     else:
#         print(i)


# name=['Honey', 'Monish']
# for i in name:
#     print(i)
#     for c in i:
#         print(c)


# for i in range(10, 0, -1):
#     print(i)


# list=[0,1,2,3,4,5,6]
# # print(list[7:-7])
#
# if 0 in list:
#     print("Yes")
# else:
#     print("NO!")


# list=[]
# for i in range(8):
#     list.append(i)
#     # list.append(1)
# print(list)
#
# # print(list.count(1))
#
# list.insert(0, 'Honey')
# print((list))
#
# listA=['Monish', 10,20,30]
# # print(listA+list)
# # print(new)
# # list.extend(listA)
# print(list)


# country=("India", "Norway", "Russia", "Germany")
# print(country.index('Norway', 0,2))
# temp=list(country)
# temp.pop(0)
# temp.insert(0, "Bharat")
# # print(type(country))
# country=tuple(temp)
# print(country)
# area=("hell", "Heaven")
# new=country+area
# print(new)


# party={"Monish" : "Organiser",
#        "Happy" : "Guest",
#        "Gupta" : "Vendor"}
#
# print(party.keys())
# print(party.values())
# print(party.items())


# for i in range(3):
#     print(i)
# else:
#     print("Sorry")



# try:
#     for i in range(2,m):
#         print(i)
#
#
# except Exception as e:
#     print(f"There's an error {e} in your system")


import os, shutil
# print(os.getcwd())
# if(os.path.exists("Honey")):
#     shutil.rmtree("Honey")
#     os.mkdir("Honey")
# else:
#     os.mkdir("Honey")

# os.rename("Honey", "Monish")

# print(os.chdir("E:\FlaskProject"))
# print(dir(os))
# os.mkdir("Monish")



# file=open("Honey",'w')
# file.writelines(["Honey is my name\n", "Monish is my official name\n"])
# file.close()
# # text1=file.read()
#
# file=open("Honey",'r')
# # file.writelines(["Honey is my name\n", "Monish is my official name\n"])
# print(file.readlines())
# file.close()


class Car:
    def __init__(self, name, brand):
        self.name=name
        self.brand=brand

Japan=Car("Amaze", "Honda")
print(Japan.name)