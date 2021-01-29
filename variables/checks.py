import check50
import check50.c

@check50.check()
def exists():
    """Variables.c exists"""
    check50.exists("variables.c")
    check50.include("1.txt")

@check50.check(exists)
def compiles():
    """variables.c compiles"""
    check50.c.compile("variables.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles an input of 10 correctly"""
    out = check50.run("./variables").stdin("10").stdout(open("1.txt").read())
