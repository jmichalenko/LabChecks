import check50
import check50.c

@check50.check()
def exists1():
    """apt1 exists"""
    check50.exists("apt1/")
@check50.check()
def exists2():
    """apt1/kitchen/cabinet/cabinet_contents.txt exists"""
    check50.exists("apt1/kitchen/cabinet/cabinet_contents.txt")
@check50.check()
def exists3():
    """apt1/kitchen/fridge exists"""
    check50.exists("apt1/kitchen/fridge")
@check50.check()
def exists4():
    """apt1/living_room exists"""
    check50.exists("apt1/living_room")

