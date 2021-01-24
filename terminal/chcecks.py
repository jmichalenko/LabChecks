import check50
import check50.c

@check50.check()
def exists():
    """apt1"""
    check50.exists("/apt1/bathroom/bathroom_cabinet.txt")

@check50.check()
def exists():
    """apt1/bathroom exists"""
    check50.exists("/apt1/kitchen/cabinet/cabinet_contents.txt")
    
