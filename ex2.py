with open("stdin.txt") as f:
    print("Введите слово на английском языке")
    a=input()
    v=0
with open("stdout.txt") as f:
    for i in a:
        v+=ord(i)
    print(v)	
