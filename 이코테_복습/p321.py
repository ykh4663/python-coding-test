n = int(input())
string_n = str(n)
len_n = len(string_n)
lst1 = []
lst2 = []
for i in range(len_n):
    if(i < len_n // 2):
        lst1.append(int(string_n[i]))
    else:
        lst2.append(int(string_n[i]))


if(sum(lst1) == sum(lst2)):
    print("LUCKY")
else:
    print("READY")
