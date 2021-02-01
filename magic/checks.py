import check50
import check50.c

@check50.check()
def exists():
    """magic.c exists"""
    check50.exists("magic.c")
    check50.include("1.txt")

@check50.check(exists)
def compiles():
    """magic.c compiles"""
    check50.c.compile("magic.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles an input of 10 correctly"""
    out = check50.run("./magic").stdin("10").stdout(open("1.txt").read())
