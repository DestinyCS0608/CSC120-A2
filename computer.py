"""
Name: Destiny Cecchi Samuels
Professor: Jordan Crouser and Johanna

Computer class that builds computers with attributes: description, processor type, 
hard drive capacity, memory, operating system, year, and price.

"""


class Computer:

    # What attributes will it need?
    description: str
    processorType: str
    hardDriveCapacity: int
    memory: int
    operatingSystem: str
    yearMade: int
    price: int
    
    # How will you set up your constructor? (assign values to each of the above attributes) 
    # Remember: in python, all constructors have the same name (__init__)

    """" 
    Computer constructor.
    """
    def __init__(self, description: str,
                    processorType: str,
                    hardDriveCapacity: int,
                    memory: int,
                    operatingSystem: str,
                    yearMade: int,
                    price: int):
        
        self.description = description
        self.processorType = processorType
        self.hardDriveCapacity = hardDriveCapacity
        self.memory = memory
        self.operatingSystem = operatingSystem
        self.yearMade = yearMade 
        self.price = price

    # What methods will you need?

    """
    Function to print the attributes of a computer.
    """
    def printAttributes(self):
        print("Description:", self.description)
        print("Processor Type:", self.processorType)
        print("Hard Drive Capactity:", self.hardDriveCapacity)
        print("Memory:", self.memory)
        print("Operating System:", self.operatingSystem)
        print("Year Made:", self.yearMade)
        print("Price:", self.price)

