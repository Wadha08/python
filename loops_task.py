
item =  input("item (enter \"done\" when finished): ")
dirc = {}
items=[]
while item != "done":
 
 price = input("price: ")
 quantity = input("quantity: ")
 dirc.update({'item':item})
 dirc.update({'price':price})
 dirc.update({'quantity':quantity})
 dirc2 =dirc.copy()
 items.append(dirc2) 
 item =  input("item (enter \"done\" when finished): ")
 

#print(items) 
print("-------------------")
print("receipt")
print("-------------------")

total =0
for i in items:
 
 price_item = float(i['price'])*float(i['quantity'])
 print(i['quantity']+" "+i['item']+""+" %.3fKD"%float(price_item))
 total =total +price_item
print("-------------------")
print("Total: %.3f"%float(total))





	

