# WRITE YOUR FUNCTIONS HERE

#1
def get_pet_shop_name(shop):
    return shop ['name']

#2
def get_total_cash(petshop_list):
    return petshop_list['admin']['total_cash']

#3 & #4
def add_or_remove_cash(petshop_list, cash):
    petshop_list['admin']['total_cash'] += cash

#5
def get_pets_sold(petshop_list):
    return petshop_list['admin']['pets_sold']

#6
def increase_pets_sold(petshop_list, pet_sold):
    petshop_list['admin']['pets_sold'] += pet_sold

#7
def get_stock_count(petshop_list):
    return len(petshop_list['pets'])

#8 & #9
def get_pets_by_breed(petshop_list, breed):
    breed_counter = []
    for pet in petshop_list['pets']:
        if pet['breed'] == breed:
            breed_counter.append(breed)
    return breed_counter   

#10 #11
def find_pet_by_name(petshop_list, pet):
    for animal in petshop_list['pets']:
        if animal['name'] == pet:
            return animal

# Additional function for #22
def pet_exists(petshop_list, pet):
    for animal in petshop_list['pets']:
        if animal['name'] == pet:
            return True
    else:
        return False

#12
def remove_pet_by_name(petshop_list, pet):
    petshop_list['pets'].remove(find_pet_by_name(petshop_list, pet))

#13
def add_pet_to_stock (petshop_list, pet):
    petshop_list['pets'].append(pet)

#14
def get_customer_cash(customer_list_index):
    return customer_list_index['cash']

#15
def remove_customer_cash(customer_list_index, money_to_substract):
    customer_list_index['cash'] -= money_to_substract

#16
def get_customer_pet_count(customer_list_index):
    return len(customer_list_index['pets'])

#17
def add_pet_to_customer(customer_list_index, new_pet):
    customer_list_index['pets'].append(new_pet)

#18, #19 & #20
def customer_can_afford_pet(customer, pet):
    return customer['cash'] >= pet['price']

#21
#  this code does the following:
#  1. increase the customer pet count.
#  2. increase the sold pet count.
#  3. update the customer cash (deduct the pet cost).
#  4. update the pet shop cash (add the pet sale) (exercise 3)

def sell_pet_to_customer(petshop_list, pet, customer):
    if pet_exists == True:
        increase_pets_sold(petshop_list, 1)
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet['price'])
        add_or_remove_cash(petshop_list, pet['price'])





