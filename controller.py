import view
import model
import text

def start():
    while True:
       select = view.menu()
       match select:
           case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)        
           case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save) 
           case 3:
              view.show_contacts(model.phone_book, text.empty_book)
           case 4:
               new = view.add_contact()
               model.add_contact(new)
               view.print_message(text.add_successful(new.get('name')))
           case 5:
               word = view.search_word()
               result = model.search(word)
               view.show_contacts(result, text.empty_search)
           case 6:
               word = view.search_word()
               result = model.search(word)
               view.show_contacts(result, text.empty_search)
               ind_change = view.search_index(text.search_ind)
               col_change = view.search_index(text.search_col)
               new_value = view.change_contact(col_change)
               change_contact = model.change_contact(ind_change, col_change, new_value)
               view.print_message(text.change_successful(change_contact))
           case 7:
               word = view.search_word()
               result = model.search(word)
               view.show_contacts(result, text.empty_search)
               ind_del = view.search_index(text.search_index)
               model.remove(ind_del)
           case 8:
               view.print_message(text.end_programm)
               break
