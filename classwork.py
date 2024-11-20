Custumers_name= str(input('Enter your name:'))
purchase_amount = float(input('enter the amount: '))
print(f'Origninal purchase Amount:{purchase_amount}')

if purchase_amount < 100:
    discount=0
    print('Hello u have no discount')
elif purchase_amount <=500:
     discount=0.1 * purchase_amount
     print(f'discount of 10%:{discount:.2f}')
elif purchase_amount > 500:
        discount=0.2 * purchase_amount
        print(f'Discount of 20%:${discount:.2f}')

discounted_amount = purchase_amount - discount

print(f'Discounted amount: ${discounted_amount:.3f}')
if discounted_amount < 200:
      tax = discounted_amount * 0.05
      print(f'tax for discount less than $200{tax:.2f}')
else:
      tax= discounted_amount * 0.08
      print(f'tax for discount above $200:.{tax:.2f}')

      final_amount = discounted_amount + tax
      print(f'final amount:${final_amount:.2f}')

    
