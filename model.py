import json


phone_book ={}
path = 'phones.json'

def open_file():
    global phone_book
    try:
        with open(path, 'r',encoding='UTF-8') as file:
            phone_book = json.load(file)
        return True
    except:
        return False
        
def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii=False) 
        return True
    except:
        return False     

def search(word: str) -> dict[int:dict[str,str]]:
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact   
    return result

def chek_id():
    if phone_book:
        return max(list(map(int, phone_book)))+ 1   
    return 1
        
def add_contact(new: dict[int:dict[str,str]]):  
    contact = {chek_id(): new}
    phone_book.update(contact)  
    
def remove(index_del_contact):  
    phone_book.pop(index_del_contact)      
    
def change_contact(index_change, col_change, new_value):
    contact = phone_book.get(index_change)        
    contact[col_change] = new_value
    return contact
    
    