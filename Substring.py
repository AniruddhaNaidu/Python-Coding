def pattern_search(text, pattern):
    # return text.count(pattern)
    count = 0
    for i in range(len(text)):
        nxt_len = i + len(pattern)
        if (text[i:nxt_len] == pattern):
            count += 1

    return count


# Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result = pattern_search(text, pattern)
print("The given text:", text)
print("Pattern:", pattern)
print("No. of occurrences of the pattern :", result)