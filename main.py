
from Models.Bird import Bird
from Models.Cat import Cat
from Models.Dog import Dog

def AskAnimalData() -> dict:

    values = {}

    values["name"] = input("Entrez le nom de l'animal : ")
    values["size"] = askInteger("Entrez la taille en cm de l'animal : ")
    values["weight"] = askFloat("Entrez le poids en Kg de l'animal : ")
    values["sex"] = input("Entrez le sexe de l'animal : ")
    values["age"] = askInteger("Entrez l'age en années de l'animal : ")
    values["arrived"] = input("Entrez la date d'arrivée de l'animal : ")

    return values;

def AskBirdData() -> Bird:
    values = AskAnimalData();
    values["color"] = input("Entrez la couleur de l'oiseau : ")
    values["aviary"] = True if input("Necessite t'il une voliere ? y/-") == "y" else False

    return Bird(values["name"], values["size"], values["weight"], values["sex"], values["age"], values["arrived"], values["color"], values["aviary"])

def askInteger(sentence) -> int:

    value = "-1"

    while(not value.isdigit()):
        value = input(sentence)

    return int(value);

def askFloat(sentence) -> float:

    while(True):
        try:
            value = float(input(sentence))
            return value;
        except:
            print("Valeur invalide, ressayez.")


print(AskBirdData())

bird = Bird("Coco", 23, 0.6, "M", 12, "12/05/2020", "Red", True)

cat = Cat("O'maley le chat de goutiere", 15, 4, "male", 3, "05/12/2021", "espiegle", False, False)

dog = Dog("Oddy", 12, 6, "male", 2, "12/06/2023", "rouge", "parson russel terrier croisé avec un beagle", False)

print(dog)