print("Hello World")

voting_data = []
voting_data.append({"county":"Arapahoe","registered_votes": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_votes": 432438})
print(voting_data)
voting_data.append({"county": "El Paso", "registered_votes": 461149})
print(voting_data)
auxitem = voting_data.pop(0)
print(voting_data)
auxDenver = voting_data.pop(0)
auxJeff = voting_data.pop(0)
voting_data.append(auxJeff)
voting_data.append(auxDenver) #make Denver the tird item and Jefferson is still the second item
print(voting_data)
voting_data.append(auxitem)  #add Arapahoe
print(voting_data)

##

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

##

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties")
