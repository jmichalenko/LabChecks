import check50
import check50.c

@check50.check()
def exists():
    """dowhile.c exists"""
    check50.exists("dowhile.c")

@check50.check(exists)
def compiles():
    """dowhile.c compiles"""
    check50.c.compile("dowhile.c", lcs50=True)

@check50.check(compiles)
def 2():
    """responds to nuber of 2"""
    check50.run("./dowhile").stdin("2").stdout("Thank you for the 2!").exit()
    
@check50.check(compiles)
def 10():
    """responds to number of 10"""
    check50.run("./dowhile").stdin("10").stdout("Thank you for the 10!").exit()
    
@check50.check(compiles)
def 1():
    """responds to number of 1"""
    check50.run("./dowhile").stdin("1").stdout("Thank you for the 1!").exit()


