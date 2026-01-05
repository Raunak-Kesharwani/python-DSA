import random as r
class bank:
    def __init__(self):
        self.passbook=r.randint(0,1000)
        self.balance= self.passbook
        
        print("passbook=",self.passbook,"balance=",self.balance)
        self.data=[]
        self.transaction=len(self.data)

    def read(self):
        return self.passbook, self.balance
    
    def credit(self):
        amount=int(input("enter amount:"))
        self.data.append(amount)
        self.balance+=amount
        return self.balance
        
    def debit(self):
        amount=int(input("enter amount:"))
        self.data.append(-amount)
        self.balance-=amount
        return self.balance
        
    def commit(self):
        self.data.clear()
        self.passbook= self.balance
        return self.passbook
   
    def abort(self):
            if not self.data :
                print("thier is no last transction")
                return ""
            else:
                t_num=int(input("Transaction number:"))
                if t_num == len(self.data):
                    return self.balance+self.data[(t_num-1)]
                else:
                    print("please enter valid transaction number")
                    return self.abort()

    def rollback(self):
        for i in self.data:
            self.balance+=i
        self.data.clear()
        return self.balance

def main():
    ob=bank()
    N=int(input("enter number of operation to be perforemed:"))
    print("choose the operation from read credit debit commit abort & rollback ")
    
    for i in range (1,N+1):
        operations=input().strip()
        if operations=="read":
            print(ob.read())
        elif operations=="credit":
            print(ob.credit())
        elif operations=="debit":
            print(ob.debit())
        elif operations=="commit":
            print(ob.commit())
        elif operations=="abort":
            print(ob.abort())
        elif operations=="rollback":
            print(ob.rollback())
        else:
            print("wrong input")



if __name__ == "__main__":
    main()
    
    

