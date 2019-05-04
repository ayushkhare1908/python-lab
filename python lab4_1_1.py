saving_account= 1500
current_account= 15000
a=input('press 1 for saving / 2 for current account')
if(a==1):
    b=input('press 1 for withdrawal / 2 for deposit')
    if(b==1):
        x=input('amount to withdraw')
        saving_account=saving_account-x;
        if(saving_account< 1000):
            print'less than limit'
        else:
            print saving_account
    else:
        y=input(' 1 for withdrawl / 2 for deposit')
        saving_account=saving_account+y
        if(saving_account< 1000):
            print'less than limit'
        else:
            print'less than limit'
else:
    c=input('press 1 for deposit / 2 for withdrawl')
    if(c==1):
        xy=input('enter amount to withdraw')
        current_account= current_account-xy
        print'less than limit'
    else:
        print current_account
        yx=input('press 1 for withdrwal / 2 for deposit')
        current_account=current_account+yx
        if(current_account< 10000):
            print'less than limit'
        else:
            print current_account
    
