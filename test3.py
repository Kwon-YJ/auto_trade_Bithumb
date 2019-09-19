mixlist = ['apple',5,'banana','grape',3,8,6,'lemon']

for i in range(len(mixlist)):
    if type(mixlist[i])==str:
        print(mixlist[i]+"의 타입은 str입니다")
    else:
        print(str(mixlist[i])+ "의 타입은 int 입니다")