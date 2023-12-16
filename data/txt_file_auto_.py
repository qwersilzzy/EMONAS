#
# # learnable_parameters_ones_counting
#
#
# with open('data/search_log/archi100_epoch20_micro_random.txt', 'r') as f:
#     for line in f:
#         line = line.strip()
#         if not line:
#             continue
#         if "learnable_parameters_ones_counting " not in line:
#             continue
#         if "median" in line:
#             continue
#         # print(line)
#         key_products_4 = line.split()
#         # print(key_products_4)
#         key_products_4 = key_products_4[3]
#         print(key_products_4)




def key_word_extraction_1(load_from, key_word):
    with open(load_from, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if key_word not in line:
                continue
            if "median" in line:
                continue
            print(line)

def key_word_extraction_2(load_from, key_word):
    with open(load_from, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if key_word not in line:
                continue
            if "median" in line:
                continue
            key_products_4 = line.split()
            print(key_products_4)

def key_word_extraction_3(load_from, key_word):
    with open(load_from, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if key_word not in line:
                continue
            if "median" in line:
                continue
            key_products_4 = line.split()
            key_products_4 = key_products_4[4]
            print(key_products_4)


def main():
    # learnable_parameters_ones_counting
    # valid_acc
    load_from = 'data/archi100_epoch20_micro_random.txt'
    key_word = "param size"
    # key_word_extraction_1(load_from, key_word)
    # key_word_extraction_2(load_from, key_word)
    key_word_extraction_3(load_from, key_word)
    return

if __name__ == "__main__":
    main()




