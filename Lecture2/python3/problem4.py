def middle_value(low, high):
    return int((low + high) / 2)

print('''
The rules are simple.  I guess a number and you
tell me if the number you are thinking is higher or
lower than the number I guessed.

If I guess correctly, simply enter correct.
''')

user_ans = ""
minimum = int(input("Smallest value: "))
maximum = int(input("Largest value: "))
# These lines are for people that try to break the logic
minimum = min(minimum, maximum)
maximum = max(minimum, maximum)

num_guesses = 0
while minimum <= maximum and user_ans != "correct":
        if user_ans == "higher":
            minimum = mid + 1
        elif user_ans == "lower":
            maximum = mid - 1
        num_guesses += 1
        mid = middle_value(minimum, maximum)
        if minimum > maximum:
            break
        print("\nIs your number " + str(mid))
        user_ans = input("Higher, Lower, or Correct: ").lower()
        
if minimum > maximum:
    print("CHEATER!!!")
else:
    print("Hooray, only " + str(num_guesses) + " guesses made.")