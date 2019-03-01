def encrypt():
   raw = input('enter the text \n')
   v = int(input('shift by:'))
   print('\n')
   out = ''
   for i in raw:
       out += chr(ord(i)+v)
   print('encrypted text==>',out)

def decrypt():
   raw = input('enter the text \n')
   v = int(input('shift by:'))
   print('\n')
   out = ''
   for i in raw:
       out += chr(ord(i)-v)
   print('decrypted text==>',out)

print('========Caesar Cipher========\n\n')
a = input('MENU\n1)Encrypt text\n2)Decrypt text\nEnter your choice\n')
if a=='1':
   encrypt()

elif a=='2':
   decrypt()

else:
   print('invalid choice!')

'''
Created by: Vasanth R
Time      : 21:37
Data      : 20/11/2018
'''
