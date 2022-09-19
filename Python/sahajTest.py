class Order:
    def __init__(self,orderId=-1):
        self.order_id=orderId
        self.orderProducts={}
        self.OrderStatus="DRAFT"
    

    def addProduct(self,productName,quantity):
        try:
            product=self.orderProducts[productName]
            prodQuantity=int(product["quantity"])
            prodQuantity+=int(quantity)
            product["quantity"]=prodQuantity
            self.orderProducts[productName]=product
            print("{} {} added to order {}".format(quantity,productName,self.order_id))
        except KeyError:
            self.orderProducts[productName]={"quantity":int(quantity),"status":"DRAFT"}
            print("{} {} added to order {}".format(quantity,productName,self.order_id))

    def statusOfOrder(self):
        status="DRAFT"
        draftPresent=False
        bookedPresent=False
        cancellledPresent=False
        for product in self.orderProducts.keys():
            productStatus=self.orderProducts[product]["status"]
            if(productStatus=="DRAFT"):
                draftPresent=True
                break
            else:
                if(productStatus=="BOOKED"):
                    status="BOOKED"
                    bookedPresent=True
                if(productStatus=="CANCELLED"):
                    cancellledPresent=True 
        if(draftPresent==False and bookedPresent==False and cancellledPresent==True):
            return "CANCELLED"
        return status

    def getCountofProducts(self):
            count=0
            for product in self.orderProducts.keys():
                count+=int(self.orderProducts[product]["quantity"])
            return count

    def printOrderDetails(self):
        print("\nOrder Id : "+str(self.order_id),self.OrderStatus,self.getCountofProducts())
        for product in self.orderProducts.keys():
            print(str(product)+" : "+str(self.orderProducts[product]["quantity"])+" "+self.orderProducts[product]["status"])
        print()

    def checkIfBookable(self,inventory):
        for product in self.orderProducts.keys():
            if(inventory[product]<int(self.orderProducts[product]["quantity"])):
                return False
        return True


    def bookOrder(self,inventory):
        updatedOrder=self.orderProducts
        updatedInventory=inventory
        notOrderedProducts=[]
        for product in self.orderProducts.keys():
            if(self.orderProducts[product]["status"]!="BOOKED" and inventory[product]>=int(self.orderProducts[product]["quantity"])):
                updatedInventory[product]=inventory[product]-int(self.orderProducts[product]["quantity"])
                updatedOrder[product]['status']="BOOKED"
            else:
                notOrderedProducts.append(product)
        self.orderProducts=updatedOrder
        return [updatedInventory,notOrderedProducts]
    
    def cancelOrder(self,inventory):
        updatedOrder=self.orderProducts
        updatedInventory=inventory
        for product in self.orderProducts.keys():
            if(self.orderProducts[product]["status"]=="BOOKED"):
                updatedInventory[product]=inventory[product]+int(self.orderProducts[product]["quantity"])
                updatedOrder[product]['status']="CANCELLED"
        self.orderProducts=updatedOrder
        return updatedInventory


    # def cancelOneProd()

class Inventory(Order):

    def __init__(self):
        self.productCount=0
        self.inventoryProducts={}
        self.lastOrderId=-1
        self.Orders={}
        self.addInventoryProducts()


    def addInventoryProducts(self):
        print("Add Inventory Products : ")
        n=int(input())
        self.productCount=n
        for i in range(n):
            productDetails=list(input().split())
            self.inventoryProducts[productDetails[0]]=int(productDetails[1])
    

    def showInventory(self):
        print("\nInventory : ")
        for product in self.inventoryProducts.keys():
            print(product," : ",self.inventoryProducts[product])
        print()

    def createOrder(self):
        newOrderId=None
        if(self.lastOrderId==-1):
            newOrderId=1
            newOrder=Order(newOrderId)
        else:
            newOrderId=self.lastOrderId+1
            newOrder=Order(newOrderId)
        self.Orders[newOrderId]=newOrder
        print("Order Created with id {}".format(newOrderId))

    def addOrderLine(self,orderId,productName,productQuantity):
        order=self.Orders[int(orderId)]
        order.addProduct(productName,productQuantity)
    

    def showOrder(self,orderId):
        order=self.Orders[int(orderId)]
        order.printOrderDetails()


    def showAllOrders(self):
        print("All Orders : ")
        for order in self.Orders.keys():
            curOrder=self.Orders[int(order)]
            curOrder.printOrderDetails()
        print("\n")
    
    def giveStatusOfOrder(self,orderId):
        order=self.Orders[int(orderId)]
        OrderStatus=order.statusOfOrder()
        print("Order Status of Order_ID {}  is {} : ".format(orderId,OrderStatus))
    

    def isOrderBookable(self,orderId):
        order=self.Orders[int(orderId)]
        status=order.checkIfBookable(self.inventoryProducts)
        print("\nOrder {} BOOKABLE STATUS : {} \n".format(orderId,status))

    def bookOrderWithOrderId(self,orderId):
        order=self.Orders[int(orderId)]
        updatedOrder=order.bookOrder(self.inventoryProducts)
        self.inventoryProducts=updatedOrder[0]
        notOrderedProducts=updatedOrder[1]

        

        if(len(notOrderedProducts)>0):
            print("NOT ORDERED PRODUCTS")
            for i in notOrderedProducts:
                print(i)
            print("\n")
        

        print("UPDATED INVENTORY : ")
        self.showInventory()


    def cancelOrderWithOrderID(self,orderId):
        order=self.Orders[int(orderId)]
        updatedOrder=order.cancelOrder(self.inventoryProducts)
        self.inventoryProducts=updatedOrder

        print("UPDATED INVENTORY : ")
        self.showInventory()

    def cancelSpecProd(self,orderId,productName):
        order=self.Orders[int(orderId)]
        updatedOrder=order.cancelOrder(self.inventoryProducts,productName)
        self.inventoryProducts=updatedOrder

        print("UPDATED INVENTORY : ")
        self.showInventory()
        
def main():
    inv=Inventory()

    while(True):
        print("1. CREATE_ORDER")
        print("2. ADD_ORDERLINE [order_id] [product_name] [product_quantity]")
        print("3. SHOW_INVENTORY")
        print("4. SHOW_ORDER [order_id]")
        print("5. SHOW_ORDERS")
        print("6. IS_ORDER_BOOKABLE [order_id]")
        print("7. BOOK_ORDER [order_id]")
        print("8. CANCEL_ORDER [order_id]")
        print("9. CANCEL_ORDER_LINE [order_id] [product_name]")
        print("10. Press 0 to exit")

        inputCommand=input().split()

        if(inputCommand[0].strip()=="CREATE_ORDER"):
            inv.createOrder()
        elif(inputCommand[0].strip()=="ADD_ORDERLINE"):
            orderId=inputCommand[1]
            productName=inputCommand[2]
            quantity=inputCommand[3]
            inv.addOrderLine(orderId,productName,quantity)
        elif(inputCommand[0].strip()=="SHOW_INVENTORY"):
            inv.showInventory()
        elif(inputCommand[0].strip()=="SHOW_ORDER"):
            orderId=inputCommand[1]
            inv.showOrder(orderId)
        elif(inputCommand[0].strip()=="SHOW_ORDERS"):
            inv.showAllOrders()
        elif(inputCommand[0].strip()=="IS_ORDER_BOOKABLE"):
            orderId=inputCommand[1]
            inv.isOrderBookable(orderId)
        elif(inputCommand[0].strip()=="BOOK_ORDER"):
            orderId=inputCommand[1]
            inv.bookOrderWithOrderId(orderId)
        elif(inputCommand[0].strip()=="CANCEL_ORDER"):
            orderId=inputCommand[1]
            inv.cancelOrderWithOrderID(orderId)
        elif(inputCommand[0].strip()=="0"):
            break
        else:
            print("\nINVALID INPUT\n")

main()

