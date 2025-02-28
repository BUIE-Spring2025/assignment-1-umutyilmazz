def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    numStr = str(num)
    if 3999 >= num >= 1000:
        d1, d2, d3, d4 = int(numStr[3]), int(numStr[2]), int(numStr[1]), int(numStr[0])
    elif num >= 100:
        d1, d2, d3, d4 = int(numStr[2]), int(numStr[1]), int(numStr[0]), 0
    elif num >= 10:
        d1, d2, d3, d4 = int(numStr[1]), int(numStr[0]), 0, 0
    elif num >= 1:
        d1, d2, d3, d4 = num, 0, 0, 0
    else: return None
    
    s1 = d4 * "M"
    if d3 in range(1,4):
        s2 = d3 * "C"
    elif d3 == 4:
        s2 = "CD"
    elif d3 in range(5,9):
        s2 = "D" + (d3 - 5) * "C"
    elif d3 == 9:
        s2 = "CM"
    else:
        s2 = ""

    if d2 in range(1,4):
        s3 = d2 * "X"
    elif d2 == 4:
        s3 = "XL"
    elif d2 in range(5,9):
        s3 = "L" + (d2 - 5) * "X"
    elif d2 == 9:
        s3 = "XC"
    else:
        s3 = ""

    if d1 in range(1,4):
        s4 = d1 * "I"
    elif d1 == 4:
        s4 = "IV"
    elif d1 in range(5,9):
        s4 = "V" + (d1 - 5) * "I"
    elif d1 == 9:
        s4 = "IX"
    else:
        s4 = ""

    return s1 + s2 + s3 + s4
