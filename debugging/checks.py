import check50
import check50.c

@check50.check()
def exists():
    """buggy.c exists"""
    check50.exists("buggy.c")

@check50.check(exists)
def compiles():
    """buggy.c compiles"""
    check50.c.compile("buggy.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles an input of 110 correctly"""
    out = check50.run("./buggy").stdin("110").stdout("110 in binary is 6 in decimal")

@check50.check(compiles)
def test2():
    """rejects non binary number"""
    out = check50.run("./buggy").stdin("33").stdout("Invalid input. Try again!")
'"
