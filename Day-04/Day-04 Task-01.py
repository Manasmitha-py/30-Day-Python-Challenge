#simple shopping bill 
item_name=input("Enter the name of the item: ")
price=int(input("Enter the price of the item: "))
quantity=int(input("Enter the quantity of item: "))
age=int(input("Enter your age: "))

print("\n-----BILL-----")
print("Item: ",item_name.upper())
print("Item: ",item_name.lower())
print("Price: ",price)
print("Quantity: ",quantity)

original_total= price*quantity
print("Oringinal Total: ",original_total)

if original_total>=1000:
    dis_amt=original_total * 20/100
elif original_total>=500:
    dis_amt=original_total * 10/100
else:
    dis_amt=0

price_after_dicount=original_total - dis_amt

if age < 18:
    age_dis=price_after_dicount - dis_amt
else:
    age_dis = 0

final_price=price_after_dicount - age_dis

print("Discount Amount:",dis_amt)
print("Age Discount:", age_dis)
print("Final Price:", final_price)

if age < 18:
    print("Customer: Minor")
else:
    print("Customer: Adult")
