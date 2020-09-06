import vehicles

# basic classes demo
print('Base classes demo starting: init')
vehicles_type_list = ('car', 'ship', 'plain', 'spaceship', 'bike', 'skateboard')
max_vehicles_of_single_type = 2
vehicles_list = list()
for current_vehicle_type in vehicles_type_list:

    for vehicles_counter in range(max_vehicles_of_single_type):

        if current_vehicle_type == 'car':
            ve = vehicles.VehicleCar(vehicles_counter)
            ve.WHEELS_QUANTITY = ve.WHEELS_QUANTITY + vehicles_counter * 2
            ve.FUEL_CAPACITY = vehicles_counter * 50
            ve.MAX_DISTANCE = vehicles_counter * 100
        elif current_vehicle_type == 'ship':
            ve = vehicles.VehicleShip(vehicles_counter)
        elif current_vehicle_type == 'plain':
            ve = vehicles.VehiclePlain(vehicles_counter)
        else:
            print(current_vehicle_type,'not supported')
            continue

        vehicles_list.append(ve)
        print(ve)

print('Base classes demo starting: actions')
for i in vehicles_list:
    i.make_a_sound()
    i.drive_a_distance()

