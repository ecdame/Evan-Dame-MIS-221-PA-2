def menu():
    print("\n\nMain Menu")
    print("Options:\n1: Inventory Check\n2: Transaction Calculator\n3: Exit")

    entry = input("Please make selection: ")
    entry = sel_check(entry, "menu")

    match entry:
        case "inventory check":
            inv_check()
        case "transaction calculator":
            trans_calc()
        case "exit":
            print("Have a nice day!")
            return
        
def inv_check():
    print("\n\nInventory Check")
    gals_left = input("\nPlease enter gallons of milk left in fridge or return to go back to main menu: ")
    gals_left = quant_check(gals_left, "float")
    if gals_left == "return":
        menu()
        return

    lattes_expected = input("\nPlease enter expected quantity of lattes ordered today or return to go back to main menu: ")
    lattes_expected = quant_check(lattes_expected, "int")
    if lattes_expected == "return":
        menu()
        return

    gals_left_expected = gals_left - (.1*lattes_expected)

    if gals_left_expected < 0:
        print(f"\nYou need to buy {.1*lattes_expected-gals_left} gallons of milk to meet expected latte demand.")
    elif gals_left_expected > 0:
        print(f"\nWith the expected latte demand, you will have {gals_left_expected} gallons of milk left.")
    else:
        print("\nYou have the exact amount of milk necessary to meet expected latte demand.")

    menu()

def trans_calc():
    print("\n\nTransaction Calculator")
    print("Drink Options:\n1: Standard Drip\n2: Specialty Cold Brew")

##Gets drink order, validates it, and returns to menu if customer enters "return"
    drink_ordered = input("Please enter drink selection or enter return to go back to main menu: ")
    drink_ordered = sel_check(drink_ordered, "drinks")
    if drink_ordered == "return":
        menu()
        return

##Gets order quantity, validates it, and returns to menu if customer enters "return"
    quantity_ordered = input("Please enter quantity ordered: ")
    quantity_ordered = quant_check(quantity_ordered, "int")
    
    if quantity_ordered == "return":
        menu()
        return

    match drink_ordered:
        case "standard drip":
            total_cost = quantity_ordered * 3
        case "specialty cold brew":
            total_cost = quantity_ordered * 6
    
    if quantity_ordered >= 10:
        total_cost = total_cost * .85

    print("Would you like to Pastry Bundle for $5 extra?")
    bundle = input("Enter yes or no, or return to go back to main menu: ")
    bundle = sel_check(bundle, "yes_no")

    if bundle == "yes":
        total_cost += 5
    elif bundle == "return":
        menu()
        return
    
    total_cost = total_cost * 1.1

    while total_cost > 0:
        print(f"Balance remaining: ${total_cost:.2f}")

        payment = input("Please enter payment, or return to cancel order: $")
        payment = quant_check(payment, "float")

        if payment == "return":
            print("\nOrder canceled")
            menu()
            return

        total_cost = round(total_cost - payment, 2)
    
    print(f"Balance remaining: ${total_cost:.2f}")
    
    if total_cost < 0:
        print(f"Change due: ${(total_cost * -1):.2f}")


    menu()
 
#quant_check ensures that the user enters a proper quantity when prompted. If entry valid, it returns entry. If not, it reprompts user.
def quant_check(entry, int_or_float):

    entry = entry.lower().strip()
    if entry == "return":
        return entry

    match int_or_float:
        case "int":
            try:
                entry = int(entry)
                if entry >= 0:
                    return entry
                else:
                    entry = input("Please enter a valid quantity: ")
                    return quant_check(entry, "int")
            except ValueError:
                entry = input("Please enter a valid quantity: ")
                return quant_check(entry, "int")
        case "float":
            try:
                entry = float(entry)
                if entry >= 0:
                    return entry
                else:
                    entry = input("Please enter a valid quantity: ")
                    return quant_check(entry, "float")
            except ValueError:
                entry = input("Please enter a valid quantity: ")
                return quant_check(entry, "float")
            
##sel_check checks for valid selections in the three selection prompts of this program. If selections are not valid, it reprompts user.
def sel_check(entry, phase):
    entry = entry.lower().strip()

    match phase:
        case "menu":
            if entry in ("inventory check", "transaction calculator", "exit"):
                return entry
            else:
                entry = input("Please make a valid selection: ")
                return sel_check(entry, "menu")
        case "drinks":
            if entry in ("specialty cold brew", "standard drip", "return"):
                return entry
            else:
                entry = input("Please make a valid selection: ")
                return sel_check(entry, "drinks")
        case "yes_no":
            if entry in ("yes", "no", "return"):
                return entry
            else:
                entry = input("Please make a valid selection: ")
                return sel_check(entry, "yes_no")

##Main program
print("\n\nWelcome to Katelyn's Coffee Shop Processing Application.")
print("Guide:\nThis program allows you to perform inventory checks and transaction calculations for Katelyn's Coffee Shop.\nWhen prompted for a selection based input, please enter the name of the selection. When prompted for a quantity, please enter a valid quantity.")
menu()