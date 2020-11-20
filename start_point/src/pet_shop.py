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

