contact_information = []

def contact_add(add):
    try:
        name, phnumber = add.split()
        contact_information.append([name, phnumber])
    except ValueError:
        print("please write contact in valid format")

def contact_view():
    if not contact_information:
        print("list is empty..")
    for i, todo in enumerate(contact_information, start=1):
        name, phnumber =todo
        print(f"{i}. Name: {name} and phone number is {phnumber}")    

def contact_delete(contact_number):
    try:
        del contact_information[contact_number - 1]
    except IndexError:
        print("wrong index...")       

def contact_search(search):
    found_contact = []
    for todo in contact_information:
        name, phnumber = todo
        if search in name:
            found_contact.append(todo)
    if todo:
        for i, todo in enumerate(found_contact, start=1):
            name, phnumber = todo
            print(f"{i}. Name: {name}, PhoneNumber: {phnumber}")
    else:
        print("sorry no contact found with this name.")
        
def contact_update():
    search_name = input("Enter the name of person for updation: ")
    update_contact = None
    for todo in contact_information:
        name, phnumber = todo
        if search_name in name:
            update_contact = todo
            break
    if update_contact:
        print("Enter the updated details:")
        name = input("Enter the updated name: ")
        phnumber = input("Enter the Updated Phone Number: ")
        index = contact_information.index(update_contact)
        contact_information[index] = [name, phnumber]
        print("Contact list succesfully updated.")
      
    else:
        print("Contact list not found..")    

while True:
    print("1. create contact..")
    print("2. View contact..")
    print("3. Delete Contact..")
    print("4. Contact search...")
    print("5. contact update..")
    print("6. for quit contact app..")
    choice = input("enter the number of task: ")
    
    if choice == "1":
        add = input("Enter the details of contact(Name, Phone Number): ")
        contact_add(add)
    elif choice == "2":
        contact_view()
    elif choice == "3":
        contact_number = int(input("enter the index of contact you want to delete(index starts = 1): "))
        contact_delete(contact_number)
    elif choice == "4":
        search = input("Enter the name of contact you are looking for: ")
        contact_search(search)
    elif choice == "5":
        contact_update()
    elif choice == "6":
        break
    else:
        print("Wrong choice please choose correct option.")  
            
        