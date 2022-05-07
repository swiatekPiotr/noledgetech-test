import os


def packet(path):
    with open(path, mode='r') as open_file:
        packet_dict = {}
        for i in open_file.read().split("\n"):
            if "|" in i:
                packet_dict[str(i.split("|")[0])] = i.split("|")[1]
    return packet_dict


def generate_dictionary(pl_to_en_path, en_to_it_path):
    file_list = os.listdir('/Users/test/internship/dictionaries')
    if 'PLtoEN.dsv' in file_list and 'ENtoIT.dsv' in file_list:
        pl_to_en = packet(pl_to_en_path)
        en_to_it = packet(en_to_it_path)
        path = '/Users/test/internship/dictionaries/output.dsv'
        with open(path, mode='w+') as open_file:
            for i in pl_to_en:
                if pl_to_en[i] in en_to_it:
                    open_file.write(i+"|"+en_to_it[pl_to_en[i]]+"\n")
        print("there is a path to your new file:\n" + path)
        return path
    else:
        print("you don't have the appropriate files in the expected path")


if __name__ == '__main__':
    generate_dictionary('/Users/test/internship/dictionaries/PLtoEN.dsv',
                        '/Users/test/internship/dictionaries/ENtoIT.dsv')
