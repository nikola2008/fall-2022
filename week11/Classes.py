class Package: 
    def __init__(self, name):
        self.name = name 
    def dropOff(self, driver):
        print(f"Deliverd {self.name} by {driver}")

class AmazonTruck:
    packages = []
    driver = "Joe"


    def load(self, packages ):
        self.packages.append(packages) #add the package to the truck

    def deliver(self):
        for package in self.packages:
            package.dropOff(self.driver)

xbox = Package("xbox")
tshirt = Package("Tshirt")
blades = Package("Blades")

truck = AmazonTruck()
truckdriver = "Joe"
truck.load(xbox)
truck.load(tshirt)
truck.load(blades)

truck.deliver()
