import csv


class Customer:
    def __init__(self, id, account_type, first_name, last_name, current_video_rentals = [""]):
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    def all_customers():

        arr1 = []
        with open("./data/customers.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for customer in reader:
                arr1.append(Customer(**dict(customer)))
        for ele in arr1:
            ele.current_video_rentals = ele.current_video_rentals.split("/")

        return arr1

    def adder(self):

        id = int(self[-1].id) +1
        atype = input("Account type (sx/px/sf/pf): ")
        if atype[0] != 's' and atype[0] != 'p':  
            return print("\nIncorrect account type, system failure... try again.")
        if atype[1] != 'x' and atype[1] != 'f':
            return print("\nIncorrect account type, system failure... try again.")
        fname = str(input("First name: "))
        lname = str(input("Last name: "))
        self.append(Customer(id, atype, fname, lname))

        return self

    def rent(accounts, movies):
        accountid = input("Account id: ")
        selected = ''
        film = ''

        for account in accounts:
            if int(account.id) == int(accountid):
                selected = account
                if Customer.checknum(account) == 'n':
                    return print("\nNo more available rentals for this ID\nReturn movie a Move?")
        if selected == '':
            return print("\nAccount ID does not exist\n")

        choice = input("Movie title: ")
        for movie in movies:
            if movie.title == choice and int(movie.copies_available) > 0:
                film = choice 
                if choice in selected.current_video_rentals:
                    return print("\nMovie already rented by customer.\n")
                if Customer.checktype(selected, movie) == 'n':
                    return print("\nSorry, movie not allowed for this account\nAnother perhaps?")
                movie.copies_available = int(movie.copies_available) -1
                selected.current_video_rentals.append(choice)
                if selected.account_type[0] == 's':
                    selected.current_video_rentals.pop(0)
        if choice != film:
            return print("\nMovie not in our inventory, sorry\n")
        return print(f"\nThank you and enjoy {choice}.")

            
    def checknum(account):

        if account.account_type[0] == 'p' and len(account.current_video_rentals) < 3:
            return 'y'
        if account.account_type[0] == 's' and account.current_video_rentals[0] == '':
            return 'y' 
        return 'n'

    def checktype(account, movie):

        if account.account_type[1] == 'f' and movie.rating == 'R':
            return 'n'
        else:
            return 'y'


    def return_movie(accounts, movies):
        choice = input("Move title: ")
        the_movie = ''

        for movie in movies:
            if movie.title == choice: 
                the_movie = movie
        if the_movie == '':
            return print("\nNot a movie in our inventory")

        accountid = input("Account id: ")
        for account in accounts:
            if int(account.id) == int(accountid):
                accountid = account
                if choice in accountid.current_video_rentals:
                    for x, ele in enumerate(accountid.current_video_rentals):
                        if choice == ele:
                            del accountid.current_video_rentals[x]
                    the_movie.copies_available = int(the_movie.copies_available)+1
                    return print(f"\nThank you for returning {choice}.")
                else:
                    return print("\nNot a movie you rented from us")
        return print("\nNot a customer here")

