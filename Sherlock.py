t = int(input("enter the number of test case"))

for i in range(t):
    pattern = input("enter the pattern you want to check")
    text = input("enter the string you want to check")

    flag = False

    for j in range(len(text)-len(pattern)+1):
        if sorted(text[j:j+len(pattern)]) == sorted(pattern):
            flag = True
            break

    if flag:
        print("YES")
    else:
        print("NO")