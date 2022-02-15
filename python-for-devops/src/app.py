# app.py


# learn variable
def getCustomer(customerID):
    lastName = "Pratama"
    firstName = "Piscki"

    if customerID == "01":
        firstName = "Febriansyah"

    fullname = f"{lastName} {firstName}"
    return f"ID: {customerID}, Name: {fullname}"


print(getCustomer("01"))


# learn list
def getCustomers():
    listCustomer = ["Piscki Pratama", "John Doe"]
    listCustomer.append("Mahrez Baker")
    listCustomer.append("Bruno Marteen")

    return listCustomer


customers = getCustomers()
customers.remove("Piscki Pratama")
print(customers)


# learn dictionaries
def getTransaction():
    transactions = {
        "name": "Piscki",
        "amount": "1000",
        "item": "Deep Work book"
    }

    return transactions


print(getTransaction())


# learn class
class Customer:
    def __init__(self, customerID="", firstName="", lastName=""):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName

    def fullname(self):
        return f"{self.firstName} {self.lastName}"


piscki = Customer("02", "Piscki", "Pratama")
print(piscki.fullname())
