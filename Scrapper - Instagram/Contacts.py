# Make a List Data Structure in Python

class List:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def append(self, item):
        self.items.append(item)

    def insert(self, index, item):
        self.items.insert(index, item)

    def pop(self):
        return self.items.pop()

    def remove(self, item):
        self.items.remove(item)

    def index(self, item):
        return self.items.index(item)

    def count(self, item):
        return self.items.count(item)

    def sort(self):
        self.items.sort()

    def reverse(self):
        self.items.reverse()

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, item):
        self.items[index] = item

    def __delitem__(self, index):
        del self.items[index]

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

    def __add__(self, other):
        return self.items + other.items

    def __iadd__(self, other):
        self.items += other.items
        return self

    def __mul__(self, other):
        return self.items * other

    def __imul__(self, other):
        self.items *= other
        return self

    def __eq__(self, other):
        return self.items == other.items

    def __ne__(self, other):
        return self.items != other.items

    def __lt__(self, other):
        return self.items < other.items

    def __le__(self, other):
        return self.items <= other.items

    def __gt__(self, other):
        return self.items > other.items

    def __ge__(self, other):
        return self.items >= other.items

# Contact class for the List class


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "Name: " + self.name + ", Phone: " + self.phone + ", Email: " + self.email

    def __eq__(self, other):
        return self.name == other.name and self.phone == other.phone and self.email == other.email

    def __ne__(self, other):
        return self.name != other.name or self.phone != other.phone or self.email != other.email

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

# Person Class


class Person:
    # Person has Name, 2 Phone Numbers and Email
    # Take Input
    def __init__(self, name, phone1, phone2, email):
        self.name = name
        self.phone1 = phone1
        self.phone2 = phone2
        self.email = email

    def __str__(self):
        return "" + self.name + "\n     Primary: " + self.phone1 + "\n     Mobile: " + self.phone2 + "\n     Email:" + self.email
    
    def __eq__(self, other):
        return self.name == other.name and self.phone1 == other.phone1 and self.phone2 == other.phone2 and self.email == other.email

    def __ne__(self, other):
        return self.name != other.name or self.phone1 != other.phone1 or self.phone2 != other.phone2 or self.email != other.email
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __le__(self, other):
        return self.name <= other.name
    
    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name






# Main Program to Test the Classes
def main():
    # Create a List of Contacts
    contacts = List()
    contacts.append(Contact("John Smith", "555-1234", "Test@gmail.com"))
    contacts.append(Contact("Jane Doe", "555-5678", "Test02@gmail.com"))
    contacts.append(Contact("Joe Schmoe", "555-9012", "Test03@gmail.com"))

    # Print the List
    print(contacts)

    # Print the List using a for loop
    for contact in contacts:
        print(contact)
    
    # Create an Object of Person
    person = Person("John Smith", "555-1234", "555-5678", "John@Test.com")
    print("======================= Printing Person Here =======================")
    print(person)
    print("==============================================")
    # Create a List of Numbers
    numbers = List()
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)

    # Print the List
    print(numbers)

    # Print the List using a for loop
    for number in numbers:
        print(number)
    
    # Create a List of Strings
    strings = List()
    strings.append("Hello")
    strings.append("World")
    strings.append("!")

    # Print the List
    print(strings)

    # Print the List using a for loop
    for string in strings:
        print(string)
    
    # Check Equality 
    print(contacts[0] == contacts[1])
    print(contacts[0] == contacts[0])
    print(contacts[0] != contacts[1])
    print(contacts[0] != contacts[0])

    # Check Less Than
    print(contacts[0] < contacts[1])
    print(contacts[0] < contacts[0])
    print(contacts[0] <= contacts[1])
    print(contacts[0] <= contacts[0])

    # Check Greater Than
    print(contacts[0] > contacts[1])
    print(contacts[0] > contacts[0])
    print(contacts[0] >= contacts[1])
    print(contacts[0] >= contacts[0])

    print(contacts)

    l = List()
    l.append(1)
    l.append(2)
    l.append(3)
    print(l)
    l.insert(0, 0)
    print(l)
    print(l.pop())
    print(l)
    l.remove(2)
    print(l)
    print(l.count(3))
    l.sort()
    print(l)
    l.reverse()
    print(l)
    print(len(l))
    print(l[0])
    l[0] = 4
    print(l)
    del l[0]
    print(l)
    for i in l:
        print(i)
    print(1 in l)
    l2 = List()
    l2.append(4)
    l2.append(5)
    l2.append(6)
    l += l2
    print(l)
    l *= 2
    print(l)
    print(l == l2)
    print(l != l2)
    print(l < l2)
    print(l <= l2)
    print(l > l2)
    print(l >= l2)

    # Reverse a List
    l.reverse()
    print(l)

    c1 = Contact("John", "1234567890", "John@test.com")
    c2 = Contact("Mark", "14234567890", "Mark@test.com")

    l3 = List()
    l3.append(c1)
    l3.append(c2)
    print(l3)
    print(l3[0])
    print(l3[0].name)
    print(l3[0].phone)
    print(l3[0].email)

    p1 = Person("John", "1234567890", "014123412", "Test@test.com")

    l4 = List()
    l4.append(p1)
    print(l4)
    print(l4[0])
    print(l4[0].name)
    print(l4[0].email)

    l5 = List()
    l5.append(1)
    l5.append(2)
    l5.append(3)
    print("END OF FILE")

# Call the main function
main()
