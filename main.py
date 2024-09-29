# Creating a currency converter using Python
currency = input("Enter any of these currency in english ($ ₦ €): ")
amount = float(input("Enter amount: "))
new_currency = input("Enter the currency you want to change the previous currency to:  ($ € ₦) ")

if currency == "dollar" and new_currency == "naira":
    amount = amount * 1600
    print(f"The amount in naira is {amount:.2f}")
elif currency == "dollar" and new_currency == "euro":
    amount = amount / 0.90
    print(f"The amount in euro is: {amount:.2f}")


if currency == "euro" and new_currency == "naira":
    amount = amount * 1861.73
    print(f"The amount in naira is: {amount:.2f}")
elif currency == "euro" and new_currency == "dollar":
    amount = amount * 0.90
    print(f"The amount in dollar is:: {amount:.2f}")

if currency == "naira" and new_currency == "dollar":
    amount = amount / 1600
    print(f"The amount in dollars is: {amount:.2f} ")
elif currency == "naira" and new_currency == "euro":
    amount = amount / 1861.73
    print(f"The amount in euro is: {amount:.2f}")

elif currency == "dollar" and new_currency == "":
    print(f"No currency target selected")

elif currency == "naira" and new_currency == "":
    print(f"No currency target selected")

elif currency == "euro" and not new_currency == "naira":
    print(f"No currency target selected")

elif currency == "euro" and not new_currency == "dollaar":
    print(f"No currency target selected")

elif currency == "dollar" and not new_currency == "naira":
    print(f"No currency target selected")

elif currency == "dollar" and new_currency == "euro":
    print(f"No currency target selected")

elif currency == "naira" and not new_currency == "dollar":
    print(f"No currency target selected")

elif currency == "naira" and not new_currency == "euro":
    print(f"No currency target selected")



