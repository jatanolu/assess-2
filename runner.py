# Write your solution here!
from classes.customer import Customer
from classes.inventory import Inventory

def options(option):
    if(option ==1):
        for row in movies:
            print(f"\nID:{row.id}  Movie:{row.title}  # Available:{row.copies_available}")
        return " "

    if(option == 2):
        for row in accounts:
            print(f"\nCustomer ID:{row.id} Name:{row.first_name} {row.last_name}")
        return " "

    if(option == 3):
        for row in accounts:
            print(f"\nCustomer ID:{row.id} Movies Rented: {row.current_video_rentals}")
        return " "

    if(option == 4): 
        Customer.adder(accounts)
        return ' '

    if(option == 5):
        Customer.rent(accounts, movies)
        return " "

    if(option == 6):
        Customer.return_movie(accounts, movies)
        return ' '

    if(option == 7):
        return "Come again!"

movies = Inventory.Available_Movies()
accounts = Customer.all_customers()
menu = 0
while menu != 7:
    menu = int(input("== Welcome to Code Platoon Video! ==\n1. View store video inventory\n2. View store customers\n3. View customer rented videos\n4. Add new customer\n5. Rent video\n6. Return video\n7. Exit\nInput: "))
    print(options(menu))
