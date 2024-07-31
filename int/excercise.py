freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}


cart = {}
#loop through stores/dicts
# for LOOP OVER THE SHOPS :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lofor LOOP OVER THE SHOPS :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {SHOPNAME}! what do you want to buy: {LIST ITEMS FOR SALE})
#     #update the cart
#     cart.update({insert KEYVAL:VALUE}) # use pop...
# print(f'You Purchased {ITEMS PUCHASED} Today it is all free. Have a nice day of mayhem!')wercase
#     buy_item = input(f'Welcome to {SHOPNAME}! what do you want to buy: {LIST ITEMS FOR SALE})
#     #update the cart
#     cart.update({insert KEYVAL:VALUE}) # use pop...
# print(f'You Purchased {ITEMS PUCHASED} Today it is all free. Have a nice day of mayhem!')
purse = 1000
for shop in (freelancers,antiques,pet_shop):
    buy_item = input(f'Welcome to {shop['name']} what do you want to buy: {shop}').lower()
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue
    cart.update({buy_item:shop.pop(buy_item)})

    buy_items = ', '.join(list(cart.keys()))
    total_sum = sum(cart.values())
print(f'You Purchased {buy_items} Your Total is {total_sum} gp. your change is {purse-total_sum}gp. Have a nice day of mayhem!')