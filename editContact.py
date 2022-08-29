def editContact(contacts):
    while True:
        print("Which contact would you like to edit?")
        print(contacts.keys())
        edit = input()
        if edit == contacts.keys():
            print(f"Please enter the updated phone number for {contacts.keys}:" + "\n")
            contacts.update = input()
        else:
            break


            # editContactName = str(input("Which contact would you like to edit?" + "\n"))
    # newContactNumber = str(input(f"Please enter the telephone number for {newContactName}:" + "\n"))

    # contacts.update({editContactName: newContactNumber})

    # updatedList = contacts + {[newContactName] + [newContactNumber]}

    return contacts


# print all contacts
# ask for which contact the user wants to edit
# user inputs name - get
# ask for updated phone number - Please enter the updated phone number for [name]."
# print updated record with name and new phone - "[name]'s phone number has been updated to..."

    # catNames = []
    # while True:
    #     print('Enter the name of cat ' + str(len(catNames) + 1) +
    #           ' (Or enter nothing to stop.):')
    #     name = input()
    #     if name == '':
    #         break
    #     catNames = catNames + [name]  # list concatenation
    # print('The cat names are:')
    # for name in catNames:
    #     print('  ' + name)
