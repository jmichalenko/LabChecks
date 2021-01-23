import check50
import check50.c

@check50.check()
def exists():
    """HelloName.c exists"""
    check50.exists("HelloName.c")
    check50.include("1.txt")

@check50.check(exists)
def compiles():
    """HelloName.c compiles"""
    check50.c.compile("HelloName.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles a height of 1 correctly"""
    out = check50.run("./HelloName").stdin("John").stdout()
    check_pyramid(out, open("1.txt").read())

