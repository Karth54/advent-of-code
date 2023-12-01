
def get_num(inputStr):
    num = None
    for c in inputStr:
        if c.isdigit():
            num = str(c)
            break
    
    reversed = inputStr[::-1]
    for c in reversed:
        if c.isdigit():
            num += str(c)
            break
    return int(num)

def main():
    total = 0
    input_list = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    with open('input.txt') as f:
        lines = f.read().splitlines()
    for l in lines:
        num = get_num(l)
        # print(num)
        total += num
    print(f"Total: {total}")
if __name__ == '__main__':
    main()