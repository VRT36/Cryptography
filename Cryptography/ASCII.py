def encrypt():
    raw = raw_input('enter the text\n')
    out = []
    for i in raw:
        out.append(ord(i)) 
    print 'encrypted text==>',out

def decrypt():
    raw = raw_input('enter the text( no comma )\n')
    out = []
    for i in raw :
        out.append(chr(i))
    print 'decrypted text==>',out

print('========ASCII========\n\n')
a = input('MENU\n1)Encrypt text\n2)Decrypt text\nEnter your choice\n')
if a==1:
   encrypt()

elif a==2:
   decrypt()

else:
   print 'invalid choice!'

'''
Created by: Vasanth R
Time      : 18:55
Data      : 21/11/2018
'''

    
