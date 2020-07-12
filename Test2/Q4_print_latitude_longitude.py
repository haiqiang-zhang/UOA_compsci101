def print_latitude_longitude(city_name, city_lat_lng_dictionary):
    result = city_lat_lng_dictionary[city_name.lower()]
    print("The latitude-longitude of ", city_name.upper(), " is ", result, ".", sep="")
    return







cities = {'shanghai': (31.2165, 121.4365), 'beijing': (39.928, 116.3883), 'seoul': (37.5663, 126.9997),'adelaide': (-34.935, 138.6), 'newcastle': (-32.8453, 151.815), 'christchurch': (-43.535, 172.63),'hamilton': (-37.7783, 175.2896), 'auckland': (-36.8481, 174.763)}
city_name = 'beijing'
print_latitude_longitude(city_name, cities)