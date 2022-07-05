# strings concatenation
def concat_way1(string_1 = "", string_2 = ""): 
    return string_1 + string_2

def concat_way2(string_1 = "", string_2 = ""):
    return "{}{}".format(string_1,string_2)

def concat_way3(string_1 = "", string_2 = ""):
    return f"{string_1}{string_2}"

def main():
    first_string = "I'm first!"#input('Write first string here:\n')
    second_string = "I'm the second!"#input('Write second string here:\n')
    print("Concatinations: ")
    print("way 1: ")
    print(concat_way1(first_string, second_string))
    print("way 2: ")
    print(concat_way2(first_string, second_string))
    print("way 3: ")
    print(concat_way3(first_string, second_string))
    input()
if __name__ == '__main__':
    main()
