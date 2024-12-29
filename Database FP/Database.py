import mysql.connector

# Establish the connection to the database
db_connection = mysql.connector.connect(
    host="127.0.0.1",         # Your host
    user="root",              # Your username
    password="Samuel235!",    # Your MySQL password
    database="restaurantdb"   # The name of your database
)

# Function to add a customer
def add_customer(first_name, last_name, email, phone_number, address):
    cursor = db_connection.cursor()
    try:
        sql = """
        INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (first_name, last_name, email, phone_number, address))
        db_connection.commit()
        print(f"Customer {first_name} {last_name} added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to remove a customer
def remove_customer(customer_id):
    cursor = db_connection.cursor()
    try:
        sql = "DELETE FROM Customer WHERE CustomerID = %s"
        cursor.execute(sql, (customer_id,))
        db_connection.commit()
        print(f"Customer with ID {customer_id} removed successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to calculate total revenue from sales
def calculate_total_revenue():
    cursor = db_connection.cursor()
    try:
        sql = "SELECT SUM(AmountPaid) FROM Payment"
        cursor.execute(sql)
        total_revenue = cursor.fetchone()[0]
        print(f"Total Revenue from Sales: ${total_revenue:.2f}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to update customer info
def update_customer_info(customer_id, field, new_value):
    cursor = db_connection.cursor()
    try:
        if field == "email":
            sql = "UPDATE Customer SET Email = %s WHERE CustomerID = %s"
        elif field == "phone":
            sql = "UPDATE Customer SET PhoneNumber = %s WHERE CustomerID = %s"
        elif field == "address":
            sql = "UPDATE Customer SET Address = %s WHERE CustomerID = %s"
        else:
            print("Invalid field. Please choose 'email', 'phone', or 'address'.")
            return
        
        cursor.execute(sql, (new_value, customer_id))
        db_connection.commit()
        print(f"Customer {field} updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to update inventory quantity
def update_inventory(inventory_id, field, new_value):
    cursor = db_connection.cursor()
    try:
        if field == "quantity":
            sql = "UPDATE Inventory SET Quantity = %s WHERE InventoryID = %s"
        elif field == "price":
            sql = "UPDATE Inventory SET UnitPrice = %s WHERE InventoryID = %s"
        else:
            print("Invalid field. Please choose quantity or price.")
            return
       
        cursor.execute(sql, (new_value, inventory_id))
        db_connection.commit()
        print(f"Inventory item with the InventoryID {inventory_id} updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to add a reservation
def add_reservation(customer_id, table_id, reservation_date, time_slot, status):
    cursor = db_connection.cursor()
    try:
        sql = """
        INSERT INTO Reservation (CustomerID, TableID, ReservationDate, TimeSlot, Status)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (customer_id, table_id, reservation_date, time_slot, status))
        db_connection.commit()
        print(f"Reservation for CustomerID {customer_id} added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to remove a reservation
def remove_reservation(reservation_id):
    cursor = db_connection.cursor()
    try:
        sql = "DELETE FROM Reservation WHERE ReservationID = %s"
        cursor.execute(sql, (reservation_id,))
        db_connection.commit()
        print(f"Reservation with ID {reservation_id} removed successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to add staff
def add_staff(staff_name, role, shift, phone_num, status, table_id):
    cursor = db_connection.cursor()
    try:
        sql = """
        INSERT INTO Staff (StaffName, Role, Shift, PhoneNum, Status, TableID)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (staff_name, role, shift, phone_num, status, table_id))
        db_connection.commit()
        print(f"Staff {staff_name} added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to remove staff
def remove_staff(staff_id):
    cursor = db_connection.cursor()
    try:
        sql = "DELETE FROM Staff WHERE StaffID = %s"
        cursor.execute(sql, (staff_id,))
        db_connection.commit()
        print(f"Staff with ID {staff_id} removed successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to update staff information
def update_staff_info(staff_id, field, new_value):
    cursor = db_connection.cursor()
    try:
        if field == "role":
            sql = "UPDATE Staff SET Role = %s WHERE StaffID = %s"
        elif field == "shift":
            sql = "UPDATE Staff SET Shift = %s WHERE StaffID = %s"
        elif field == "phone_num":
            sql = "UPDATE Staff SET PhoneNum = %s WHERE StaffID = %s"
        elif field == "status":
            sql = "UPDATE Staff SET Status = %s WHERE StaffID = %s"
        elif field == "table_id":
            sql = "UPDATE Staff SET TableID = %s WHERE StaffID = %s"
        else:
            print("Invalid field. Please choose 'role', 'shift', 'phone_num', 'status', or 'table_id'.")
            return
        
        cursor.execute(sql, (new_value, staff_id))
        db_connection.commit()
        print(f"Staff {field} updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to add inventory item
def add_inventory(item_name, category, quantity, price):
    cursor = db_connection.cursor()
    try:
        sql = """
        INSERT INTO Inventory (ItemName, Category, Quantity, UnitPrice)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (item_name, category, quantity, price))
        db_connection.commit()
        print(f"Inventory item {item_name} added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to remove inventory item
def remove_inventory(inventory_id):
    cursor = db_connection.cursor()
    try:
        sql = "DELETE FROM Inventory WHERE InventoryID = %s"
        cursor.execute(sql, (inventory_id,))
        db_connection.commit()
        print(f"Inventory item with ID {inventory_id} removed successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
# Function to add inventory item
def add_menuitem(item_name, category, price, description):
    cursor = db_connection.cursor()
    try:
        sql = """
        INSERT INTO MenuItem (ItemName, Category, Price, Description)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (item_name, category, price, description))
        db_connection.commit()
        print(f"Menu {item_name} added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Function to remove inventory item
def remove_menuitem(menuitem_id):
    cursor = db_connection.cursor()
    try:
        sql = "DELETE FROM MenuItem WHERE MenuItemID = %s"
        cursor.execute(sql, (menuitem_id,))
        db_connection.commit()
        print(f"Menu item with ID {menuitem_id} removed successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
def update_menuitemprice(menuitem_id, new_price):
    cursor = db_connection.cursor()
    try:
        sql = "UPDATE MenuItem SET Price = %s WHERE MenuItemID = %s"
        cursor.execute(sql, (new_price, menuitem_id))
        db_connection.commit()
        print(f"Menu item with ID {menuitem_id} price updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


# Menu function for user operations
def menu():
    while True:
        print("\nRestaurant Management System")
        print("1. Add Customer")
        print("2. Remove Customer")
        print("3. Calculate Total Revenue")
        print("4. Update Customer Info")
        print("5. Add Reservation")
        print("6. Remove Reservation")
        print("7. Add Staff")  
        print("8. Remove Staff")  
        print("9. Update Staff Info")  
        print("10. Update Inventory")
        print("11. Add Inventory Item") 
        print("12. Remove Inventory Item")  
        print("13. Update Menu Item Price")
        print("14. Add Menu Item") 
        print("15. Remove Menu Item")  
        print("16. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            phone_number = input("Phone Number: ")
            address = input("Address: ")
            add_customer(first_name, last_name, email, phone_number, address)
        elif choice == '2':
            customer_id = int(input("Enter CustomerID to remove: "))
            remove_customer(customer_id)
        elif choice == '3':
            calculate_total_revenue()
        elif choice == '4':
            customer_id = int(input("Enter CustomerID to update: "))
            print("What do you want to update?")
            print("1. Email")
            print("2. Phone Number")
            print("3. Address")
            field_choice = input("Enter your choice: ")
            
            if field_choice == '1':
                new_email = input("Enter new email: ")
                update_customer_info(customer_id, "email", new_email)
            elif field_choice == '2':
                new_phone = input("Enter new phone number: ")
                update_customer_info(customer_id, "phone", new_phone)
            elif field_choice == '3':
                new_address = input("Enter new address: ")
                update_customer_info(customer_id, "address", new_address)
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        elif choice == '5':  
            customer_id = int(input("Enter CustomerID for reservation: "))
            table_id = int(input("Enter TableID for reservation: "))
            reservation_date = input("Enter Reservation Date: ")
            time_slot = input("Enter Time Slot: ")
            status = input("Enter Status: ")
            
            add_reservation(customer_id, table_id, reservation_date, time_slot, status)
        elif choice == '6': 
            reservation_id = int(input("Enter ReservationID to remove: "))
            remove_reservation(reservation_id)
        elif choice == '7':  
            staff_name = input("Enter Staff Name: ")
            role = input("Enter Role: ")
            shift = input("Enter Shift: ")
            phone_num = input("Enter Phone Number: ")
            status = input("Enter Status: ")
            table_id = int(input("Enter TableID: "))
            
            add_staff(staff_name, role, shift, phone_num, status, table_id)
        elif choice == '8':  
            staff_id = int(input("Enter StaffID to remove: "))
            remove_staff(staff_id)
        elif choice == '9':  
            staff_id = int(input("Enter StaffID to update: "))
            print("What do you want to update?")
            print("1. Role")
            print("2. Shift")
            print("3. Phone Number")
            print("4. Status")
            print("5. Table ID")
            field_choice = input("Enter your choice: ")
            
            if field_choice == '1':
                new_role = input("Enter new role: ")
                update_staff_info(staff_id, "role", new_role)
            elif field_choice == '2':
                new_shift = input("Enter new shift: ")
                update_staff_info(staff_id, "shift", new_shift)
            elif field_choice == '3':
                new_phone = input("Enter new phone number: ")
                update_staff_info(staff_id, "phone_num", new_phone)
            elif field_choice == '4':
                new_status = input("Enter new status: ")
                update_staff_info(staff_id, "status", new_status)
            elif field_choice == '5':
                new_table_id = int(input("Enter new table ID: "))
                update_staff_info(staff_id, "table_id", new_table_id)
            else:
                print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")
        elif choice == '10': 
            itemname = input("Enter Item Name to update: ")
            print("What do you want to update?")
            print("1. Quantity")
            print("2. Price")
            field_choice = input("Enter your choice: ")
            
            if field_choice == '1':
                new_quantity = input("Enter new quantity: ")
                update_inventory(itemname, "quantity", new_quantity)
            elif field_choice == '2':
                new_price = input("Enter new phone price: ")
                update_inventory(itemname, "price", new_price)
            else:
                print("Invalid choice. Please choose 1 or 2.")
        elif choice == '11': 
            inventory_id = int(input("Enter Item Name: "))
            category = input("Enter Category: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            add_inventory(inventory_id, category, quantity, price)
        elif choice == '12':  
            inventory_id = int(input("Enter InventoryID to remove: "))
            remove_inventory(inventory_id)
        elif choice == '13':  
            menuitem_id = int(input("Enter InventoryID to update quantity: "))
            new_price = float(input("Enter new price: "))
            update_menuitemprice(menuitem_id, new_price)
        elif choice == '14': 
            menuitem = input("Enter Item Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            description = input("Enter Description: ")
            add_menuitem(menuitem, category, price, description)
        elif choice == '15':  
            menuitem_id = int(input("Enter MenuItemID to remove: "))
            remove_menuitem(menuitem_id)
        elif choice == '16':
            db_connection.close()
            break
        else:
            print("Invalid choice. Try again.")


menu()



