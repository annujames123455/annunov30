'''
author name:annu james
date:30/11/24
'''
def mobile_number():
    n=input("enter the mobile number:")
    if len(n)==10 and n[1] in '789':
        print("valid")
    else:
        print("invalid")
mobile_number()


