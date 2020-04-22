#import base64
from string import ascii_lowercase as lc, ascii_uppercase as uc

def rot_alpha(n):      #function to make rot functions (I stole this bit off of reddit. I do NOT understand maketrans)
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

JAC1 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "JYRBUIAXGMWENjyrbuiaxgmwenQDSPTCVHFOLZKqdsptcvhfolzk")
'''str.translate("Hello World!", JAC1)''' #usage

JAC1u = str.maketrans( 
    "JYRBUIAXGMWENjyrbuiaxgmwenQDSPTCVHFOLZKqdsptcvhfolzk",
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

JAC2 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "FZOGKYAJTBVIWfzogkyajtbviwRSDNHLCXQMUEPrsdnhlcxqmuep")

JAC2u = str.maketrans( 
    "FZOGKYAJTBVIWfzogkyajtbviwRSDNHLCXQMUEPrsdnhlcxqmuep", 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

JAC3 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "HUZDNMVGWLCXYhuzdnmvgwlcxyTIEOAPSFKBQJRtieoapsfkbqjr")

JAC3u = str.maketrans( 
    "HUZDNMVGWLCXYhuzdnmvgwlcxyTIEOAPSFKBQJRtieoapsfkbqjr", 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

JAC4 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "GSREUFTDVWJXKgsreuftdvwjxkIQCHPBZMNYAOLiqchpbzmnyaol")

JAC4u = str.maketrans( 
    "GSREUFTDVWJXKgsreuftdvwjxkIQCHPBZMNYAOLiqchpbzmnyaol", 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

JAC5 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "SFRAZLCXTBUHVsfrazlcxtbuhvGPQDMOIKJYEWNgpqdmoikjyewn")

JAC5u = str.maketrans( 
    "SFRAZLCXTBUHVsfrazlcxtbuhvGPQDMOIKJYEWNgpqdmoikjyewn", 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

JAC6 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "QRFSPEIZHXGLKqrfspeizhxglkDWOVTAUJMNCBYdwovtaujmncby")

JAC6u = str.maketrans( 
    "QRFSPEIZHXGLKqrfspeizhxglkDWOVTAUJMNCBYdwovtaujmncby", 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

def NUM1(s):
    result = ""
    for v in s:
        c = ord(v)
        c += 20

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result

def NUM1u(s):
    result = ""
    for v in s:
        c = ord(v)
        c -= 20

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result

def NUM2(s):
    result = ""
    for v in s:
        c = ord(v)
        c -= 4

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result

def NUM2u(s):
    result = ""
    for v in s:
        c = ord(v)
        c += 4

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result

def NUM3(s):
    result = ""
    for v in s:
        c = ord(v)
        c += 7

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result

def NUM3u(s):
    result = ""
    for v in s:
        c = ord(v)
        c -= 7

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result

print('Encrypt or Decrypt?')
EorD = input()
encryptions_applied = [ ]
if EorD == 'Encrypt' or EorD == 'encrypt':
    
    print('Enter your message to be encrypted:')
    message = input() #secret message :-)
    print('')
    
    #IT WOULD BE MORE DIFFICULT IF I CONVERT TO BASE64 RIGHT HERE
    
    rot_tf = 'false'
    while rot_tf == 'false':        #this should repeat until the number that is entered is between 1 and 25 for the rot function
        print('Enter a number between 1 and 25')
        rot = int(input())
        
        if 0 < rot < 26:
            rot_tf = 'true'
        else:
            rot_tf = 'false'
    
    if rot == 1:
        message = rot_alpha(1)(message)
        encryptions_applied.append('r!u')
    if rot == 2:
        message = rot_alpha(2)(message)
        encryptions_applied.append('r@v')
    if rot == 3:
        message = rot_alpha(3)(message)
        encryptions_applied.append('r#w')
    if rot == 4:
        message = rot_alpha(4)(message)
        encryptions_applied.append('r$x')
    if rot == 5:
        message = rot_alpha(5)(message)
        encryptions_applied.append('r%y')
    if rot == 6:
        message = rot_alpha(6)(message)
        encryptions_applied.append('r^z')
    if rot == 7:
        message = rot_alpha(7)(message)
        encryptions_applied.append('r&a')
    if rot == 8:
        message = rot_alpha(8)(message)
        encryptions_applied.append('r*b')
    if rot == 9:
        message = rot_alpha(9)(message)
        encryptions_applied.append('r(c')
    if rot == 10:
        message = rot_alpha(10)(message)
        encryptions_applied.append('r)d')
    if rot == 11:
        message = rot_alpha(11)(message)
        encryptions_applied.append('r!!e')
    if rot == 12:
        message = rot_alpha(12)(message)
        encryptions_applied.append('r!@f')
    if rot == 13:
        message = rot_alpha(13)(message)
        encryptions_applied.append('r!#g')
    if rot == 14:
        message = rot_alpha(14)(message)
        encryptions_applied.append('r!$h')
    if rot == 15:
        message = rot_alpha(15)(message)
        encryptions_applied.append('r!%i')
    if rot == 16:
        message = rot_alpha(16)(message)
        encryptions_applied.append('r!^j')
    if rot == 17:
        message = rot_alpha(17)(message)
        encryptions_applied.append('r!&k')
    if rot == 18:
        message = rot_alpha(18)(message)
        encryptions_applied.append('r!*l')
    if rot == 19:
        message = rot_alpha(19)(message)
        encryptions_applied.append('r!(m')
    if rot == 20:
        message = rot_alpha(20)(message)
        encryptions_applied.append('r@)n')
    if rot == 21:
        message = rot_alpha(21)(message)
        encryptions_applied.append('r@!o')
    if rot == 22:
        message = rot_alpha(22)(message)
        encryptions_applied.append('r@@p')
    if rot == 23:
        message = rot_alpha(23)(message)
        encryptions_applied.append('r@#q')
    if rot == 24:
        message = rot_alpha(24)(message)
        encryptions_applied.append('r@$r')
    if rot == 25:
        message = rot_alpha(25)(message)
        encryptions_applied.append('r@%s')
    
    print('Enter what encryptions you would like to use')
    print('    -\"option\" to see options')
    print('    -\"enter\" when you have finished applying desired encryptions')
    enc = ''
    while enc != 'enter':
        enc = input()
        if enc == 'Option' or enc == 'option':
            print(' JAC1 through JAC6 \n NUM1 through NUM3')
            print('You may enter one JAC encryption, one NUM encryption, and one other encryption')
        if enc == 'JAC1':
            message = str.translate(message, JAC1)
            encryptions_applied.append('JANG')
        if enc == 'JAC2':
            message = str.translate(message, JAC2)
            encryptions_applied.append('RANG')
        if enc == 'JAC3':
            message = str.translate(message, JAC3)
            encryptions_applied.append('HANG')
        if enc == 'JAC4':
            message = str.translate(message, JAC4)
            encryptions_applied.append('SANG')
        if enc == 'JAC5':
            message = str.translate(message, JAC5)
            encryptions_applied.append('GANG')
        if enc == 'JAC6':
            message = str.translate(message, JAC6)
            encryptions_applied.append('BANG')
        if enc == 'NUM1':
            message = NUM1(message)
            encryptions_applied.append('orc')
        if enc == 'NUM2':
            message = NUM2(message)
            encryptions_applied.append('gob')
        if enc == 'NUM3':
            message = NUM3(message)
            encryptions_applied.append('dra')
    print('Encoded Message:')
    print(message)
    print(encryptions_applied)
        
if EorD == 'Decrypt' or EorD == 'decrypt':
    
    print('Enter your message to be decrypted:')
    message = input()
    print('')
    
    print('Enter the first item in the list')
    item1 = input()
    encryptions_applied.append(item1)
    
    print('Enter the second item in the list (or N/A if no 2nd item)')
    item2 = input()
    encryptions_applied.append(item2)
        
    print('Enter the third item in the list (or N/A if no 3rd item)')
    item3 = input()
    encryptions_applied.append(item3)
    
    if encryptions_applied[2] == 'dra':
        message = NUM3u(message)
    
    if encryptions_applied[2] == 'gob':
        message = NUM2u(message)
    
    if encryptions_applied[2] == 'orc':
        message = NUM1u(message)
    
    
    if encryptions_applied[1] == 'BANG':
        message = str.translate(message, JAC6u)
        
    if encryptions_applied[1] == 'GANG':
        message = str.translate(message, JAC5u)
        
    if encryptions_applied[1] == 'SANG':
        message = str.translate(message, JAC4u)
        
    if encryptions_applied[1] == 'HANG':
        message = str.translate(message, JAC3u)
        
    if encryptions_applied[1] == 'RANG':
        message = str.translate(message, JAC2u)
        
    if encryptions_applied[1] == 'JANG':
        message = str.translate(message, JAC1u)
    
    
    if encryptions_applied[0] == 'r!u':
        message = rot_alpha(25)(message)

    if encryptions_applied[0] == 'r@v':
        message = rot_alpha(24)(message)

    if encryptions_applied[0] == 'r#w':
        message = rot_alpha(23)(message)
                                   
    if encryptions_applied[0] == 'r$x':
        message = rot_alpha(22)(message)

    if encryptions_applied[0] == 'r%y':
        message = rot_alpha(21)(message)
        
    if encryptions_applied[0] == 'r^z':
        message = rot_alpha(20)(message)
        
    if encryptions_applied[0] == 'r&a':
        message = rot_alpha(19)(message)
        
    if encryptions_applied[0] == 'r*b':
        message = rot_alpha(18)(message)
        
    if encryptions_applied[0] == 'r(c':
        message = rot_alpha(17)(message)
        
    if encryptions_applied[0] == 'r)d':
        message = rot_alpha(16)(message)
        
    if encryptions_applied[0] == 'r!!e':
        message = rot_alpha(15)(message)
        
    if encryptions_applied[0] == 'r!@f':
        message = rot_alpha(14)(message)
        
    if encryptions_applied[0] == 'r!#g':
        message = rot_alpha(13)(message)
                                   
    if encryptions_applied[0] == 'r!$h':
        message = rot_alpha(12)(message)
        
    if encryptions_applied[0] == 'r!%i':
        message = rot_alpha(11)(message)
        
    if encryptions_applied[0] == 'r!^j':
        message = rot_alpha(10)(message)

    if encryptions_applied[0] == 'r!&k':
        message = rot_alpha(9)(message)
        
    if encryptions_applied[0] == 'r!*l':
        message = rot_alpha(8)(message)
        
    if encryptions_applied[0] == 'r!(m':
        message = rot_alpha(7)(message)
       
    if encryptions_applied[0] == 'r@)n':
        message = rot_alpha(6)(message)
        
    if encryptions_applied[0] == 'r@!o':
        message = rot_alpha(5)(message)
        
    if encryptions_applied[0] == 'r@@p':
        message = rot_alpha(4)(message)
      
    if encryptions_applied[0] == 'r@#q':
        message = rot_alpha(3)(message)
                                   
    if encryptions_applied[0] == 'r@$r':
        message = rot_alpha(2)(message)
        
    if encryptions_applied[0] == 'r@%s':
        message = rot_alpha(1)(message)
    
    print('Here is your decrypted message:')
    print(message)