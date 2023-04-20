#functions.py

#Name: Rongbo He, Joshua Nickol, Eva Rios
#email: hero@mail.uc.edu, nickolje@mail.uc.edu, rioseb@mail.uc.edu
#Assignment Title: Assignment final project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that I can use Eclipse to create a function that 
#extract data from a list using encrypted data as an index to that list and another function
#that loads and displays the image we took at the location.
#Citations:
#Anything else that's relevant:



import json
from PIL import Image, ImageOps
def extract_location():
    #Open the JSON file
    with open('EncryptedGroupHints Spring 2023 section 001.json') as f:
        data = json.load(f)
    #Open and read the text file
    with open('english.txt') as txt:
        lines = txt.readlines()
        lns = [line.strip() for line in lines]
    #print(lns)
    #Find the text index for our group
    txtIndex = data['Nikolai Andrianov']
    #print(txtNum)
    #Create index for each value in the text file
    index = []
    num = 0 
    for line in lns:
        num +=1
        index.append(str(num))
    #print(index)
    #Create a dictionary combing JSON file and text file
    dictionary = dict(zip(index, lns))
    #print(dictionary)
    #Print the location 
    for index in txtIndex:
        print(dictionary[index])
        
        
def load_image():
    image_Ops = Image.open('picture.jpeg')
    image = ImageOps.flip(image_Ops)
    image.show()
   
    

    
