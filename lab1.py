tuition_fee = float(input("Enter Tuition Fee: "))
lab_fee = float(input("Enter Lab Fee: "))
library_fee = float(input("Enter Library Fee: "))
exam_fee = float(input("Enter Exam Fee: "))
discount_amount = float(input("Enter Discount Amount: "))
total_fee = tuition_fee + lab_fee + library_fee + exam_fee
fee_after_discount = total_fee - discount_amount
annual_fee = fee_after_discount * 2
monthly_installment = annual_fee / 12
print("\nTuition Fee:", tuition_fee)
print("Lab Fee:", lab_fee)
print("Library Fee:", library_fee)
print("Exam Fee:", exam_fee)
print("Total Fee:", total_fee)
print("Discount:", discount_amount)
print("Fee after Discount:", fee_after_discount)
print("Annual Fee:", annual_fee)
print("Monthly Installment:", round(monthly_installment, 2))
