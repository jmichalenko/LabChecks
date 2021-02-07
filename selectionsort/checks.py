import check50
import check50.c

@check50.check()
def exists():
    """selection.c exists"""
    check50.exists("selection.c")

@check50.check(exists)
def compiles():
    """selection.c compiles"""
    check50.c.compile("selection.c", lcs50=True)

@check50.check(compiles)
def test1():
    """sorts numbers in array correctly"""
    out = check50.run("./selection").stdout("0 1 2 3 4 5 6 7 8 9")
