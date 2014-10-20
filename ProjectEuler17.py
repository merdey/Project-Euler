num_to_text = {1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
            }

def numText(num):
    if num == 1000:
        return 'onethousand' #saves me coding for thousands for the sake of one number
    if num in num_to_text:
        return num_to_text[num]
    else:
        hundreds = int(num / 100)
        num -= (hundreds * 100)
        tens = int(num / 10)
        num -= (tens * 10)
        ones = num

        s = ''
        if hundreds:
            s += num_to_text[hundreds] + 'hundred'
            if tens or ones:
                s += 'and'
        if tens:
            if tens == 1:
                s += num_to_text[tens * 10 + ones]
                return s
            else:
                s += num_to_text[tens * 10]
        if ones:
            s += num_to_text[ones]
        return s

letter_total = 0
for i in range(1, 1001):
    letter_total += len(numText(i))
print(letter_total)

