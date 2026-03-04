import json
class expense:
    def __init__(self,id,title,category,amount,date):
        self.id = id
        self.title = title
        self.category = category 
        self.amount = amount
        self.date = date
    @staticmethod
    def show_expense(expenses):
        for x in range(len(expenses)):
             print(expenses[x].title)

    def to_dict(self):
        return {
            "I.D." : self.id,
            "Title": self.title,
            "Category": self.category,
            "Amount": self.amount,
            "Date": self.date,
        }


record = []
expenses = []
cmd = True
while cmd != "end":
    a = input("Enter 'id':")
    b = input("Enter title:")
    c = input("Enter category:")
    d = input("Enter amount:")
    e = input("Enter date:")
    new_expense = expense(a,b,c,d,e)
    record.append(expense.to_dict(new_expense))
    expenses.append(new_expense)
    cmd = input("Enter command:")

with open("C:/Users/Lenovo/Documents/Programs/python_files/simple-projects/expenses.json","w") as file:
        json.dump(record,file)
expense.show_expense(expenses)
with open("C:/Users/Lenovo/Documents/Programs/python_files/simple-projects/expenses.json","r") as f:
    data = json.load(f)
    [print(x) for x in data]

















