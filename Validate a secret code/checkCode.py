def checkCode(input):
    letter=input[2]
    vowels=["A","E","I","O","U","Y"]
    RemoveString=(input.replace(input[2],"").replace(input[6],""))
    ConvertToList=list(RemoveString)
    for i in range(0,len(ConvertToList)):
        ConvertToList[i]=int(ConvertToList[i])
        ListInt=ConvertToList
    print(ListInt)
    if (letter.upper() not in vowels and
        (ListInt[0]+ListInt[1])%2==0 and
        (ListInt[2]+ListInt[3])%2==0 and
        (ListInt[3]+ListInt[4])%2==0 and
        (ListInt[5]+ListInt[6])%2==0):
        print("valid")
    else:
        print("invalid")
checkCode("11B242-73")
