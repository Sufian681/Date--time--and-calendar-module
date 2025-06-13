def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Jakarta":
        return 1045
    elif city == "Paris":
        return  1375 
    elif city == "New York":
        return 1375
    elif city == "Tokyo":
        return 875
    
    
def rental_car_cost(days):
    
    if days >= 7:
        return (40*days) - 50
    elif days >= 3:
        return (40*days) - 20
    else:
        return (40*days)
    
def trip_cost(city, days):
    
    h_c = hotel_cost(days)
    r_c = rental_car_cost(days)
    p_c = plane_ride_cost(city)
    
    sum = h_c + r_c + p_c
    return sum

d = int(input("Enter the number of days you will stay (in digit): "))
c = input("Enter the city you will visit [Jakarta, Paris, New York, Tokyo]: ")

print()
print(f"Hotel cost: ${hotel_cost(d)}")
print(f"Car cost: ${rental_car_cost(d)}")
print(f"Plane cost: ${plane_ride_cost(c)}")
print(f"Total cost: ${trip_cost(c,d)}")

