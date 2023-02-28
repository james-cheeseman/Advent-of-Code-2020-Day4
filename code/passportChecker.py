import re

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
    
    def validatePassport(passport):
        # Return true if passport valid
        # if passport contains correct fields
        # and if each field is valid
        requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        if all(key in passport for key in requiredFields):
            return all([PassportChecker.validateByr(passport), 
                       PassportChecker.validateIyr(passport), 
                       PassportChecker.validateEyr(passport), 
                       PassportChecker.validateHgt(passport), 
                       PassportChecker.validateHcl(passport), 
                       PassportChecker.validateEcl(passport), 
                       PassportChecker.validatePid(passport)])
        
        return False

    def validateByr(passport):
        # Return true if birth year is valid
        # four digits; at least 1920 and at most 2002
        
        byr = passport.get("byr")
        if type(byr) == str:
            byr = int(byr)
            if 1920 <= byr <= 2002:
                return True
            
        return False

    def validateIyr(passport):
        # Return true if issue year is valid
        # four digits; at least 2010 and at most 2020
        iyr = passport.get("iyr")
        if type(iyr) == str:
            iyr = int(iyr)
            if 2010 <= iyr <= 2020:
                return True
        
        return False

    def validateEyr(passport):
        # Return true if expiration year is valid
        # four digits; at least 2020 and at most 2030
        eyr = passport.get("eyr")
        if type(eyr) == str:
            eyr = int(eyr)
            if 2020 <= eyr <= 2030:
                return True
       
        return False

    def validateHgt(passport):
        # Return true if height is valid
        # a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76
        hgt = passport.get("hgt")
        if type(hgt) == str:
            if "cm" in hgt:
                hgt = hgt.replace("cm","")
                hgt = int(hgt)
                if 150 <= hgt <= 193:
                    return True
            elif "in" in hgt:
                hgt = hgt.replace("in","")
                hgt = int(hgt)
                if 59 <= hgt <= 76:
                    return True

        return False

    def validateHcl(passport):
        # Return true if hair colour is valid
        # a # followed by exactly six characters 0-9 or a-f
        hcl = passport.get("hcl")
        if type(hcl) == str:
            if re.match("^#[0-9a-f]{6}",hcl):
                return True
            
        return False
                        
    
    def validateEcl(passport):
        # Return true if eye colour is valid
        # exactly one of: amb blu brn gry grn hzl oth
        expectedValues = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        ecl = passport.get("ecl")
        if type(ecl) == str:
            if ecl in expectedValues:
                return True
            
        return False

    def validatePid(passport):
        # Return true if passport id is valid
        # a nine-digit number, including leading zeroes
        pid = passport.get("pid")
        if type(pid) == str:
            if re.match("\d{9}",pid):
                return True
        
        return False