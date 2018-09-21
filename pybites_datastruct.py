cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    car_str = ", ".join(cars['Jeep'])
    return car_str

print(get_all_jeeps())


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    # return [models[0] for models in cars.values()]
    first = []
    for key in cars.keys():
        first.append(cars[key][0])
    return first

print(get_first_model_each_manufacturer())


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    car_trail = []
    for value in cars.values():
        for x in value:
            if grep.lower() in x.lower():
                car_trail.append(x)
    return sorted(car_trail)

print(get_all_matching_models())


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    for value in cars.values():
        value.sort()
    return cars
print(sort_car_models())