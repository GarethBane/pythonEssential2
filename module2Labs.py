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
#This lab takes a text and checks if its a palindromes, meaning if the the text was reversed would it spell out the same word(s)
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