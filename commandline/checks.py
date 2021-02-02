import check50
import check50.c

@check50.check()
def exists():
    """commandline.c exists"""
    check50.exists("commandline.c")

@check50.check(exists)
def compiles():
    """commandline.c compiles"""
    check50.c.compile("commandline.c", lcs50=True)

@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("./commandline Emma").stdout("hello, Emma").exit()

@check50.check(compiles)
def blank_rejected():
    """responds to name Rodrigo"""
    check50.run("./commandline").stdout("You need to provide the name in the command line.").exit()
