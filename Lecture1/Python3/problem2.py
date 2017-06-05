price = float(eval(input("Price: ")))
tip_percent = float(eval(input("Tip %")))

tip_percent = tip_percent / 100

final_price = price + (price * tip_percent)
print("Pay " + str(final_price))
