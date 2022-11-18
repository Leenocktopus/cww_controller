import csv


class Repository():

    def __init__(self, employees, ratings):
        self.employees = employees
        self.ratings = ratings

    def find_all_names(self):
        with open(self.employees) as employees:
            csv_reader = csv.reader(employees, delimiter=',')
            return [row for row in csv_reader if row != ['NAME']]

    def save_rating(self, name, rating, decision):
        with open(self.ratings, mode='a') as ratings:
            fieldnames = ['NAME', 'RATING', 'DECISION']
            writer = csv.DictWriter(ratings, fieldnames=fieldnames)
            writer.writerow({fieldnames[0]: name, fieldnames[1]: rating, fieldnames[2]: decision})

    def find_all_ratings(self):
        with open(self.ratings) as employees:
            csv_reader = csv.reader(employees, delimiter=',')
            return [row for row in csv_reader if row != ['NAME', 'RATING', 'DECISION']]
