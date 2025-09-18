def main():
    menu = {"burger" : 100,
            "coffee" : 200,
            "pasta" : 300,
            "shake" : 400,
            "pizza" : 500
            }
    print(f"🥰🥰WELCOME TO OUR CAFE🥰🥰!\nHere's the menu:\nBurger : Rs.100\nCoffee : Rs.200\nPasta : Rs.300\nShake : Rs.400\nPizza : Rs.500")
    order_total = 0

    order_1 = input("Order please! : ").lower().strip()
    if order_1 in menu:
        order_total+=menu[order_1]
        print(f"Your {order_1} is added to your order")
    else:
        print("Sorry, please select something from menu.")

    while True:
        order_n = input("Anthing else? (Give order or say 'no' to stop) : ").lower().strip()
        if order_n == "no":
            print(f"Your bill is Rs.{order_total}")
            break
        else:            
            if order_n in menu:
                order_total+=menu[order_n]
                print(f"Your {order_n} is added to your order")
            else:
                print("Sorry, please select something from menu.")
    
main()


