#ascii value range
#A-Z:65-90
#a-z:97-122
#0-9:48-57
# ord-order
# chr-character
#checking the character is in lowercase
# char="v"
# code=ord(char)
# if code>=97 and code<=122:
#     print("LowerCase")
# else:
#     print("Not a LowerCase")

#checking whether the char is in lower or uppercase
# char="S"
# code=ord(char)
# if code>=97 and code<=122:
#     print("Lowercase")
# elif code>=65 and code<=90:
#     print("uppercase")
# else:
#     print("not an alphabet")

#printing character from ascii value
# char=97
# print(chr(char))

#counting no.of uppercase and lowercase letters
# word="Hari Hara Veeramallu"
# uppercount=0
# lowercount=0
# for i in range(len(word)):
#     code=ord(word[i])
#     if code>=97 and code<=122:
#         lowercount+=1
#     elif code>=65 and code<=90:
#         uppercount+=1
# print(lowercount,uppercount)

#checking the character is lowercase or uppercase or number
def check_char(char):
    code=ord(char)
    if(code>=97 and code<=122):
        print("lowercase char:",chr(code))
    elif(code>=65 and code<=90):
        print("uppercase char:",chr(code))
    elif(code>=48 and code<=57):
        print("number:",char)
    else:
        print("it's not a character,number,it may be special symbol")
check_char("9")

#function to convert vowel character into next character(vigneswari-vjgnfswbrj)
def code_decode(word):
    secret=""
    for i in range(len(word)):
        char=ord(word[i])
        if word[i]=="a"or word[i]=="e"or word[i]=="i"or word[i]=="o"or word[i]=="u" or word[i]=="A" or word[i]=="E" or word[i]=="I" or word[i]=="O"or word[i]=="U":
            secret+=chr(char+1)
        else:
            secret+=word[i]
    print(secret) 

code_decode("vigneswari")




