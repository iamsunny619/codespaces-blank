city = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

while len(city)>0:
    print(city[0])
    city.pop(0)  # Remove the first city from the list
    # This will continue until the list is empty