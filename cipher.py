"""
Your mission if you choose to accept it.. (you really have no choice)
is to create an encryption key and a decryption key
using the alphabet.

You can use the Caesar Cipher or a Random Alphabet Cipher.

You will need to create a string for the alphabet.
Then a string that has the coded alphabet.

encode():
You will need to check each letter of 'theString' with
each letter of the alphabet, then change it to the coded letter.

decode():
You will need to do the exact opposite of what you did in encode()

"""



def encode(theString):
    eString = ""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    omega = "JKLMNOPQRSTUVWXYZABCDEFGHI" #RANDOM/SHIFTED ALPHABET, Use ALL CAPS
    for x in theString:
        eString = eString + omega[alpha.find(x)]
        
        #Since this is a super secret spy mission, you MUST delete these comments
        #you will need to FIND each letter of the string
        #in the alphabet, then add the coded letter to the
        #encrypted string
        
    return eString
    

def decode(theString):
    dString = ""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    omega = "JKLMNOPQRSTUVWXYZABCDEFGHI" #RANDOM/SHIFTED ALPHABET, Use ALL CAPS
    for x in theString:
        if ((x != " ") or int("9")):
            dString = dString + alpha[omega.find(x)]
        
        #Since this is a super secret spy mission, you MUST delete these comments
        #you will need to FIND each letter of the encrypted word
        #in the coded alphabet, then add the decoded letter to the
        #decrypted string
        dString = dString #+ something
        
    return dString

# Test cases...

wordList = ["Hello", "Ciphers are fun!", "This Sunday is Valentine's day.","CyWoods","Computer Science 1 K","John Wayne"]
for x in wordList:
    encoded = encode(x.upper())
    decoded = decode(encoded)
    print ("'" + x + "' decodes to '" + encoded + "' and back to '" + decoded + "'")
    
#outputs: 
#    'Hello' decodes to 'QNUUX' and back to 'HELLO'
#    'Ciphers are fun!' decodes to 'LRYQNABIJANIODWI' and back to 'CIPHERSZAREZFUNZ'
#    'This Sunday is Valentine's day.' decodes to 'CQRBIBDWMJHIRBIEJUNWCRWNIBIMJHI' and back to 'THISZSUNDAYZISZVALENTINEZSZDAYZ'
#    'CyWoods' decodes to 'LHFXXMB' and back to 'CYWOODS'
#    'Computer Science 1 K' decodes to 'LXVYDCNAIBLRNWLNIIIT' and back to 'COMPUTERZSCIENCEZZZK'
#    'John Wayne' decodes to 'SXQWIFJHWN' and back to 'JOHNZWAYNE'
