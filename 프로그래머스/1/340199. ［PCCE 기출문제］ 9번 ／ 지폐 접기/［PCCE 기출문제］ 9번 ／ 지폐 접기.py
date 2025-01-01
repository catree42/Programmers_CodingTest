def foldBill(bill):
    if bill[0] > bill[1] :
        bill[0] = int(bill[0]/2)
    else : 
        bill[1] = int(bill[1]/2)
    return bill

def check(wallet, bill) :
    if wallet[0] >= bill[0] :
        if wallet[1] >= bill[1]:
            return True
        else : pass 
    if wallet[0] >= bill[1]:
        if wallet[1] >= bill[0]:
            return True
        else : pass
    return False
        

def solution(wallet, bill):
    count = 0
    
    while(True) :
        if(check(wallet,bill) == True):
            break
        else :
            bill = foldBill(bill)
            count += 1 

    return count