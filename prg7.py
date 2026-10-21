marks= int(input("Enter marks(0-100):"))
if marks>=0 and marks<=100:
    if marks>=40:
        print("PASS")
    else:
        print("FAIL")
else:
    print("Invalid marks range(0-100)")