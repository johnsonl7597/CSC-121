# This program will determine the amount of change the cashier 
# would give to custumer if dollar is paid.
# CSC-121, Fewest Change
# 29 Jan. 2022
# Lilee Johnson
# -------------------------PSEUDOCODE-------------------------
# ask user for price of item under a dollar
# calcuate change (quarters, dimes, nickles, pennies)
# display change
# ------------------------------------------------------------
import sys
DOLLAR = 100
QUARTERS = 25
DIMES = 10
NICKLES = 5
PENNIES = 1
price = int(input("Enter price for item in cents(100 cents or less) > "))
change = DOLLAR - price
def main():
    print(f'\nPrice total is {price}, and a dollar was given.',
          "\n\nThe change is: ")
    cal_dollar()
    cal_quarter()
    cal_dime()
    cal_nickle()
    cal_penny()
    
def cal_dollar():
    if change == 0:
        print("...there is NO change")
    if change < 0:
        print("\n!!You do not have enough for this item, ",
              "restart and enter price that is under 100 cents!!\n")
        sys.exit()
        
def cal_quarter():
    numQ = change // QUARTERS
    print("Quarters: ", numQ)
    
def cal_dime():
    remain = change % QUARTERS
    numDi = remain // DIMES
    print("Dimes:    ", numDi)
    
def cal_nickle():
    remain = change % QUARTERS
    dime = remain % DIMES
    numN = dime // NICKLES
    print("Nickles:  ", numN)
    
def cal_penny():
    remain = change % NICKLES
    numP = remain // PENNIES
    print("Pennies:  ", numP)
    
main()