# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:15:20 2019

@author: nav27
"""
#Defining all the symbols that can be encrypted using this code
LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

print("Enter the value of the key: ")

#Taking the value of the shift key from the user
key = int(input())

# Converting the key to the value less than 66 
key = key%66

transformOutput = ''

print("Enter mode of operation: 'Encrypt' or 'Decrypt' ")
Mode = input()
'''
#Checking if the user entered the right input
while Mode != 'Encrypt' or 'Decrypt':
    print("Enter mode of operation: 'Encrypt' or 'Decrypt' ")
    Mode = input() '''
    
print("Enter the string you want to encrypt or decrypt: ")
userInput = input()

for i in range(len(userInput)):
    if(userInput[i] in LETTER):
        
        #Find the index of the letter in all the letters that we defined to
        #match them 
        userIndex = LETTER.find(userInput[i])
        
        if Mode == 'Encrypt':
            transformIndex = userIndex + key
        else:
            transformIndex = userIndex - key
        
        transformIndex = transformIndex%66
    
        transformOutput = transformOutput + LETTER[transformIndex]
    else:
        
        transformOutput = transformOutput + userInput[i]
print(transformOutput)