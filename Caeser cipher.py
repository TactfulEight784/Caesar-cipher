# ceaser cipher encryptr and decryptr with any key
alpha = "abcdefghijklmnopqrstuvwxyz" # makes a alphabet variable
yesOrNo = input("Would you like to encrypt Y/N: ")
if(yesOrNo == "Y"): 
  def encrypt(cleartext, key): # defining the below statment that uses cleartext
    cyphertext = "" #blank for cypher text to start
    for char in cleartext: #for char which is an index in cleartext do this. char starts at 0 which is the first letter then to 1 the second letter so on 
      if char in alpha:
        newpos = (alpha.find(char) + key) % 26 #finds the new charactor in number form stores it in newpos
        cyphertext += alpha[newpos] # indexs number for newpos into a letter from alpha
      else:
        cyphertext += char # adds a non alpha char to the cypher
    return cyphertext # exits the def loop makes encrypt function the actual output
  
  cleartext = input("thing you want encrypted: ") #inputting clear text
  cleartext = cleartext.lower() # makes clear text all lowercase
  key = int(input("enter your key 1 to 25: "))
  while key <= 0 or key >=26:
    print("error key must be 1 to 25 please try again ")
    key = int(input("enter your key 1 to 25 "))
  print("Your code is:", encrypt(cleartext, key))# this makes it where encrypt accepts the variables while also printing it when its done calls the function then prints
  print("your key is", key)
yesOrNo = input("Would you like to decrypt Y/N: ") #basically the same as above so the comments go with it
if(yesOrNo == "Y"):
  def decrypt(cyphertext, key): # make another program for decrypt 
    cleartext = ""
    for char in cyphertext:
      if char in alpha:
        newpos = (alpha.find(char) - key) % 26
        cleartext += alpha[newpos]
      else:
        cleartext += char
    return cleartext
  cyphertext = input("Please enter what you want decoded: ")
  cyphertext = cyphertext.lower()
  key = int(input("What key is needed to decode: "))
  while key <= 0 or key >=26:
    print("error key must be 1 to 25 please try again ")
    key = int(input("enter your key 1 to 25 "))
  print("Your text is:", decrypt(cyphertext, key)) # the first part outputs the cleartext while the second part puts the inputs into the def
  print("Your key used was", key)