class VehicleCommon:
    TYPE_OF_VEHICLE = ''  # 'Land/Water/Air
    IS_PASSANGER = ''  # 'True/False'
    FUEL_TYPE = ''  # 'Carbon/Hydrogen/Electrical'
    LIGHTS_IS_ON = '' # 'True/False'

    def change_light(self, status):
        if self.LIGHTS_IS_ON == True:
            self.LIGHTS_IS_ON = False
            print('LIGHT STATUS :', 'OFF')
        else:
            self.LIGHTS_IS_ON = True
            print('LIGHT STATUS :', 'ON')


class VehicleLand(VehicleCommon):
    TYPE_OF_VEHICLE = 'Land'


class VehicleWater(VehicleCommon):
    TYPE_OF_VEHICLE = 'Water'


class VehicleAir(VehicleCommon):
    TYPE_OF_VEHICLE = 'Air'


truck1 = VehicleLand()
truck1.FUEL_TYPE = 'Carbon'
truck1.IS_PASSANGER = False

bus1 = VehicleLand()
bus1.FUEL_TYPE = 'Electrical'
bus1.IS_PASSANGER = True


tractor1 = VehicleLand()
bus1.FUEL_TYPE = 'Hydrogen'
bus1.IS_PASSANGER = False


tractor1.change_light(True)
