# Unairy Function
from typing import Tuple


def unairy(lst):
    if isinstance(lst, list) == True:
        if lst == []:
            return True
        else:
            cLst = lst.copy()
            if lst[0].lower() == "m":
                cLst.pop(0)
                for i in cLst:
                    if cLst.pop().lower() == "o":
                        continue
                    else:
                        return False
                return True
            elif lst[0].lower() == "o":
                for i in cLst:
                    if cLst.pop().lower() == "o":
                        continue
                    else:
                        return False
                return True  
    else:
        print("not a list")
        return False


# Unairy Is Zero? Function
def uzero(lst):
    if isinstance(lst, list) == True:
        if lst == []:
            return True
        elif lst == ["m"] or lst == ["M"]:
            return True
        else:
            return False
    else:
        print("Not a list")
        return False

# Unairy Is Negitive? Function
def uisneg(lst):
    if isinstance(lst, list) == True:
        cLst = lst.copy()
        if lst == ["m"] or lst == ["M"]:
            return False
        elif lst == []:
            return False
        elif lst[0].lower() == "m":
            cLst.pop(0)
            for i in cLst:
                if cLst.pop().lower() == "o":
                    continue
                else:
                    return False
            return True
        else:
            return False
    else:
        print("Not a list")
        return False
# Unairy Is Positive? Function
def uispos(lst):
    if isinstance(lst, list) == True:
        cLst = lst.copy()
        if lst == ["m"] or lst == ["M"] or lst == []:
            return False
        elif lst[0].lower() == "o":
            for i in cLst:
                if cLst.pop().lower() == "o":
                    continue
                else:
                    return False
            return True
        else:
            return False
    else:
        print("Not a list")
        return False

# Unairy list to number
def u2n(lst):
    if isinstance(lst, list) == True:
        cLst = lst.copy()
        number = 0
        isNeg = False
        if uisneg(lst) == True:
            isNeg = True
            cLst.pop(0)
            for i in range(len(cLst)):
                if cLst.pop().lower() == "o":
                    number += 1
                else:
                    return "not a number"
        elif uispos(lst) == True:
            for i in range(len(cLst)):
                if cLst.pop(0).lower() == "o":
                    number += 1
        if isNeg == False:
            return number
        elif isNeg == True:
            return -number
    else:
        return "not a list"
# Number To Unairy Function
def n2u(num):
    if isinstance(num, int) == True:
        unairyLst = []
        numStr = str(num)
        if numStr[0] == "-":
            unairyLst.append("m")
            noNegitive = numStr[1:]
            for i in range(int(noNegitive)):
                unairyLst.append("o")
            return unairyLst
        else:
            for i in range(int(numStr)):
                unairyLst.append("o")

            return unairyLst
    else:
        return "not a number"

# Positive To Negitive Unary:
def uneg(lst):
    if isinstance(lst, list) == True:
        if unairy(lst) == True:
            cLst = lst.copy()
            if uisneg(lst) == True:
                cLst.pop(0)
                return cLst
            elif uispos(lst) == True:
                cLst[0:0] = ["m"]
                return cLst
        return "not a unairy list"
    else:
        return "Not a list"


def uabs(lst):
    num = u2n(lst)
    if uisneg(lst) == True:
        return num[1:]
    else:
        return num


def uadd(lst1, lst2):
    num1 = u2n(lst1)
    num2 = u2n(lst2)
    answer = num1 + num2
    return answer

def usub(lst1, lst2):
    num1 = u2n(lst1)
    num2 = u2n(lst2)
    answer = num1 - num2
    return answer

def uinc(lst1):
    num1 = u2n(lst1)
    answer = num1 + 1
    return answer

def udec(lst1):
    num1 = u2n(lst1)
    answer = num1 - 1
    return answer
lst1 = ["o"]
lst2 = ["o"]