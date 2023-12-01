def str_to_digit(digitStr):
    digit_strs = {
        "one": 1, 
        "two": 2,
        "three": 3,
        "four": 4, 
        "five": 5, 
        "six": 6, 
        "seven": 7, 
        "eight": 8, 
        "nine": 9
    }

    for d in list(digit_strs.keys()):
        if d in digitStr:
            return True, digit_strs[d]
    return False, None

def get_num(inputStr):
    num = ""
    tmp_str = ""
    for c in inputStr:
        if not c.isdigit():
            tmp_str += c
            success, val = str_to_digit(tmp_str)
            if success:
                num += str(val)
                break
        else:
            num += str(c)
            break
    
    reversed = inputStr[::-1]
    tmp_str = ""
    for c in reversed:
        if not c.isdigit():
            tmp_str = c + tmp_str
            success, val = str_to_digit(tmp_str)
            if success:
                num += str(val)
                break
        else:
            num += str(c)
            break
    
    return int(num)


def main():
    total = 0
    # lines = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
    # lines = ["oneeightwo"]
    with open('input.txt') as f:
        lines = f.read().splitlines()
    for l in lines:
        num = get_num(l)
        total += num
    print(f"Total: {total}")
if __name__ == '__main__':
    main()