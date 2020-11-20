# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return shop ['name']

def get_total_cash(petshop_list):
    return petshop_list['admin']['total_cash']

def add_or_remove_cash(petshop_list, cash):
    petshop_list['admin']['total_cash'] += cash