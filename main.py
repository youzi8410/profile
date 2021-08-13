def check_first_line(first_line):
    line1_ok = False
    line1_list = first_line.split()
    if len(line1_list) != 3 \
            or check_digit(first_line) == False \
            or int(line1_list[1]) < 1 \
            or int(line1_list[0]) < int(line1_list[1]) \
            or int(line1_list[0]) > 1000 \
            or int(line1_list[2]) < 0 \
            or int(line1_list[0]) > 10000\
            or int(line1_list[0]) < 1:
        print("The first line of input must contains three integers(N,H,L).\n" +
              "(1<=H<N<=1000, 0<=L<=10000)\nEnter line1 again...")
        line1_ok = False
    else:
        global movies_count
        global second_line_len
        global similar_count
        second_line_len = int(line1_list[1])
        movies_count = int(line1_list[0])
        similar_count = int(line1_list[2])
        line1_ok = True
    return line1_ok

def check_second_line(second_line):
    line2_ok = False
    line2_list = second_line.split()
    if len(line2_list) != second_line_len\
            or check_digit(second_line) == False\
            or check_id(second_line) == False:
        print("The second line contains H unique space-separated intergers which<N " +
              "denoting the ID of the movies on the horror list.\nEnter line2 again...")
        line2_ok = False
    else:
        line2_ok = True
    return line2_ok

def check_similar(similar_line, list_num):
    similar_ok = False
    similar_each_list = similar_line.split()
    if len(similar_each_list) != 2\
            or check_digit(similar_line) == False\
            or check_id(similar_line) == False:
        print("The following L lines contains H two space-separated, which both<N" +
              "denoting the movie with both ID are similar.\n Enter similar list " +
              list_num.__str__() + " again...")
        similar_ok = False
    else:
        similar_list.append(similar_each_list)
        similar_ok = True
    return similar_ok

def check_digit(check):
    check_list = check.split()
    for i in range(0, len(check_list)):
        if not check_list[i].isdigit():
            return False

def check_id(id):
    id_list = id.split()
    for j in range(0, len(id_list)):
        if int(id_list[j]) >= movies_count\
                or int(id_list[j]) < 0:
            return False

def cal_most_horror():
    print(similar_list)
    print(similar_list[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global similar_list
    similar_list = []
    line1 = input("Sample Input(N,H,L) :\n")
    while check_first_line(line1) == False:
        line1 = input("Sample Input(N,H,L) :\n")
    line2 = input()
    while check_second_line(line2) == False:
        line2 = input()
    for k in range(1, similar_count + 1):
        similar_movies = input()
        while check_similar(similar_movies, k) == False:
            similar_movies = input()
    cal_most_horror()
 #   print("Sample Output\n" + cal_most_horror())
