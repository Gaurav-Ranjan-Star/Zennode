#To Calculate Discount based on the given rules:
def best_discount_for_User(cart):
  max_discount=0
  discount_name=""

  #Rule 1: If cart total exceeds $200, apply a flat $10 discount on the cart total.
  if cart['Subtotal'] > 200:
    discount_amount=10
    if discount_amount > max_discount:
      max_discount=discount_amount
      discount_name = "flat_10_discount"

  #Rule 2:If the quantity of any single product exceeds 10 units, apply a 5% discount on that item's total price.
  for product in cart['Products']:
    if product['quantity'] > 10:
      discount_amount=product['total_price'] * 0.05;
      if discount_amount > max_discount:
        max_discount=discount_amount
        discount_name = "bulk_5_discount"


  #Rule 3: If total quantity exceeds 20 units, apply a 10% discount on the cart total.
  if cart['Total_Quantity'] > 20:
    discount_amount=cart['Subtotal'] * 0.10
    if discount_amount > max_discount:
        max_discount=discount_amount
        discount_name = "bulk_10_discount"


  #Rule 4: If total quantity exceeds 30 units & any single product quantity greater than 15,
           #then apply a 50% discount on products which are above  15 quantity. 
           #The first 15 quantities have the original price and units above 15 will get a 50% discount.

  if cart['Total_Quantity'] > 30:
    for product in cart['Products']:
      if product['quantity'] > 15:
        discount_amount =(product['quantity'] - 15) *product['price'] * 0.5
        if discount_amount > max_discount:
          max_discount=discount_amount
          discount_name = "tiered_50_discount"

  return discount_name,max_discount


#Function to calculate and display final receipt
def final_receipt():
  products={'Product A':20,'Product B':40,'Product C':50}
  cart={'Products':[],'Subtotal':0,'Total_Quantity':0}
  gift_wrap_fee=0

  #Input values for quantities and gift wrap 
  print("\n\n+-------------------------Input Area---------------------------+\n")
  for product,price in products.items():
    quantity=int(input(f"Enter the quantity of {product}:"))
    is_gift_wrapped = input(f"Is {product} wrapped as a gift ? (yes/no)    -> ").lower() == 'yes'

    total_price =quantity * price
    cart['Subtotal'] += total_price
    cart['Total_Quantity'] += quantity

    if is_gift_wrapped:
      #Gift Wrap Fee
      gift_wrap_fee += quantity

    cart['Products'].append({'name': product,'quantity':quantity,'price':price,'total_price':total_price})


    #Discount name and amount calculation
  discount_name,discount_amount = best_discount_for_User(cart)

    #Shipping Charge
    # This will converting value as ceil values.
    # Eg. 21 units ,each package contains 10 unit .Total package = 3
  shipping_fee = -(-(cart['Total_Quantity']) // 10) * 5

    #Total Amount
  total_amount = cart['Subtotal'] - discount_amount + gift_wrap_fee + shipping_fee


    #Display Final Result as following Guidelines:
  print("\n+----------------------------Final Receipt-------------------------------+")
  for product in cart['Products']:
    print(f"{product['name']} -> Quantity : {product['quantity']}, Total Amount : ${product['total_price']}")
    
  print(f"\nSubtotal : ${cart['Subtotal']}")
  print(f"\nDiscount Name applied : {discount_name} & Discount Amount : ${discount_amount}")

  print(f"\nShipping Fee : ${shipping_fee}  &  Gift Wrap Fee : ${gift_wrap_fee}")
  print(f"\nTotal : ${total_amount}")
  print(f"\n--------------------------------------------------------------------")

#Function Call
final_receipt()
