#my pet

class Critter(object):
    """Your virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
        
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
        print("Prrr... Thanks!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Yupiii")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Your pets's name is...? ")
    crit = Critter(crit_name)
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
            crit.talk()
            print(crit.hunger , crit.boredom)
        #feed
        elif choice == "2":
            food_value = int(input("How much food do you wanna give? "))
            crit.eat(food_value)
        #play
        elif choice == "3":
            play_value = int(input("How long do you wanna play? "))
            crit.play(play_value)
        #unexpectable input
        else:
            print("Sorry, {} not an option".format(choice))

main()
input("\npress Enter to exit")
        
