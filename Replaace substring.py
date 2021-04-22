text=input("Text: ")
pattern=input("Substring to replace: ")
sub=input("Substring to replace with: ")
for i in range(0, len(text)):
    for j in range(i, len(text)):
        if (text[i:j + 1] == pattern):
            str1 = text[:i]
            str2 = sub
            str3 = text[j + 1:]
            text = str1 + str2 + str3
print(text)