print("="* 40)
print("    CALENDER VERIFICATION SYSTEM")
print("="* 40)

year= int(input("Enter year:"))
if year <= 0:
    print("Error: Please enter a positive year.")
else:
    if year % 100 == 0:
        if year % 400 == 0:
          leap = True
          reason = "Century year divisible by 400"
        else:
          leap = False
          reason = "Century year not divisible by 400"
    elif year % 4 == 0:
       leap = True
       reason = "Divisible by 4 and not a century year"
    else:
       leap = False
       reason = "Not divisible by 4"
    if leap:
       days = 366
       february = 29
       status = "LEAP YEAR"
    else:
       days = 365
       february = 28
       status = "COMMON YEAR"

    print("Year:", year)
    print('Status:', status)
    print("Days in Year:", days, "days")
    print("Days in February", february, "days")
    print("Reason:", reason)

        