user_in = raw_input("Type something: ")
print user_in[0] + user_in[1:].replace(user_in[0], "@")
