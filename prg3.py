t_fee= int(input("Enter the tution fee"))
e_fee= int(input("Enter the exam fee"))
lib_fee= int(input("Enter the library fee"))
dis= int(input("Enter the discout"))
sem_fee=t_fee+e_fee+lib_fee
aftersem_fee= sem_fee-dis
print(aftersem_fee)
annual= aftersem_fee*2
print(annual)
