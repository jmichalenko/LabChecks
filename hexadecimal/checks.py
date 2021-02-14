import check50
import check50.c

@check50.check()
def exists():
    """hexadecimal.c exists"""
    check50.exists("hexadecimal.c")

@check50.check(exists)
def compiles():
    """bubble.c compiles"""
    check50.c.compile("hexadecimal.c", lcs50=True)

@check50.check(compiles)
def test1():
    """sorts numbers in array correctly"""
    out = check50.run("./hexadecimal").stdout("0 1 2 3 4 5 6 7 8 9")
