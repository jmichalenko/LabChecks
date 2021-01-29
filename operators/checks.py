import check50
import check50.c

@check50.check()
def exists():
    """operators.c exists"""
    check50.exists("operators.c")
    check50.include("1.txt")
    check50.include("2.txt")

@check50.check(exists)
def compiles():
    """datatypes.c compiles"""
    check50.c.compile("operators.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles inputs correctly"""
    out = check50.run("./operators").stdin(open("2.txt").read()).stdout(open("1.txt").read())
