list_1 = [i+1 for i in range(30)]
while True:
    try:
        attend = int(input().rstrip())
        list_1.remove(attend)
    except:
        break
for i in list_1:
    print(i)