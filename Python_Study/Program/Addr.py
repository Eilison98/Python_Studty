class Contact:
      def __init__(self, name, phone_number, e_mail, addr):
          self.name = name
          self.phone_number = phone_number
          self.e_mail = e_mail
          self.addr = addr
 
      def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

def input_menu():
     print("1. Addr Input")
     print("2. Addr Print")
     print("3. Addr Del")
     print("4. Exit")
     menu = input("Menu Select: ")
     return int(menu)

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def main():
    contact_list = []
    while(1):
         menu = input_menu()
         if menu == 1:
             contact = set_contact()
             contact_list.append(contact)

         elif menu == 2:
             print_contact(contact_list)

         elif menu == 3:
             name = input("Name: ")
             delete_contact(contact_list, name)

         elif menu == 4:
             break

if __name__ == "__main__":
    main()
