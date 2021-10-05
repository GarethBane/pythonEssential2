################################ MODULE 2 LABS

# LAB: 2.3.1.18 Your own split
# write your own function, which behaves almost exactly like the original split() method
def mysplit(strng):
    loop = True
    list = []
    while loop:
        strng += " "
        strng = strng.lstrip()
        if strng == "":
            return list
            loop = False
        else:
            ws = strng.index(" ")
            text = strng[0:ws]
            list.append(text)
            strng = strng.replace(text, "", 1)

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

# LAB: 2.4.1.6 A LED Display
# This blew my mind and im still trying to work it out.
digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]

def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)

print_number(int(input("Enter the number you wish to display: ")))

# LAB: 2.5.1.7 Palindromes
#This lab takes a text and checks if its a palindromes, meaning if the text was reversed would it spell out the same word(s)
def palindrome(string):
	list = []
	new_string = string.upper() # 1. Create a new string and turns the input text to all uppercase
	new_string = new_string.replace(" ", "") # 2. Removes all white space
	for i in range(len(new_string)): # 3. Iterates through the string
		list.insert(0, new_string[i]) # 4. Adds each character into a list in reverse order - through insert

	reversed_str = "".join(list) # 5. Converts the list back into a string

	if new_string == "": # 6. If the original list is empty, It's not a palindrome
		print("It's not a palindrome")
	elif reversed_str == new_string: # 7. Compares the two formatted strings if a match, It's a palindrome
		print("It's a palindrome")
	else: # If both fail send a message back, It's not a palindrome
		print("It's not a palindrome")

palindrome("Eleven animals I slam in a net")
palindrome("Ten animals I slam in a net")

# DSs solution!
text = input("Enter text: ")

# remove all spaces...
text = text.replace(' ','')

# ... and check if the word is equal to reversed itself
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("It's a palindrome")
else:
	print("It's not a palindrome")

# LAB: 2.5.1.8 LAB: Anagrams

def anagram(a,b):
    c = ""
    new_a = a.strip()
    new_b = b.strip()
    not_anagram = "Not anagrams!"
    is_anagram = "Are anagrams!"
    for i in new_a.lower():
        if i not in new_b.lower():
            return not_anagram
        else:
            c += i
    if len(c) == len(new_b):
        return is_anagram
    else:
        return not_anagram

print(anagram("Listen ", "Silent"))

# DS's SOLUTION !
str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
if len(strx_1) > 0 and strx_1 == strx_2:
	print("Anagrams")
else:
	print("Not anagrams")

# LAB: 2.5.1.9 The Digit of Life:
# Some say that the Digit of Life is a digit evaluated using somebody's birthday.
# It's simple - you just need to sum all the digits of the date.
# If the result contains more than one digit, you have to repeat the addition until you get exactly one digit.
# For example:
# 1 January 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
bday = input("Please enter your bday in YYYYMMDD: ")
x = 0
repeat = True
while repeat:
    for i in bday:
        x += int(i)
    bday = str(x)
    if len(bday) > 1:
        x = 0
    else:
        print(bday)
        repeat = False

# DSs SOLUTION:
date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
if len(date) != 8 or not date.isdigit():
    print("Invalid date format.")
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print("Your Digit of Life is: " + date)

bday = input("Please enter your bday in YYYYMMDD: ")

# LAB: 2.5.1.10 LAB: Find a word!
# Find the characters for a given word in a text of strings
# If there is a complete match print a message if there is a match print an appropriate message.
def find_a_word(word, text):
	count = ""
	for chr in word.upper():
		if text.upper().find(chr) == -1:
			break
		else:
			count += chr
	if count == word.upper():
		print("Word found!")
	else:
		print("Word not found")

find_a_word("donor", "Nabucodonosor")
find_a_word("donut", "Nabucodonosor")

# DS's SOLUTION:
word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start)
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Yes")
else:
	print("No")

