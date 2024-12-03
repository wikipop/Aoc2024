import re

with open("input.txt") as f:
    lines = f.read()
    output = re.findall(r"mul\(\d{1,3},\d{1,3}\)", lines)
    for i in range(len(output)):
        output[i] = re.findall(r"\d{1,3}", output[i])
        output[i] = int(output[i][0]) * int(output[i][1]) # Multiplication
    print(sum(output))

with open("input.txt") as f:
    output = re.findall(r"(^|do\(\))(.*?)(don't\(\)|$)", lines, flags=re.DOTALL)
    for i in range(len(output)):
        output[i] = re.findall(r"mul\(\d{1,3},\d{1,3}\)", output[i][1])
        for j in range(len(output[i])):
            output[i][j] = re.findall(r"\d{1,3}", output[i][j])
            output[i][j] = int(output[i][j][0]) * int(output[i][j][1]) # Multiplication
        output[i] = sum(output[i])

    print(sum(output))