
## import Abstract Base Class and abstractmethod
from abc import ABC, abstractmethod                 

## declare abstract class vehicle
class vehicle(ABC):
    def vehYear(self, year):                                ## method that prints the year
        print("Your vehicle is model year: ",year)

    @abstractmethod                                         ## declare abstract parent method vehWarranty for use later
    def vehWarranty(self, year):
        pass

class CheckWarrantyValid(vehicle):                          ## declare class for checking the vehicle warranty
    def vehWarranty(self, year):                            ## define the vehWarranty method
        if year > 2016:
            print("Your warranty is valid!")
        else:
            print("Your warranty is expired! Sorry!")

vehObj = CheckWarrantyValid()
vehObj.vehYear(2016)
vehObj.vehWarranty(2016)

vehObj.vehYear(2020)
vehObj.vehWarranty(2020)
        
            
