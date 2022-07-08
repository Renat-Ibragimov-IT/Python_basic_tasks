options = {
       'R':['*****','*   *','*   *','*****','**   ','* *  ','*  * ','*   *'],
       'E':['*****','*    ','*    ','**** ','*    ','*    ','*    ','*****'],
       'N':['*   *','**  *','* * *','*  **','*   *','*   *','*   *','*   *'],
       'A':['  *  ',' * * ',' * * ','*   *','*****','*   *','*   *','*   *'],
       'T':['*****','  *  ','  *  ','  *  ','  *  ','  *  ','  *  ','  *  ']
       }

def print_big(newList):
   for i in range(8):
       for j,_ in enumerate(newList):
           print(options[newList[j]][i]+"   ",end = " ")
       print()

name = "RENAT"
print_big(list(name))
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
from art import *
Art=text2art("Renat",font='block',chr_ignore=True)
print(Art)

print(text2art("Renat","white_bubble"))

tprint("Renat")

