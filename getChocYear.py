<<<<<<< HEAD
chocolates = {
    "first":1800,
    "second":1950,
    "third": 2010
    }
for choc in chocolates:
    print(f"{choc.capitalize()} {chocolates[choc]}")

choice = input("Please type the chocolate you want:\n").lower()
if choice in chocolates:
=======
chocolates = {
    "first":1800,
    "second":1950,
    "third": 2010
    }
for choc in chocolates:
    print(f"{choc.capitalize()} {chocolates[choc]}")

choice = input("Please type the chocolate you want:\n").lower()
if choice in chocolates:
>>>>>>> f1cf4a07c260a26ff3083f30cf20e94bd318a501
    print(chocolates[choice])