birth_year= int(input("Enter the Birth year"))
height= int(input("Enter the height(in cm)"))
VIP_pass= input("Enter if have VIP pass (Type 1 for Yes, 0 for No)")
current_year= 2026
Age= current_year - birth_year
height_in_metres= height/100
can_enter= Age>=12
needs_child_ticket= 12 <= Age >= 17
needs_adult_ticket= Age>=18
can_ride_water_slide= height_in_metres>=1.4
gets_vip_access= VIP_pass == 1
print("------- Visitor Profile ------")
print("Age:", Age)
print("Height(metres):", height_in_metres)
print("------ Access Rules ------")
print("Can enter park:", can_enter)
print("Needs child ticket:", needs_child_ticket)
print("Needs Adult Ticket:", needs_adult_ticket)
print("Can ride water slide:", can_ride_water_slide)
print("Gets VIP access:", gets_vip_access)

