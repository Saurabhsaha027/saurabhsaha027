def generate(current, index, s, result):
    if current:
        result.append(current)
    for i in range(index, len(s)):
        generate(current + s[i], i + 1, s, result)



s = "abcd"
result = []
generate("", 0, s, result)
result = sorted(result)
print(result)
