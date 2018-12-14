def encrypt():
    raw = raw_input('enter the text\n')
    raw = raw.encode('hex')
    print 'encrypted Hex value==>',raw
 
print('========Hexadecimal========\n\n')
a = input('MENU\n1)Encrypt text\n2)Decrypt text\nEnter your choice\n')    
encrypt()

'''
Created by: Vasanth R
Time      : 21:37
Data      : 20/11/2018
'''
