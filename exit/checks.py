  
import check50
import check50.c

@check50.check()
def exists():
    """exit.c exists"""
    check50.exists("exit.c")

@check50.check(exists)
def compiles():
    """exit.c compiles"""
    check50.c.compile("exit.c", lcs50=True)

@check50.check(compiles)
def incorrect_arguments():
    """responds to incorrect_arguments"""
    check50.run("./exit").stdout("Usage: ./exit <firstname> <lastname>").exit()

@check50.check(compiles)
def incorrect_arguments_one():
    """responds to only one argument provided"""
    check50.run("./exit John").stdout("Usage: ./exit <firstname> <lastname>").exit()

@check50.check(compiles)
def responds_correctly():
    """responds to correct number of arguments"""
    check50.run("./exit John Michalenko").stdout("Hello, John Michalenko!").exit()
