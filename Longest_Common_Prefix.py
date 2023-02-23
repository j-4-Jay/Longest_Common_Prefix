# str = ["dog23","raceca","car2"]
str = ["flower","flow","flight"]

ans = ""

# print(str[0])
# print(str[-1])
first = str[0]
last = str[-1]

for i in range (len(first)):
    if first[i] != last[i]:
        break
    else:
        ans += first[i]

print(ans)