from unicodedata import name
from sqlalchemy import false, true


inventory = {}
orders = {}
# order = {}
# orderline = {}

def add_product(name, quantity):
    inventory.update({name: quantity})

# add_product("a", 5)
# add_product("b", 6)
# add_product("c", 7)
# print(inventory)

def show_inventory():
    print("The products available in the inventory are as follows: ")
    for i in inventory:
        print(i, " -> ", inventory[i])

# show_inventory()

def create_order():
    order_id = len(orders) + 1
    orders.update({order_id: []})
    print("Order created with order id: ", order_id)

# create_order()

def count_status(array):
    draft = 0
    booked = 0
    cancelled = 0
    for order_l in array:
        if(order_l["status"] == "draft"):
            draft += 1

        elif(order_l["status"] == "booked"):
            booked += 1

        elif(order_l["status"] == "cancelled"):
            cancelled += 1

    return [draft, booked, cancelled]


def show_order(id):
    if(id > len(orders)):
        print("Order id doesn't exist")
        return

    stat = count_status(orders[id])
    print("Order: ", id)
    print("DRAFT: ", stat[0], "\nBOOKED: ", stat[1], "\nCANCELLED: ", stat[2])
    for i in orders[id]:
        print(i["name"], " -> ", i["quantity"], " -> ", i["status"])

def show_all_orders():
    for i in range(len(orders)):
        show_order(i+1)
        print()

def order_status(id):
    if(id > len(orders)):
        print("Order id doesn't exist")
        return

    stat = count_status(orders[id])

    if(stat[1] == 0 and stat[2] == 0):
        return "DRAFT"

    elif(stat[0] == 0 and stat[1] >= 1):
        return "BOOKED"

    elif(stat[0] == 0 and stat[1] == 0 and stat[2] >= 1):
        return "CANCELLED"
    

def add_order_line(id, name, quantity):
    # print(quantity)
    if(id > len(orders)):
        print("Order id doesn't exist")
        return

    if(inventory[name] >= quantity):
        order_line = {
            "name": name,
            "quantity": quantity,
            "status": "draft"
        }

        orders[id].append(order_line)

        print(quantity, " ", name, " added to order ", id)

    else:
        print("The ", name, " is not available in the demanded quantity")

# add_order_line(1, "a", 5)
# add_order_line(1, "b", 7)
# add_order_line(2, "a", 5)
# print(orders)
# show_all_orders()

    
def is_orderline_bookable(line):
    p_name = line["name"]
    p_quant = line["quantity"]
    p_status = line["status"]
    if(inventory[p_name] <= p_quant):
        print("Quantity not available")

    if(inventory[p_name] <= p_quant and p_status == "draft"):
        return true

def is_bookable(id):
    if(id > len(orders)):
        print("Order id doesn't exist")
        return

    curr_order = orders[id]
    sts = count_status(curr_order)
    if(sts[0] >= 1):
        for i in curr_order:
            if( is_orderline_bookable(i) == false):
                return false

        return true

    else:
        return false


def book_o_line(id, p_name):
    print(p_name)
    if(id > len(orders)):
        print("Order id doesn't exist")
        return

    
    for i in range(len(orders[id])):
        t = orders[id][i]
        if(t["name"] == p_name):
            if(orders[id][i]["status"] == "draft"):
                orders[id][i]["status"] = "booked"
                # print(inventory[orders[id][t]["name"]])
                inventory[orders[id][i]["name"]] = inventory[orders[id][i]["name"]] - orders[id][i]["quantity"]

    # print("t: ", t)
    # print(orders[id][t]["status"])

    

def cancel_o_line(id, p_name):
    if(id > len(orders)):
        print("Order id doesn't exist")
        return

    # t = -1
    for i in range(len(orders[id])):
        t = orders[id][i]
        if(t["name"] == p_name):
            if(orders[id][i]["status"] == "booked"):
                orders[id][i]["status"] = "cancelled"
                # print(inventory[orders[id][t]["name"]])
                inventory[orders[id][i]["name"]] = inventory[orders[id][i]["name"]] + orders[id][i]["quantity"]

    # if(orders[id][t]["status"] == ""):
    #     orders[id][t]["status"] = ""
    #     inventory[orders[id][t]["name"]] = inventory[orders[id][t]["name"]] + orders[id][t]["quantity"]
        

def book_order(id):
    if(id > len(orders)):
        print("Order id doesn't exist")
        return

    if(is_bookable(id)):
        for i in orders[id]:
            # print("Orders: ", orders[id])
            book_o_line(id, i["name"])


def cancel_order(id):
    if(id > len(orders)):
        print("Order id doesn't exist")
        return

    sts = count_status(orders[id])
    if(sts[1] >= 1):
        for i in orders[id]:
            cancel_o_line(id, i["name"])
    else:
        print("Order can not be cancelled")


    

print("\nBuild Inventory: ")
p_nos = int(input())
while(p_nos > 0):
    n, q = input().split()
    add_product(n, int(q))
    p_nos -= 1

print()
print("1. CREATE_ORDER")
print("2. ADD_PRODUCT_ORDER [ORDER_ID] [PRODUCT_NAME] [PRODUCT_QUANTITY]")
print("3. SHOW_INVENTORY")
print("4. SHOW_ORDER [ORDER_ID]")
print("5. SHOW_ORDERS")
print("6. IS_ORDER_BOOKABLE [ORDER_ID]")
print("7. BOOK_ORDER [ORDER_ID]")
print("8. CANCEL_ORDER [ORDER_ID]")
print("9. CANCEL_ORDER_LINE [ORDER_ID] [PRODUCT_NAME]")
print("10. EXIT")
print()

print("\nEnter any of the above command(CASE SENSITIVE): ")
while(true):
    cmds = input().split()
    cmd = cmds[0]
    # print(cmds)
    if(cmd == "CREATE_ORDER"):
        create_order()
        print()

    elif(cmd == "SHOW_INVENTORY"):
        show_inventory()
        print()

    elif(cmd == "SHOW_ORDERS"):
        show_all_orders()
        print()

    elif(cmd == "SHOW_ORDER"):
        show_order(int(cmds[1]))
        print()

    elif(cmd == "ADD_PRODUCT_ORDER"):
        add_order_line(int(cmds[1]), str(cmds[2]), int(cmds[3]))
        print()

    elif(cmd == "IS_ORDER_BOOKABLE"):
        if(is_bookable(int(cmds[1]))):
            print("Yes the order is bookable")
        else:
            print("No the order is not bookable")

        print()
    
    elif(cmd == "BOOK_ORDER"):
        book_order(int(cmds[1]))
        print()

    elif(cmd == "CANCEL_ORDER"):
        cancel_order(int(cmds[1]))
        print()

    elif(cmd == "CANCEL_ORDER_LINE"):
        cancel_o_line(int(cmds[1]), cmds[2])
        print()

    elif(cmd == "EXIT"):
        break

    else: 
        print("Wrong command entered.")
        print()
        # break

