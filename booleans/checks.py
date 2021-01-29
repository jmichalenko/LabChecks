import check50
import check50.c

@check50.check()
def exists():
    """booleans.c exists"""
    check50.exists("booleans.c")

@check50.check(exists)
def compiles():
    """boolean.c compiles"""
    check50.c.compile("booleans.c", lcs50=True)

@check50.check(compiles)
def A():
    """responds to grade 90-100"""
    check50.run("./booleans").stdin("90").stdout("You get an A!").exit()

@check50.check(compiles)
def B():
    """responds to grade 80-89"""
    check50.run("./booleans").stdin("89").stdout("You get a B!").exit()
    
@check50.check(compiles)
def C():
    """responds to grade 70-79"""
    check50.run("./booleans").stdin("75").stdout("You get a C!").exit()

@check50.check(compiles)
def D():
    """responds to grade below 70"""
    check50.run("./booleans").stdin("69").stdout("You need to work harder to pass this class").exit()
