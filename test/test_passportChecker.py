from code.passportChecker.py import passportChecker

def test_innit(Pfile):
    passports = passportChecker(pFile)
    print(passports)

test_innit("../input/input.txt")