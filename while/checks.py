import check50
import check50.c

@check50.check()
def exists():
    """while.c exists"""
    check50.exists("while.c")

@check50.check(exists)
def compiles():
    """while.c compiles"""
    check50.c.compile("while.c", lcs50=True)

@check50.check(compiles)
def eighty():
    """responds to nuber of 80"""
    check50.run("./while").stdin("80").stdout("Your number can be doubled 1 times before reaching 100!").exit()
    
@check50.check(compiles)
def four():
    """responds to number of 4"""
    check50.run("./while").stdin("4").stdout("Your number can be doubled 5 times before reaching 100!").exit()
