#Finnegan Sutherland
#3/29/2026
#List of items I want put in a store and it cacultes subtotal, tax, shipping, and then final total

def main():
    cart = []
    prices = []
    while True:
     print("=" * 30 + " Finn wonder store " + "=" * 30)
     print("")
     print("-" * 60)
     print("1: MotherBoard")
     print("2: CPU")
     print("3: RAM")
     print("4: Storage")
     print("5: GPU")
     print("6: Cooling System")
     print("7: Case")
     print("")
     print("8:  Checkout")
     print("9:  Clear selected")
     print("10: Leave, you bought nothing from here!")
     print("=" * 60)

     choice = input("Enter your item\n")
    

     if choice == "1":
        print("-" * 60)
        print("1: MSI B850M-A Pro - $169.99\n")
        print("2: Gigabyte x870 aorus stealth amd - $309.99\n")
        print("3: Asus B850M-Plus Tuf Gaming - $259.99\n")
        print("-" * 60)

        sub_choice = input("choose one: ")
       
        if sub_choice == "1":
            cart.append("MSI B850M-A Pro")
            prices.append(169.99)
        elif sub_choice == "2":
            cart.append("Gigabyte x870 aorus stealth amd")
            prices.append(309.99)
        elif sub_choice == "3":  
             cart.append("Asus B850M-Plus Tuf Gaming")
             prices.append(259.99)
        
     elif choice == "2":
        print("-" * 60)
        print("1: Intel core ultra 9 - $593.49\n")
        print("2: AMD Ryzen 7 - $479.00\n")
        print("3: Intel core ultra 5 - $167.49\n")
        print("-" * 60)

        sub_choice = input("choose one: ")
       
        if sub_choice == "1":
            cart.append("Intel core ultra 9")
            prices.append(593.49)
        elif sub_choice == "2":
            cart.append("AMD Ryzen 7")
            prices.append(479.00)
        elif sub_choice == "3":  
             cart.append("Intel core ultra 5")
             prices.append(167.49)
        
     elif choice == "3":
         print("-" * 60)
         print("1: Corsair Vengenace LPX 32GB, DDR4 - $242.99\n")
         print("2: Corsair Vengeance RG 32GB, DDR 5 - $369.99 \n")
         print("3: Corsair Vengeance 32GB, DDR5 - $349.99\n")
         print("-" * 60)

         sub_choice = input("choose one: ")
       
         if sub_choice == "1":
            cart.append("Corsair Vengenace LPX 32GB, DDR4")
            prices.append(242.99)
         elif sub_choice == "2":
            cart.append("Corsair Vengeance RG 32GB, DDR 5")
            prices.append(369.99)
         elif sub_choice == "3":  
             cart.append("Corsair Vengeance 32GB, DDR5")
             prices.append(349.99)
     elif choice == "4":
            print("-" * 60)
            print("1: Samsung 990 Pro 2TB - $242.99\n")
            print("2: Crucial P310 2TB - $259.99\n")
            print("3: Samsu ng 990 Pro 2TB - $399.99\n")
            print("-" * 60)

            sub_choice = input("choose one: ")
       
            if sub_choice == "1":
                cart.append("Samsung 990 Pro 2TB")
                prices.append(242.99)
            elif sub_choice == "2":
                cart.append("Crucial P310 2TB")
                prices.append(259.99)
            elif sub_choice == "3": 
                cart.append("Samsung 990 Pro 2TB")
                prices.append(399.99)
     elif choice == "5":
         print("-" * 60)
         print("1: Gigabyte GeFOrce TRX 5050 - $317.99\n")
         print("2: PNY GeForce RTX 5080 - $1289.99\n")
         print("3: MSI Nvidia GeForce RTX 5070 - $679.99\n")
         print("-" * 60)

         sub_choice = input("choose one: ")
       
         if sub_choice == "1":
            cart.append("Gigabyte GeFOrce TRX 5050")
            prices.append(317.99)
         elif sub_choice == "2":
            cart.append("PNY GeForce RTX 5080")
            prices.append(1289.99)
         elif sub_choice == "3": 
             cart.append("MSI Nvidia GeForce RTX 5070")
             prices.append(679.99)
     elif choice == "6":
            print("-" * 60)
            print("1: Air Cooling - $150\n")
            print("2: Liquid Cooling - $200\n")
            print("-" * 60)

            sub_choice = input("choose one: ")
       
            if sub_choice == "1":
                cart.append("Air Cooling")
                prices.append(150)
            elif sub_choice == "2":
                cart.append("Liquid Cooling")
                prices.append(200)
            
     elif choice == "7":
            print("-" * 60)
            print("1: Card Board Box - FREE!\n")
            print("2: NZCT H6 flow ATX mid tower pc case with dual chamber black - $99.99\n")
            print("3: NZXT H9 flow 2025 ATX Mid tower dual chamber pc case white - $119.99\n")
            print("-" * 60)

            sub_choice = input("choose one: ")
       
            if sub_choice == "1":
                cart.append("Card Board Box - Free")
                prices.append(0)
            elif sub_choice == "2":
                cart.append("NZCT H6 flow ATX mid tower pc case with dual chamber black")
                prices.append(99.99)
            elif sub_choice == "3": 
                cart.append("NZXT H9 flow 2025 ATX Mid tower dual chamber pc case white")
                prices.append(119.99)
     
     elif choice == "8":
         if len(cart) == 0:
                print("There is nothing in your cart.")
         else: 
            for item, price in zip(cart,prices):
             print(item, "- $" + str(price))
            print("-" * 30 + " Conformation of purchase " + "-" * 30)
            confirm = input("1: Confirm / 2: Go back\n")

            if confirm == "1":
                print("=" * 30 + " Payment " + "=" * 30)
                for item, price in zip(cart,prices):
                    print(item, "- $" + str(price))
                print("-" * 60)

                subtotal = 0
                
                for i in range(len(prices)):
                    subtotal += float(prices[0])

                tax = subtotal * .065
                shipping = 5.99
                total = subtotal + tax + shipping

                print("Your subtotal: $" + str(round(subtotal, 2)))
                print("Tax: $" + str(round(tax, 2)))
                print("Shipping: $" + str(round(shipping, 2)))
                print("Total: $" + str(round(total, 2)) + "\n")

                print("Thank you for your purchase!")
                break
            if confirm == "2":
                pass
                
     elif choice == "9":
        cart.clear()
        print("Your cart is clear.")
    
     elif choice == "10":
        print("Thank you for coming by, see you next time!")
        break
main()        

   