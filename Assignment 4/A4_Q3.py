def overlap(list1,list2):
    for item in list1:
        if item in list2:
            return True
    return False
#list1=input("Enter list1 :")
#list2=input("Enter list2 :")
list1=[11,22,34,55]
list2=[85,55,45,78]

result=overlap(list1,list2)
print(result)