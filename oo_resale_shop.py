from computer import *

"""
Name: Destiny Cecchi Samuels
Professor: Jordan Crouser and Johanna
* Code help from CSC TA's 

Resale Shop that buys, refurbish, and sells computers! 

"""
class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    """
    ResaleShop constructor
    """
    def __init__(self):
        self.inventory = []  
    # What methods will you need?

    """
    Add computer into the inventory list.
    """
    def buy(self, computer:Computer):
        self.inventory.append(computer)

    """
    Updates the price of the computer.
    """
    def updatePrice(self, computer:Computer, new_price):
        if computer in self.inventory:
            computer.price = new_price
        else: 
            print("Item not found. Cannot update price.")

    """
    Updates the OS of the computer.
    """
    def updateOS (self, computer: Computer, new_os):
        if computer in self.inventory:
            computer.operatingSystem = new_os
        else:
            print("Item not found. Cannot update OS.")

    """
    Changes the prices of the computer based on the year it was made.
    """
    def refurbish(self, computer:Computer):
        if computer in self.inventory:
            if int(computer.yearMade) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.yearMade) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.yearMade) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff
        else:
            print("Item not found. Please select another item to refurbish.")
    
    """
    Removes the computer from inventory.
    """
    def sell (self, computer:Computer):
        self.inventory.remove(computer)

    """
    Prints all the items in the inventory (if it isn't empty), prints error otherwise.
    """
    def printInventory(self, computer:Computer):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for computer in self.inventory:
                # Print its details
                computer.printAttributes()  
        else:
            print("No inventory to display.")

"""
Just to see if it works!
"""
# def main():
#     computer1 = Computer("ASUS Republic of Gamers",
#         "Intel Core I-7th Gen",
#         250, 60,
#         "Windows", 2017, 1000)
#     computer2 = Computer("MacBook Air",
#         "Apple Chip M1",
#         1024, 8,
#         "macOS Big Sur", 2020, 1000)
    
#     testShop = ResaleShop()

#     testShop.buy(computer1)
#     testShop.printInventory(computer1)

#     testShop.buy(computer2)
#     testShop.printInventory(computer2)

#     testShop.refurbish(computer2)
#     testShop.printInventory(computer2)

#     testShop.updateOS(computer1, "XYZ")
#     testShop.printInventory(computer1)

#     testShop.sell(computer1)
#     testShop.printInventory(computer1)
    
# main()