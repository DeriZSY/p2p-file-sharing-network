CHARACTER_SET = "UTF-8"

NUMBER_MESSAGE_WIDTH = 8
BYTE_ORDER = "big"


def request_file_message(file_name):
    message_header = "REQFILE ".encode(CHARACTER_SET)

    # Need to be able to encode utf-8 file file_names
    file_name_bytes = file_name.encode(CHARACTER_SET)
    file_name_bytes_len = len(file_name_bytes).to_bytes(NUMBER_MESSAGE_WIDTH, BYTE_ORDER)


    payload = message_header + file_name_bytes_len + file_name_bytes
    return payload


def file_not_found_message():
    message_header = "FNF     ".encode(CHARACTER_SET)
    return message_header
