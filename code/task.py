from passportChecker import PassportChecker

def countPassports(passportList):
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validPassports = 0

    for passport in passportList:
            if all(key in passport for key in requiredFields):
                 validPassports += 1
    
    return validPassports

      
                     
passports = PassportChecker("input/input.txt")
passports = passports.toList()
print(countPassports(passports))