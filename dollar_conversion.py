dollars = eval(input("Enter the amount in dollars : "))

cent = dollars * 100

new_dollars = int(cent // 100)

cent = cent % 100 #cent - (new_dollars * 100)

quarters = int(cent // 25)

cent = cent % 25 #cent - (quarters * 25)

dime = int(cent // 10)

cent = cent % 10 #cent - (dime * 10)

nickel = int(cent // 5)

cent = cent % 5 #cent - (nickel * 5)

penny = int(cent)

print(dollars,"dollars, =", new_dollars, "dollars,", quarters,"quarters,", end = ' ')
print(dime, "dime,", nickel, "nickel, and", penny, "penny.")


