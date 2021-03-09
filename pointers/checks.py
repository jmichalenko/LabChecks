import check50
import check50.c

@check50.check()
def exists():
    """pointers.c exists"""
    check50.exists("pointers.c")
    check50.include("1.txt")

@check50.check(exists)
def compiles():
    """pointers.c compiles"""
    check50.c.compile("pointers.c", lcs50=True)
    
@check50.check(compiles)
def numbers_add_up_correctly():
    """First line is lower case, second line is uppercase"""
    out = check50.run("./pointers").stdin("john").stdout(open("1.txt").read())
