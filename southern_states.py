#Program:       southern_states.py
#Programmer:    Lorenzo Openito
#Date:           07/082024
#Description:   Python lists
###################################################

#create a list
southern_states =['virginia', "tennessee", "arkansas", "louisiana", 
                  "north carolina", "south carolina", "mississippi",
                  "alabama", "georgia", "florida", "texas"
                  ]

#print name of report
print("Report - Southern United States\n")

#show list unsorted
print("UNSORTED:\n")
print(f"{southern_states[0].title()}") 
print(f"{southern_states[1].title()}") 
print(f"{southern_states[2].title()}") 
print(f"{southern_states[3].title()}") 
print(f"{southern_states[4].title()}") 
print(f"{southern_states[5].title()}") 
print(f"{southern_states[6].title()}") 
print(f"{southern_states[7].title()}") 
print(f"{southern_states[8].title()}") 
print(f"{southern_states[9].title()}") 
print(f"{southern_states[10].title()}") 


#use meg index value to access last element in list
print(f"\nLast state on this unsorted list: {southern_states[-1].title()}\n")

# sort the list
sorted_southern_states = sorted(southern_states)

# show list sorted
print("SORTED:\n")
print(f"{sorted_southern_states[0].title()}")
print(f"{sorted_southern_states[1].title()}")
print(f"{sorted_southern_states[2].title()}")
print(f"{sorted_southern_states[3].title()}")
print(f"{sorted_southern_states[4].title()}")
print(f"{sorted_southern_states[5].title()}")
print(f"{sorted_southern_states[6].title()}")
print(f"{sorted_southern_states[7].title()}")
print(f"{sorted_southern_states[8].title()}")
print(f"{sorted_southern_states[9].title()}")
print(f"{sorted_southern_states[10].title()}")

print(f"\nLast state on this ordered list: {sorted_southern_states[-1].title()}\n")

#show length of list
print(f"\nSource: simple.wikipedia.org/wiki/Southern_United_States")

