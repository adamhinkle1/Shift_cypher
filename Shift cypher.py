check = True;
word = input("input shift cipher encrypted message: ")
word = word.replace(' ','')
def hit(message):  # function will check if the incoming string contains any of these very common words.
    commonWords = ['the', 'and', 'was', 'are','for','have','with','from','what','would','about','who','that','him','her','does']
    flag = False
    for word in commonWords:
        if message.find(word) != -1:
            flag = True
    return flag

for i in range(1,26):  # test shift the cipher text each 25 positions
    shift = i
    new = []
    for j in range(len(word)):
            n = ord(word[j])-shift
            if n < ord('a'):
                n += 26
            elif n > ord('z'):
                n += -26
            new += chr(n)
    str1 = ''.join(new)
    if hit(str1):  # only display the shifted message if it passes the hit() function test
        print("encrypted message is: \n");
        print(str1)
        check = False;
if (check):
    print("Sorry, couldn't identify the correct message.");
