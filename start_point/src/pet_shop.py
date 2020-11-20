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
# I've decided to use += instead of = because I feel that the function would be more
# useful this way. For example, if two cats are sold, I can just plug 2 without
# having to remember how many have been sold and then add two to that number.

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

#10
def find_pet_by_name(petshop_list, pet):
    for animal in petshop_list['pets']:
        if animal['name'] == pet:
            return animal



