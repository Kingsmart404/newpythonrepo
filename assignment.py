Custumers_name= str(input('Enter your name:'))
#actual_purchase_amount=int(input ('Amount:'))
purchase_amount = float(input('enter the amount: '))
if purchase_amount < 100 :
  print('Hello u have no discount')

elif purchase_amount == 100 :
 print ("Hello,Customer, You  have been giving 10%_discount")

elif purchase_amount > 500:
  purchase_amount == 500
  print ("Customer,You Just Got 20%_discount")

if purchase_amount < 100:
    discount = 0
    tax = 0.05 * purchase_amount 
    actual_purchase_amount= purchase_amount - discount + tax
elif purchase_amount < 500:
   discount = 0.1
   tax = 0.05 * purchase_amount 
   actual_purchase_amount= purchase_amount - discount + tax
elif purchase_amount > 500:
    discount = 0.2
actual_purchase_amount= purchase_amount - discount + tax

if discount < 200:
    tax = 0.05 * purchase_amount 
    actual_purchase_amount= purchase_amount - discount + tax
else:
    tax =  0.08 * purchase_amount 

actual_purchase_amount = purchase_amount - discount + tax
print (f'your discount amount:$ {discount}. ')
print(f'your tax is:$ {tax}. ')
print (f'amount to pay:$ {actual_purchase_amount}. ')
print ( 'thanks for shooping with us')