print("=" * 40)
print("       CALENDAR VERIFICATION SYSTEM")
print("=" * 40)
year = int(input("Enter year: "))
if year <= 0:
    print("Error: Year must be a positive integer.")

else:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
            reason = "Century year divisible by 400"
        else:
            leap_year = False
            reason = "Century year not divisible by 400"

    else:
        if year % 4 == 0:
            leap_year = True
            reason = "Divisible by 4 and not a century year"
        else:
            leap_year = False
            reason = "Not divisible by 4"
    if leap_year:
        status = "LEAP YEAR"
        days_in_year = 366
        days_in_february = 29
    else:
        status = "COMMON YEAR"
        days_in_year = 365
        days_in_february = 28
    print("-" * 40)
    print(f"Year: {year}")
    print(f"Status: {status}")
    print(f"Days in Year: {days_in_year} days")
    print(f"Days in February: {days_in_february} days")
    print(f"Reason: {reason}")
    print("-" * 40)
