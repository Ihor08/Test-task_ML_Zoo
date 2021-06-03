
listofanimals = ["lion", "monkey", "panter", "lynx", "deer", "roe", "hare",
                "raccoon", "bear", "crocodile", "horse", "cheetah"]

travoidni = ["monkey", "deer", "roe", "hare", "raccoon", "horse"]
myasoidni = ["lion", "panter", "lynx", "crocodile", "cheetah"]

a = int(input("Enter how many lions do you want: "))
b = int(input("Enter how many monkeys do you want: "))
c = int(input("Enter how many panter do you want: "))
d = int(input("Enter how many lynx do you want: "))
e = int(input("Enter how many deer do you want: "))
f = int(input("Enter how many roe do you want: "))
g = int(input("Enter how many hare do you want: "))
k = int(input("Enter how many raccoon do you want: "))
l = int(input("Enter how many bear do you want: "))
m = int(input("Enter how many crocodile do you want: "))
n = int(input("Enter how many horse do you want: "))
o = int(input("Enter how many cheetah do you want: "))


lion = 12
monkey = 2
panter = 12
lynx = 10
deer = 9
roe = 5
hare = 1
raccoon = 1
bear = 7
crocodile = 8
horse = 12
cheetah = 10

travoidnianimal = b * monkey + e * deer + f * roe + g * hare + k * raccoon + n * horse

myasoidnianimal = a * lion + c * panter + d * lynx + l * bear + m * crocodile + o * cheetah


if travoidnianimal + myasoidnianimal < 3400000:
    print("You need to create 2 detachment for different classes of animal")
    print(f'You need about {travoidnianimal} square meters for herbivores')
    print(f'You need about {myasoidnianimal} square meters for carnivores')
else:
    print("You don`t have enough territory")

g = str(input("If you want to see how many territory is, write 'yes', if no write 'no' "))

freesquareofzoo = 3400000 - travoidnianimal - myasoidnianimal
if g == "yes":
    print(f'You have {freesquareofzoo} square meters ')
else:
    print("Thanks for attention")
    exit()


otheranimal = str(input("If you want settle down other animal, write 'yes', if no write 'no' "))
if otheranimal =="yes":
    a = int(input("Enter how many lions do you want: "))
    b = int(input("Enter how many monkeys do you want: "))
    c = int(input("Enter how many panter do you want: "))
    d = int(input("Enter how many lynx do you want: "))
    e = int(input("Enter how many deer do you want: "))
    f = int(input("Enter how many roe do you want: "))
    g = int(input("Enter how many hare do you want: "))
    k = int(input("Enter how many raccoon do you want: "))
    l = int(input("Enter how many bear do you want: "))
    m = int(input("Enter how many crocodile do you want: "))
    n = int(input("Enter how many horse do you want: "))
    o = int(input("Enter how many cheetah do you want: "))
else:
    print("Thanks for attention")
    exit()

travoidnianimal2 = b * monkey + e * deer + f * roe + g * hare + k * raccoon + n * horse

myasoidnianimal2 = a * lion + c * panter + d * lynx + l * bear + m * crocodile + o * cheetah

if travoidnianimal2 + myasoidnianimal2 < 3400000:
    print(f'You need about {travoidnianimal2 + travoidnianimal} square meters for herbivores')
    print(f'You need about {myasoidnianimal2 + myasoidnianimal} square meters for carnivores')
else:
    print("You don`t have enough territory")
    exit()

finalsquare = str(input("If you want to see how many territory is, write 'yes', if no write 'no' "))
freesquareofzoo2 = 3400000 - travoidnianimal - myasoidnianimal -travoidnianimal2 - myasoidnianimal2
if finalsquare == "yes":
    print(f'You have {freesquareofzoo2} square meters ')
else:
    print("Thanks for attention")
    exit()




