#Создайте программу, имитирующую телевизор как объект. У пользователя должна быть возможность вводить
#номер канала, а также увеличивать и уменьшать громкость. Программа допжна следить за тем, чтобы номер
#канала и уровень громкости оставались в допустимых пределах.

class Television(object):

    def __init__(self, channel, volume, min_volume = 0, max_volume = 50, min_channel = 1, max_channel = 25):
        self.__channel = channel
        self.__volume = volume
        self.min_volume = min_volume
        self.max_volume = max_volume
        self.min_channel = min_channel
        self.max_channel = max_channel
    @property
    def channel(self):
        return self.__channel
    @property
    def volume(self):
        return self.__volume
    
    def __str__(self):
        rep = "now channel is: " + str(self.__channel) + " and volume is: " + str(self.__volume)
        return rep
    def channel(self, new_channel):
        if new_channel in range(self.min_channel, (self.max_channel + 1)):
            self.__channel = new_channel
            print("You turned on {} channel".format(new_channel))
        else:
            print("Channel doesn't exist")
    def volume_increase(self):
        if self.__volume < self.max_volume:
            self.__volume +=1
            print("Volume now is {}".format(self.__volume))
        else:
            print("Volume should be 0 - 50")
    def volume_reduce(self):
        if self.__volume > self.min_volume:
            self.__volume -=1
            print("Volume now is {}".format(self.__volume))
        else:
            print("Volume should be 0 - 50")
def main():
    tel = Television(1,0)
    choice = None
    while choice != "0":
        print \
        ("""
        Television
        0 - Exit
        1 - Change channel
        2 - Increase volume
        3 - Reduce volume
        4 - Values
        """)
        choice = input("Choice: ")
        print()
        #exit
        if choice == "0":
            print("Good bye")
        #channel
        elif choice == "1":
            choice_channel = int(input("Which channel do you wont to watch? "))
            tel.channel(choice_channel)

        #volume increase
        elif choice == "2":
            tel.volume_increase()

        #volume reduce
        elif choice == "3":
            tel.volume_reduce()
        #values
        elif choice == "4":
            print(tel)
        
        else:
            print("Sorry, {} not an option".format(choice))

main()
input("\npress Enter to exit")
        
