states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])

stations ={}
stations['kone'] = set(["id","nv","ut"])
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])

station_list =['kone','ktwo','kthree','kfour','kfive']
useful_stations = []
best_station = ""
rabbit = ""
number_of_states_serviced = 0
temp_states_serviced = [] 
states_serviced = []



while states_needed != set([]):
    number_of_states_serviced = 0
    for station in station_list:    
        if len(stations[station] & states_needed) > number_of_states_serviced:
            number_of_states_serviced = len(stations[station] & states_needed)
            
            rabbit = station
    useful_stations.append(rabbit)
    temp_states_serviced = stations[rabbit] & states_needed
    station_list.remove(rabbit)
    
    for state in temp_states_serviced:
        states_needed.remove(state)
        states_serviced.append(state)

print(useful_stations)


      
