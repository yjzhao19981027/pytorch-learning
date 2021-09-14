import xlrd

file_refered = 'soybean_SNP_new.txt'            #对照文件
file_input = 'soybean_geen_pair_SNP.txt'        #需要填充的源文件
file_output = 'soybean_geen_pair_SNP_new.txt'   #填充完的新文件


def save_SNP(dic, line, line_num, type):
    new_line = ""
    cnt = 0
    for i in line:
        if i == '\t':
            cnt += 1
            continue
        if type == 1:
            if cnt == 5:
                new_line += i
            if cnt > 5:
                break
        elif type == 2:
            if cnt == 6:
                new_line += i
            if cnt > 6:
                break
    pair = {new_line: line_num}
    dic.update(pair)


def get_nth(line, n):
    word = ""
    cnt = 0
    for i in line:
        if i == '\n':
            break
        if i == '\t':
            cnt += 1
            continue
        if cnt == n:
            word += i
        if cnt > n:
            break
    return word


def get_line(the_file_path, line_number):
    if line_number < 1:
        return ''
    for cur_line_number, line in enumerate(open(the_file_path, 'r')):
        if cur_line_number == line_number - 1:
            return line
    return ''


def get_head(line):
    word = ""
    cnt = 0
    for i in line:
        if i == '\n':
            break
        if i == '\t':
            cnt += 1
        word += i
        if cnt == 6:
            break
    return word


file = open(file_refered, 'r')
line = file.readline()
line = file.readline()
line_num = 2
snp_dic = {}
# 将对照文件中snp1和snp2存入字典,即一个snp号对应一个行数
while line != "":
    if line_num < 15475:
        save_SNP(snp_dic, line, line_num, 1)
    else:
        save_SNP(snp_dic, line, line_num, 2)
    line_num += 1
    line = file.readline()

# 打开输入文件
# input_file = open(file_input, 'r')
# output_file = open(file_output, 'w')
input_file = open('soybean_geen_pair_SNP.txt', 'r')
output_file = open("test1.txt", 'w')
# 写第一行（属性行）
line = input_file.readline()
output_file.write(line)
print(line)

flag = 0
line = input_file.readline()
while line != "":
    # 去掉后面空格
    new_line = get_head(line)
    snp1 = get_nth(line, 2)
    snp2 = get_nth(line, 3)
    snp1_line_num = snp_dic[snp1]
    snp2_line_num = snp_dic[snp2]
    line1 = get_line(file_refered, snp1_line_num)
    line2 = get_line(file_refered, snp2_line_num)
    for j in range(1, 2215):
        word = ""
        word += get_nth(line1, j + 8)
        word += get_nth(line2, j + 8)
        new_line += word + '\t'
    print(new_line)
    new_line += '\n'
    output_file.write(new_line)
    line = input_file.readline()
