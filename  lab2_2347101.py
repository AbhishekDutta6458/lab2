#1_LIST

#given list divisible by 3 or not:
listcomp=[24,18,60,36,48,54,24,54]
newlist=[a if a%3==0 else "Number is not divisible by 3" for a in listcomp]
print("Updated list is:",newlist)

#square of even numbers in a list:
newlist1=[b**2 if b%2==0 else "Number is not even" for b in listcomp]
print("New list is:",newlist1)

#sum of digits of all even numbers in a list:

def sod(y):
    s=0
    temp=y
    while(temp>0):
        r=temp%10
        s=s+r
        temp=int(temp/10)
    return s
    
newlist2=[sod(y) if y%2==0 else "Not possible" for y in listcomp]
print("Therefore the list is:",newlist2)


#remove duplicate numbers in a list:

remove_duplicate_list=[]
[remove_duplicate_list.append(c) for c in listcomp if c not in remove_duplicate_list]
print(remove_duplicate_list)

#2_dictionary
#dictionary problem:
passenger1=  {"Abhishek Dutta": "28 October 2000", "Raamesh Yadav": "25 October 1987", "Manish Pandey":
"10 September 1989", "Rohit Sharma": "30 April 1987", "Ravindra Jadeja": "6 December1988", "Hardik Pandya": "11 October 1993" }
def birthdate(name):
    print (passenger1[name])
birthdate("Abhishek Dutta")


















    
      