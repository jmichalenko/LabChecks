import check50
import check50.c

@check50.check()
def exists():
    """typecasting.c exists"""
    check50.exists("typecasting.c")

@check50.check(exists)
def compiles():
    """typecasting.c compiles"""
    check50.c.compile("typecasting.c", lcs50=True)

@check50.check(compiles)
def typecast():
    """moves string value by one"""
    check50.run("./typecasting").stdin("John").stdout("Kpio").exit()
