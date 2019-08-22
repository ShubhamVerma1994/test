#!/usr/bin/env python
# coding: utf-8

# In[1]:




def new_Account():
    acc_num = int(input("enter a account number:"))
    list1 = ["Name", "Address","Phone","ID","Amount"]
    list2 = []
    for items in list1:
        list2.append(input("Enter %s:"%item))
    #store data
    data[acc_num]=dict(zip(list1, list2))
    
    print("------datastore-------")

def exixting_account():
    acc_num = int(input("enter a account number:"))
    if acc_num in data:
        print("------data found------")
        ch = int(input(".New Account\n2.Exixting account\n3.Exit\nEnter your choice:"))
        if ch ==1:
            print("avaliable balance:"data[acc_num]["Amount"])
        elif ch ==2:
            amt = int(input("Enter the amount to withdraw"))
            final_amt = int(data[acc_num]["Amount"]) - amt
            print("Withdraw successful!! avaliable balance is", final_amt)
            #add one more condition to check mininum bal before withdraw
            #update dictionary
        elif ch == 3:
            amt = int(input("Enter the amount to deposite"))
            final_amt = int(data[acc_num]["Amount"]) + amt
            print("deposite successful!! avaliable balance is", final_amt)
    else:
        print("-----data not found-------")
while True:
    ch = int(input1(".New Account\n2.Exixting account\n3.Exit\nEnter your choice:"))
    if ch == 1:
        new_Account()
    elif ch == 2:
        exixting_account()
    elif ch == 3:
        break
    else:
        break
        
    


# In[ ]:




