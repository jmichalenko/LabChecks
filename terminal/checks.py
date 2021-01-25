import check50
import check50.c

@check50.check()
def exists():
    """Kitchen_cabinet.txt exists"""
    check50.exists("./kitchen/cabinet/cabinet_contents.txt")
    
@check50.check()
def exists():
    """Bathroom_cabinet.txt exists"""
    check50.exists("./apt1/bathroom/bathroom_cabinet/bathroom_cabinet.txt")
    
