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