
import csv

codes = {
    1  : 'Macroeconomics',
    2  : 'Civil Rights',
    3  : 'Health',
    4  : 'Agriculture',
    5  : 'Labor',
    6  : 'Education',
    7  : 'Environment',
    8  : 'Energy',
    9  : 'Immigration',
    10 : 'Transportation',
    12 : 'Law and Crime',
    13 : 'Social Welfare',
    14 : 'Housing',
    15 : 'Domestic Commerce',
    16 : 'Defense',
    17 : 'Technology',
    19 : 'International Affairs',
    20 : 'Government Operations',
    21 : 'Public Lands',
    24 : 'Local Government',

}

# BillCSV is a class which implements downloaded CSV files containing bill data
# into Python so it can be interfaced with the application. This will initially be 
# designed solely for our visualization purposes, but I intend to design the class 
# to be as useful as possible for implementing the data into Python for easy access
# to statistical analysis, data models, and machine learning in the future.

class BillCSV:

    class Bill:

        bill_attrs = [
            'uid', 'title', 'fulltext',
            'session', 'finalcode', 'summary'
        ]
        
        def __init__(self, data):
            for i in range(len(data)):
                setattr(self, self.bill_attrs[i], data[i])

        def __repr__(self):
            return f'<Session:{self.session}, Code:{self.finalcode}, UID:{self.uid}>'

        def __str__(self):
            return self.__repr__()

        def get_year(self):
            return int(self.session[:4])

        def get_code(self, numeric=False):
            global codes
            if not numeric:
                return self.finalcode
            else:
                return list(codes.keys())[list(codes.values()).index(self.finalcode)]


            
    """The BillCSV class takes a file URI as the only argument. Make sure you
    have the file downloaded and are in the right directory. It will then import
    the csv file into Python. Each individual will become it's own object, 'Bill',
    which is a sort of "child" object of the larger BillCSV object which contains
    all the bills in the CSV file"""
    def __init__(self, csv_file):
        csv_obj = csv.reader(open(csv_file), delimiter=',')
        self.bills = [BillCSV.Bill(row) for row in csv_obj]
        self.bills.pop(0)

    def __repr__(self):
        return f'<BillCSV, {len(self.bills)} bills>'

    def __str__(self):
        return self.__repr__()

    def __iter__(self):
        return iter(self.bills)

    def __next__(self):
        ind = self.ind
        self.ind += 1
        return ind
    
    def __getitem__(self, index):
        return self.bills[index]

    def __len__(self):
        return len(self.bills)

    def get_bills_by_year(self, year):
        return [bill for bill in self if bill.get_year() ==  year]

    def get_bills_by_code(self, code):
        global codes
        return [bill for bill in self if bill.get_code() == codes[code]]