import check50
import check50.c

@check50.check()
def exists():
    """multiplication.c exists"""
    check50.exists("multiplication.c")
    check50.exists("multiplication.h")
    check50.include("1.txt")
    check50.include("2.txt")

@check50.check(exists)
def compiles():
    """mulitiplication.c compiles"""
    check50.c.compile("multiplication.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles inputs correctly"""
    out = check50.run("./multiplication").stdin(3, 4).stdout("The product is: 12")
