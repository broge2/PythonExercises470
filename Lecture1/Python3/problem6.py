alphabet = list("abcdefghijklmnopqrstuvwxyz")

user_in = input("Type something: ").replace(" ", "").lower()

user_in = set(user_in)

user_in = sorted(list(user_in))
print(user_in == alphabet)

