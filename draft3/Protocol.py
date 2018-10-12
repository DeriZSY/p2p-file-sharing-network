STR_LENGTH = 8
INT_LENGTH = 8


def str_to_fixed_width_bytes(_str):
    str_len = len(_str)

    output_str = _str
    for i in range(0, STR_LENGTH - str_len):
        output_str += " "

    print(output_str + " " + str(len(output_str)))


def requst_file(file_name):
    file_name_bytes = file_name.encode("UTF-8")
    file_name_len_bytes = len(file_name_bytes).to_bytes(8, "big")
