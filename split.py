splits = 'the sentence split'

split_val = []
temp = ''
for i in splits:
    if i == ' ':
        split_val.append(temp)
        temp = ''
    else:
        temp += i
if temp:
    split_val.append(temp)
    print(split_val)