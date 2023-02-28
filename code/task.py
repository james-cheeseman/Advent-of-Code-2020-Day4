from passportChecker import PassportChecker

def countPassports(passportList):
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validPassports = 0

    for passport in passportList:
            if all(key in passport for key in requiredFields):
                 validPassports += 1
    
    return validPassports

def countValidatedPassports(passportList):
    count = 0
    for passport in passportList:
        if(PassportChecker.validatePassport(passport)):
            count += 1
    
    return count

      
                     
passports = PassportChecker("input/test_input.txt")
passports = passports.toList()

print("Validated Passports: ",countValidatedPassports(passports))

print(countPassports(passports))