#Yun Ma
#Assignment 10.1
#Purpose: create my own class and methods

class ShoppingCart:
    type = "4 Wheel Shopping Cart"                                  #class variable
    def __init__(self, brand, num_riders, average_age_riders):
        self.__brand = brand                                        #private data variables
        self.__num_riders = int(num_riders)
        self.__age_riders = float(average_age_riders)
        self.__speed = 100.0 - (self.__num_riders * 10)

    def set_brand(self, new_brand):             #used to assign a new value to self.__brand
        self.__brand = new_brand

    def get_brand(self):                        #used to return self.__brand
        return self.__brand

    def set_rider_age(self, new_average_age):   #used to assign a new value to self.__age_riders
        self.__age_riders = new_average_age

    def get_rider_age(self):                    #used to return self.__age_riders
        return self.__age_riders

    def get_rider_number(self):                 #used to return self.__num_riders
        return self.__num_riders

    def get_speed(self):                        #used to return self.__speed
        return self.__speed

    def carpool_checker(self):                  #carpool lane checker
        if self.__num_riders >= 3:
            print(f'{self.__brand} Carpool Lane Available !!')  #if the number of riders on the cart is at least 3, carpool lane is available and self.speed is multiplied by 1.2
            print("Speed is Increased by 20% !!")
            self.__speed *= 1.2
        elif self.__num_riders < 3:                             #if not, print out message
            print(f'{self.__brand} Carpool Lane is Not Available.')
            print("Speed is Not Increased.")

    def age_checker(self):                                      #age checker
        if self.__age_riders >= 8:
            print("Mature Cart Rider Detected !!")              #if average age of the riders is greater than or equal to 8, all riders are removed
            print("All Riders Are Removed !!")
            self.__num_riders = 0
            self.__age_riders = 0
            self.__speed = 100.0                                #self.__speed is then set to 100.
        else:
            print("No Mature Cart Rider Detected !!")           #if it passes the age check, print out message nothing happens.
            print("Age Check Passed !!")

    def shopping_speed_checker(self):                           #shopping speed checker
        if self.__speed >= 70:                                  #if self.speed is >= 70, return "fast shopping"
            return ("Fast Shopping")
        elif self.__speed < 70 and self.__speed >= 40:          #if it's between 70 and 40, return "slow shopping"
            return ("Slow Shopping")
        elif self.__speed < 40:
            return ("Shopping Almost Impossible")               #if it's below 40, return "shopping almost impossible"

#Main function / Test program

def main():
    input_brand = input("Enter Store Name.\n>>> ")                                      #make user input values for the brand, number of riders and average age of them
    input_num_riders = input("Enter the Number of Riders in the Shopping Cart.\n>>> ")
    if int(input_num_riders) > 0:
        input_age_riders = input("Enter the Average Age of the Riders.\n>>> ")
    else:
        input_age_riders = 0
    print("\n")

    cart1 = ShoppingCart(input_brand, input_num_riders, input_age_riders)               #print out general info based on the inputs
    print(f'Current Shopping Cart is a {cart1.type} from {cart1.get_brand()}. \nThe Number of Riders on it is {cart1.get_rider_number()}, And the Average Age of the Riders is {cart1.get_rider_age()}.')
    print(f'Current Speed is {cart1.get_speed()}% of Normal Speed.')
    print("\n")

    filler = input("Enter Any Key to Check if Riders Have to be Evacuated.\n>>> ")      #filler to make printing less in rush

    print("\n")

    print("Checking Rider Age . . .\n")                         #use age_checker to age check
    cart1.age_checker()
    print("\n")

    yesno = int(input("Check Availability For A Carpool Lane? (1 = Yes, 0 = No)\n>>> "))    #use carpool_checker to check availability for a carpool lane
    if yesno == 1:
        cart1.carpool_checker()
    print("\n")

    print(f'Current Speed of the Shopping Cart is {cart1.get_speed()}% of Normal Speed.\nExpected Shopping Speed With Given Info is: {cart1.shopping_speed_checker()}.\nGood Luck!')
    #print out self.__speed and expected shopping speed using shopping_speed_checker.

    """
    print("\n\n")
    x = ShoppingCart("Walmart", 4, 9)
    print(x.get_brand())
    x.set_brand("Target")
    print(x.get_brand())
    print(x.get_rider_number())
    print(x.get_rider_age())
    x.set_rider_age(2)
    print(x.get_rider_age())
    print(x.get_speed())

    print("\n")

    x.carpool_checker()
    print(x.get_speed())

    print("\n")

    x.age_checker()
    print(x.get_rider_number())
    print(x.get_rider_age())
    print(x.get_speed())
    """


if __name__ == "__main__":
    main()