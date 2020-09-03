import os #importing os
file_name = input("Input the Filename: ") #taking file name with extension from the user
name, extension = os.path.splitext(file_name) #spliting file and it's extension and saving in different variables
dic ={".py":"Python",".txt":"Text",".java":"java",".c":"C",".cpp":"C++"} #creating a dictionary for comparing extensions
print(dic.get(extension)) #printing the extension name
