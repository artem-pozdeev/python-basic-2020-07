from abc import ABCMeta, abstractmethod
import error_handlers

class VehicleCommon(metaclass=ABCMeta):
    WEIGHT = 0
    PAYLOAD_CAPACITY = 0
    FUEL_CAPACITY = 0
    MAX_DISTANCE = 0
    FUEL_CONSUMPTION = 0
    REG_NUMBER = ""

    def __init__(self, *args):
        self.REG_NUMBER = args[0]

    def __repr__(self):
        print(f"{self.REG_NUMBER} have ", self.FUEL_CAPACITY )

    def __str__(self):
        # return f"{self.__class__.__name__}(WEIGHT={self.WEIGHT}, PAYLOAD_CAPACITY={self.PAYLOAD_CAPACITY})"
        return f"subclass {self.__class__.__name__} object # {self.REG_NUMBER} initiated"

    @abstractmethod
    def make_a_sound(self) -> str:
        raise NotImplementedError
        # print(self, 'now making sound')

    def drive_a_distance(self):
        pass


class VehicleCar(VehicleCommon):
    FUEL_CAPACITY = 60
    MAX_DISTANCE = 400
    WHEELS_QUANTITY = 4

    def make_a_sound(self):
        print("car #", self.REG_NUMBER, "making sound")

    def drive_a_distance(self):
        # raise error_handlers.MyZeroDivisionError({self.REG_NUMBER}, "fuel capacity")
        try:
            self.FUEL_CONSUMPTION = self.FUEL_CAPACITY / self.MAX_DISTANCE
        except ZeroDivisionError:
            print('max distance = 0!!!')

        print(f"{self.__class__.__name__} reg.number {self.REG_NUMBER} have")
        print(f"---------------------- FUEL CAPACITY {self.FUEL_CAPACITY}")
        print(f"---------------------- MAX DISTANCE {self.MAX_DISTANCE}")
        print(f"---------------------- FUEL CONSUMPTION {self.FUEL_CONSUMPTION} Can go : ....")
        print(f"---------------------- Can drive : ....")



    def get_vehicle_status(self):
        pass


class VehicleShip(VehicleCommon):
    WEIGHT = 200000
    PAYLOAD_CAPACITY = 150000
    DISTANCE_TO_DRIVE = 15000
    FUEL_CAPACITY = 6000
    DISPLACEMENT = 50000

    def get_vehicle_status(self):
        pass

    def make_a_sound(self):
        print("ship #", self.REG_NUMBER, "making sound")

    def drive_a_distance(self):
        pass


class VehiclePlain(VehicleCommon):
    WEIGHT = 50000
    PAYLOAD_CAPACITY = 20000
    DISTANCE_TO_DRIVE = 5000
    FUEL_CAPACITY = 1500
    ALLOWED_ALTITUDE = 10000

    def get_vehicle_status(self):
        pass

    def make_a_sound(self) -> str:
        print("plain #", self.REG_NUMBER, "making sound")

    def drive_a_distance(self):
        pass

class passanger_car(VehicleCar):
    pass