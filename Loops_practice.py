##x = 0
#hile x <= 5:
#    print(x)
#    x = x + 1

#counties = ["Arapahoe","Denver","Jefferson"]
#for county in counties:
#    print(county)

counties_dict = {"Arapahoe": 422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)

print(counties_dict.keys())
for county in counties_dict.keys():
    print(county)