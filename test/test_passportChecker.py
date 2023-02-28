from passportChecker import PassportChecker

def test_innit(filePath):
    passports = PassportChecker(filePath)
    print(passports)

test_innit("input/input.txt")