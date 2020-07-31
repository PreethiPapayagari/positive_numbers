input_string = input("Enter a list elements separated by space :")
List = input_string.split()
for i in range(len(List)):
    if int(List[i])>=0:
        print(List[i],end=",")
