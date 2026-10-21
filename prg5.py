Name= input("Enter student's name")
RNo= int(input("Enter the roll no."))
Age= int(input("Enter the age"))
Math= float(input("Enter marks of maths"))
Science=float(input("Enter marks of science"))
English=float(input("Enter marks of english"))
Total= Math+Science+English
Average= Total/3
Percentage= (Total/300)*100

print("Name:", Name)
print("Roll no.:", RNo)
print("Age:", Age)
print("Total:",Total,"/300")
print("Average:", Average)
print("Percentage:", Percentage,"%")