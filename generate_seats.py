def generate_seats_data():
    MAX_ROWS = 24
    MAX_COLS = 33
    seats_list = []

    # 座位排數
    top_row = list(range(23, 13, -1)) #[23, 22, 21, 20, 19, 18, 17, 16, 15, 14]
    bottom_row = list(range(13, 0, -1)) # [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # 座位號碼
    left_cols = list(range(31, 12, -2))  # [31, 29, 27, 25, 23, 21, 19, 17, 15, 13]
    middle_cols = list(range(11, 0, -2)) + list(range(2, 13, 2)) # [11, 9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12]
    right_cols = list(range(14, 33, 2)) # [14, 16, 18, 20, 22, 24, 26, 28, 30, 32]


    # 上半部
    for i in top_row:
        # 左上C區
        for j in left_cols:
            seats_list.append({"area": "C", "row": i, "col":j, "sold": 0})
        #中上B區
        for j in middle_cols:
            seats_list.append({"area": "B", "row": i, "col":j, "sold": 0})
        #右上C區
        for j in right_cols:
            seats_list.append({"area": "C", "row": i, "col":j, "sold": 0})

    # 下半部
    for i in bottom_row:
        #左下B區
        for j in left_cols:
            seats_list.append({"area": "B", "row": i, "col":j, "sold": 0})
        #中下A區
        for j in middle_cols:
            seats_list.append({"area": "A", "row": i, "col":j, "sold": 0})
        #右下B區
        for j in right_cols:
            seats_list.append({"area": "B", "row": i, "col":j, "sold": 0})

    return seats_list


# [{'area': 'C', 'row': 23, 'col': 31, 'sold': 0},
#  {'area': 'C', 'row': 23, 'col': 29, 'sold': 0},
#  {'area': 'C', 'row': 23, 'col': 27, 'sold': 0},
#  {'area': 'C', 'row': 23, 'col': 25, 'sold': 0},
#  {'area': 'C', 'row': 23, 'col': 23, 'sold': 0},
#  {'area': 'C', 'row': 23, 'col': 21, 'sold': 0},
#  {'area': 'C', 'row': 23, 'col': 19, 'sold': 0},
#  {'area': 'C', 'row': 23, 'col': 17, 'sold': 0},
# ......
# ......