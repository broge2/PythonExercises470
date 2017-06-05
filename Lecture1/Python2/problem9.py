phonebook = {"Friend One":"555-1234", 
             "Friend Two":"555-1235", 
	     "Friend Three":"555-1236"}

friend = raw_input("Who would you like to call: ")
print phonebook.get(friend, "Does not exist")
