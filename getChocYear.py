chocolates = {
    "first":1800,
    "second":1950,
    "third": 2010
    }
for choc in chocolates:
    print(f"{choc.capitalize()} {chocolates[choc]}")

choice = input("Please type the chocolate you want:\n").lower()
if choice in chocolates:
    print(chocolates[choice])