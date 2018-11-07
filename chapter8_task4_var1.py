#my pet
#Фиклированное кол-во питомцев. В данном случае 5
#Доступ к данным питомца - 555
import random as r
class Critter(object):
    """Your virtual pet"""
    def __init__(self, name, hunger, boredom):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        rep = "Object of class Critter\n"
        rep += "Name of your pet: " + self.name + ", his hunger value: " + str(self.hunger) + ", his boredom value: " + str(self.boredom) + "\n"
        return rep
                
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "perfect"
        elif 5<= unhappiness <=10:
            m = "not bad"
        elif 11<= unhappiness <=15:
            m = "worse than I wish"
        else:
            m = "awful"
        return m
            
    def talk(self):
        print("My name is {} and now I feel {}".format(self.name, self.mood))
        self.__pass_time()
        
    def eat(self, food):
        print("Prrr... Thanks! Said {}".format(self.name))
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Yupiii! Said {}".format(self.name))
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    critters = []
    for i in range(0,5):
        crit_name = input("Your pets's name is...? ")
        hunger_value = r.randint(0, 15)
        boredom_value = r.randint(0, 15)
        critters.append(Critter(crit_name, hunger_value, boredom_value))
    choice = None
    while choice != "0":
        print \
        ("""
        My pet
        0 - Exit
        1 - Find out how your pet feel
        2 - Feed your pet
        3 - Play with your pet
        """)
        choice = input("Pick something: ")
        print()
        #exit
        if choice == "0":
            print("Good bye")
        #talking
        elif choice == "1":
            for i in range(5):
                critters[i].talk()
        #feed
        elif choice == "2":
            food_value = int(input("How much food do you wanna give? "))
            for i in range(5):
                critters[i].eat(food_value)
        #play
        elif choice == "3":
            play_value = int(input("How long do you wanna play? "))
            for i in range(5):
                critters[i].play(play_value)
        #secret input
        elif choice == "555":
            for i in range(5):
                print(critters[i])
        #unexpectable input
        else:
            print("Sorry, {} not an option".format(choice))

main()
input("\npress Enter to exit")
        
