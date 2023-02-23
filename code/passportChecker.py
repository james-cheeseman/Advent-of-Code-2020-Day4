import pandas

class PassportChecker:

    def __init__(self, filePath):
        with open(filePath, "r") as file:
            self.passportsString = file.read()

    def toList(self):
        # Split the string on a line break ("\n\n")
        passportList = self.passportsString.split("\n\n")

        # Create a new list and populate with each passport converted to a dictionary
        passportDictList = []
        for passport in passportList:
            # Split the string on white space
            passport = passport.split()

            # Split each field on : with the first item as key and second item as value
            # Add these values to the dictionary and add this dictionary to the list
            passportDict = {}
            for field in passport:
                key, value = field.split(":")
                passportDict.update({key:value})
            passportDictList.append(passportDict)


        return passportDictList
    
    def validatePassport(self, passport):
        # Return true if passport valid

    def validateByr(self, byr):
        # Return true if birth year is valid
        # four digits; at least 1920 and at most 2002

    def validateIyr(self, iyr):
        # Return true if issue year is valid
        # four digits; at least 2010 and at most 2020

    def validateEyr(self, eyr):
        # Return true if expiration year is valid
        # four digits; at least 2020 and at most 2030

    def validateHgt(self, eyr):
        # Return true if height is valid
        # a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76

    def validateHcl(self, hcl):
        # Return true if hair colour is valid
        # a # followed by exactly six characters 0-9 or a-f
    
    def validateEcl(self, ecl):
        # Return true if eye colour is valid
        # exactly one of: amb blu brn gry grn hzl oth

    def validatePid(self, pid):
        # Return true if passport id is valid
        # a nine-digit number, including leading zeroes