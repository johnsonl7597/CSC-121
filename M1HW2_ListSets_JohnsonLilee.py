# This program will practice useing sets and lists.
# CSC-121, M1HW2 - List and Sets
# 21 Jan. 2022
# Lilee Johnson
# ----------------------PSEUDOCODE-----------------------
# ask user for 10 num
# create list list10
# display lowNum, highNum, total, average
# convert list list10 to set listTen
# ---------------------------------------------------------------------
def main():
            listSet(list_10)
            results(list_10)
list_10 = []   
def listSet(list_10):
    count2 = 0
    for x in range(10):
        count2 +=1
        list_10.append(int(input('Enter number ' + str(count2)
                                 + ' of 10 > ')))
    print("\nList_10 list:\n", list_10, "\n")
    return list_10  
def results(list_10):
    lowNum = min(list_10)
    highNum = max(list_10)
    total = sum(list_10)
    average = total / 6
    listTen = set(list_10)
    print("smallest number in List_10: ", lowNum)
    print("LARGEST number in List_10:  ", highNum)
    print("Sum of numbers in List_10:  ", total)
    print("The average in List_10:     ", '{:.2f}'.format(average))
    print("\nListTen set:\n", listTen, "\n")
main()
