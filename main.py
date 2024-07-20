a = input("Want the phone to be on or off:")
if a == "on":
  print("")
  print("Powering on\nThis might take a few seconds")
  ab = int(input("Enter your sim pin:"))
  if ab == 7086:
    print("Sim unlocking")
    print("")
    ac = int(input("Enter your phone pin:"))
    while ac == 7098:
      print("phone is starting and ready to go")
      print("1. Contacts\n2. Calculator\n3. Shut down\n4. Cake Delivery app\n5. Browser\n6. Clock\n7. Game")
      contacts = {}
      while True:
       ad = int(input("Enter your choice:"))
       if ad == 1:
         while True:
          print("Choose any of the following options")
          print("\n1. Add Contact\n2. View Contacts\n3. Delete Contact\n4. Exit")
          choice = int(input("Enter your choice:"))
          if choice == 1:
           name = input("Enter contact name:")
           phone = input("Enter contact phone number:")
           contacts[name] = phone
           print(f"Contact {name} added")
          elif choice == 2:
           if contacts:
            for name, phone in contacts.items():
             print(f"{name}: {phone}")
           else:
            print("No contacts found")
          elif choice == 3:
           name = input("Enter contact name to delete:")
           if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted")
           else:
            print(f"Contact {name} not found")
          elif choice == 4:
            print("1. Contacts\n2. Calculator\n3. Shut down\n4. Cake Delivery app\n5. Browser\n6. Clock\n7. Game")
            break
            
          else:
           print("Invalid choice. Please try again")
       elif ad == 2:
         while True:
          print("Entering calculator")
          print("1. Enter calculator\n2. Exit")
          aba = int(input("Enter your choice"))
          if aba == 1:
           aa = int(input("Enter the first number"))
           bb = input("Enter the operator")
           cc = int(input("Enter the second number"))
           if bb == "+":
            print(aa + cc)
           elif bb == "-":
            print(aa - cc)
           elif bb == "*":
            print(aa * cc)
           elif bb == "/":
            print(aa / cc)
           else:
            print("Invalid operator inserted")
          elif aba == 2:
            print("1. Contacts\n2. Calculator\n3. Shut down\n4. Cake Delivery app\n5. Browser\n6. Clock\n7. Game")
            break
       elif ad == 3:
        print("Shutting down")
        exit()
       elif ad == 4:
         # Bakery shop inventory

         bakery_inventory = {

         "cakes": [

         {"name": "Chocolate Cake", "price": 15.0},

         {"name": "Vanilla Cake", "price": 12.0}

         ],

         "cookies": [

         {"name": "Chocolate Chip Cookie", "price": 2.0},

         {"name": "Oatmeal Raisin Cookie", "price": 2.5}

         ],

         "pastries": [

         {"name": "Croissant", "price": 3.0},

         {"name": "Danish", "price": 3.5}
         ]
         }

         # Order list
         orders = []

         # Display menu
         print("Welcome to the Bakery Shop!")
         print("Here is our menu:")
         for category, items in bakery_inventory.items():
             print(f"\n{category.capitalize()}:")
             for item in items:
                 print(f"  - {item['name']} (${item['price']})")

         # Taking orders
         while True:
             print("\nWhat would you like to order?")
             category = input("Enter category (cakes, cookies, pastries or 'done' to finish): ").lower()

             if category == "done":
                 break
             elif category in bakery_inventory:
                 print(f"\nAvailable {category}:")
                 for i, item in enumerate(bakery_inventory[category]):
                     print(f"{i + 1}. {item['name']} (${item['price']})")

                 item_number = int(input("Enter the item number you want to order: ")) - 1
                 if 0 <= item_number < len(bakery_inventory[category]):
                     quantity = int(input("Enter the quantity: "))
                     selected_item = bakery_inventory[category][item_number]
                     orders.append({"category": category, "item": selected_item["name"], "price": selected_item["price"], "quantity": quantity})
                     print(f"{quantity} x {selected_item['name']} added to your order.")
                 else:
                     print("Invalid item number. Please try again.")
             else:
                 print("Invalid category. Please try again.")

         # Display order summary
         if orders:
             print("\nOrder Summary:")
             total_amount = 0
             for order in orders:
                 print(f"{order['quantity']} x {order['item']} (${order['price']} each)")
                 total_amount += order["price"] * order["quantity"]
             print(f"\nTotal Amount: ${total_amount}")
         else:
             print("No items ordered.")

         print("Thank you for visiting the Bakery Shop!")
         print("Choose any of the following options")
         print("1. Contacts\n2. Calculator\n3. Shut down\n4. Cake Delivery app\n5. Browser\n6. Clock\n7. Game")    
       elif ad == 5:
         while True:
          print("1. enter browser\n2. Exit")
          aa = int(input("enter your choice:"))
          if aa == 1:
           a = input("Enter an URL:")
           if a == "replit.com":
            print("Welcome to world of coding\nStart building your projects\nStart coding")
           elif a == "github.com":
            print("Welcome to Github\nstart storing code")
           elif a == "bublooscientist.com":
            print("Welcome to a word of science where blogs meet science, entertainment and much more")
           elif a == "bublooscientist.com/login":
            b = input("Enter a username:")
            c = input("enter your username:")
            if b == "Abdur" and c == "abisbah2011@gmail.com":
              print("Welcome to word-press")
              print("These are your latest posts")
              print("Food and Nutrition\nBalanced diet\nPython coding")
          elif aa == 2:
            print("1. Contacts\n2. Calculator\n3. Shut down\n4. Cake Delivery app\n5. Browser\n6. Clock\n7. Games")
            break
       elif ad == 6:
           while True:
            print("1. Enter Clock\n2. Exit Clock")
            af = int(input("enter your choice"))
            if af == 1:
             import datetime
             import time
             date_and_time = datetime.datetime.now()
             print("Current date:", date_and_time.strftime("%x"))
             print("Current time:",time.strftime("%H:%M:%S"))
            elif af == 2:
              print("1. Contacts\n2. Calculator\n3. Shut down\n4. Cake Delivery app\n5. Browser\n6. Clock\n7. Game")
              break
            else:
              print("You have entered invalid input")
       elif ad == 7:
         while True:
          print("1. Enter Game\n2. Exit\n3. Counter")
          asa = int(input("Enter your choice:"))
          if asa == 1:
            import random



            number = random.randint(1, 100)
            attempts = 11
            guess = 0
            print("Welcome to the Python's Official Number gusessing")
            print("Rules:")
            print("1. Guess any number from 1 to 10.")
            print("2. You have only 10 attempts\nso the attempt counter will run and display each time you enter a wrong number")
            print("Have fun")
            if attempts >= 1:
             while guess != number:
              guess = int(input("enter your guess:"))
              attempts -= 1
              if guess > number:
               print("The number is High!!!")
              elif guess < number:
               print("The number is low!!!")
              else:
               print("Congratulations!!!")
            else:
              print("You have lost!\nTry again")
          elif asa == 2:
            print("1. Contacts\n2. Calculator\n3. Shut down\n4. Cake Delivery app\n5. Browser\n6. Clock\n7. Game")
            break
          elif asa == 3:
            import time
            a = int(input("Enter the number from which the counter will start:"))
            while a > 0:
              print(a)
              time.sleep(1)
              a = a  - 1
            else:
              print(f"Counter is at {a}")

            
           

elif a == "off":
 print("off")
else:
  print("invalid input")