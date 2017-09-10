year = input("Enter any year to check leap  ")
if year % 4 == 0:
    print  "Year is Leap"
else:
    print "Year is not Leap"



a = input("Enter any Number ")
if a >= 0:
    print("The Number is positive")
else:
    print("Entered number is negative")

    """Lets Check something else """
    print("\n" )
# Nested ifElse statement
a=10
if a>=20:
    print "Condition is True"
else:
    if a>=15:
        print "Checking second value"
    else:
        print "All Conditions are false"