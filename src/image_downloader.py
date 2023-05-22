import random, pickle
from pygoogle_image import image as pi

print("Download High Resolution images")

file = open("autoareply.pkl", 'rb')

def reply():
    autoReply = pickle.load(file)
    print(random.choice(autoReply))
    file.close()

prompt = [
    "images of Mountains", 
    "images of cities", 
    "images of African People", 
    "images of oceans", 
    "images of American People", 
    "images of Russian People", 
    "images of Kenyan People", 
    "images of Nigerian People", 
    "images of asian People",
    "Select from above to search or type it here", 
    "Do you want to search unlisted images from above?"]
nextNo = 1
for eachPrompt in prompt:
    print(f'{nextNo}. {eachPrompt}')
    nextNo += 1

def backPart():
    choice = int(input("Type 1 for the first choice and type 2 for the second choice\n"))
    if(choice==1):
        search = int(input("1. Select from above to search or type it here\n"))
        if(search == 1):
            lim1 = int(input("Enter the number of Mountains images you want to download \n -->"))
            if(lim1 <=20):
                pi.download("images of Mountains", limit=lim1)
            else:
                print("Too many images to download in free account")
        elif(search == 2):
            lim2 = int(input("Enter the number of images of cities you want to download \n -->"))
            if(lim2 <=20):
                pi.download("images of cities", limit=lim2)
            else:
                print("Too many images to download in free account")
        elif(search == 3):
            lim3 = int(input("Enter the number of images you want to download \n -->"))
            if(lim3 <= 20):
                pi.download("images of African People", limit=lim3)
            else:
                print("Too many images to download in free account")
        elif(search == 4):
            lim4 = int(input("Enter the number of images you want to download \n -->"))
            if(lim4 <= 20):
                pi.download("images of oceans", limit=lim4)
            else:
                print("Too many images to download in free account")
        elif(search == 5):
            lim5 = int(input("Enter the number of images you want to download \n -->"))
            if(lim5 <= 20):
                pi.download("images of American People", limit=lim5)
            else:
                print("Too many images to download in free account")
        elif(search == 6):
            lim6 = int(input("Enter the number of images you want to download \n -->"))
            if(lim6 <= 20):
                pi.download("images of Russian People", limit=lim6)
            else:
                print("Too many images to download in free account")
        elif(search == 7):
            lim7 = int(input("Enter the number of images you want to download \n -->"))
            if(lim7<= 20):
                pi.download("images of Kenyan People", limit=lim7)
            else:
                print("Too many images to download in free account")
        elif(search == 8):
            lim8 = int(input("Enter the number of images you want to download \n -->"))
            if(lim8 <=20):
                pi.download("images of Nigerian People", limit=lim8)
            else:
                print("Too many images to download in free account")
    elif(choice ==2):

        name = input("Enter the name of the person you want to search in the space below \n--> ")

        unaccepted = ['porn','sex','fuck','nude','dick','puss','vagin','rape','rapist','ngwati','kibwenye','kinembe','xxx','nyandus']
        if name in unaccepted:
            reply()
        else:
            limit = int(input("Enter the number of images you want to download \n --> "))
            if(limit <= 20):
                pi.download(name, limit=limit)
            else:
                print("Too many images to download in free account")
    else:
        print("Wrong choice kindly, restart the program and select 1 or 2 to proceed.")

backPart()
