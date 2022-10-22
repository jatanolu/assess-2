import csv

class Inventory():
    def __init__(self, id, title, rating, release_year, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available

    def Available_Movies():
        arr2 = []
        with open("./data/inventory.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for movie in reader:
                arr2.append(Inventory(**dict(movie)))


        return arr2
