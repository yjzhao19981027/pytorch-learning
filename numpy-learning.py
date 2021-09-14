file = open('test.txt', 'r')
file_write = open('t.txt', 'r')
line = file.readline()
file_write.write(line)
print(line)
line = file.readline()
while line != "":
    cnt = 0
    new_line = ""
    D_To_0 = ''
    E_To_1 = ''
    for i in line:
        if cnt <= 8 or i == '\t':
            new_line += i
        if i == '\t':
            cnt += 1
        if cnt == 3:
            D_To_0 = i
        if cnt == 4:
            E_To_1 = i
        if cnt >= 8:
            if i == '1':
                new_line += E_To_1
            if i == '0':
                new_line += D_To_0
            if i == "|":
                pass
    line = file.readline()
    file_write.write(new_line + '\n')
    print(new_line)