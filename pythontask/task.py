# EmailAddress Class

class EmailAddress:
    def __init__(self, username, symbol, domain):
        self.username = username
        self.symbol = symbol
        self.domain = domain

    def __str__(self):
        return f"{self.username}{self.symbol}{self.domain}"

    def is_address_valid(self):
        if self.symbol == "@":
            pass
        else:
            print("invalid: no @ sign")
            return False

        # If the username is empty return False
        if self.username == "":
            print("invalid: Username is an empty string.")
            return False

        # If the domain contains .edu return True
        if ".edu" in self.domain:
            pass
        else:
            print("invalid: no .edu")
            return False
        return True


a1 = EmailAddress("john", "@", "gmu.edu")
a2 = EmailAddress("peter", "&", "gmu.net")
a3 = EmailAddress("", "@", "t.edu ")
a4= EmailAddress("user", "@", "t.eau ")

print("===================== Object 01 =====================")
print("Email: " + a1.__str__())
if (a1.is_address_valid()):
    print("Validity: Valid")

print("===================== Object 02 =====================")
print("Email: " + a2.__str__())
if (a2.is_address_valid()):
    print("Validity: Valid")

print("===================== Object 03 =====================")
print("Email: " + a3.__str__())
if (a3.is_address_valid()):
    print("Validity: Valid")

print("===================== Object 04 =====================")
print("Email: " + a4.__str__())
if (a4.is_address_valid()):
    print("Validity: Valid")