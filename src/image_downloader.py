import random, pickle
from pygoogle_image import image as pi

print("Download High Resolution images")

file = open("autoareply.txt", 'x')

def reply():
    autoReply = [
    "Our system has flagged a sentence containing inappropriate language.",
    "Unwanted words were identified in the text, including sensitive and explicit content.",
    "The algorithm has detected a sentence with potentially offensive or personal information.",
    "We have identified a string of text that includes inappropriate language, both sexual and personal in nature.",
    "Alert: The system has identified a sentence containing explicit or private content.",
    "The automated filters have detected offensive words in the given sentence, including sexual and personal references.",
    "Warning: The system has marked a sentence as containing objectionable words, including sexual or private information.",
    "Our system's content analysis has found a sentence that includes inappropriate language, specifically sexual and personal references.",
    "The algorithm has raised a red flag on a sentence due to the presence of offensive words, including sexually explicit or personally sensitive content.",
    "Notification: Unwanted words, such as sexual and personal references, have been detected in the sentence by our monitoring system.",
    "The system has detected inappropriate language in the sentence provided.",
    "We have identified offensive words in the text, including explicit or personal content.",
    "Alert: Objectionable words were found in the given sentence, which may include sexual or private references.",
    "Warning: Offensive language has been detected in the provided text, including sexually explicit or sensitive information.",
    "The automated filters have marked the sentence as containing inappropriate words, both sexual and personal in nature.",
    "Our system's content analysis indicates the presence of offensive language, including references of a sexual or personal nature.",
    "The algorithm has identified potentially offensive content in the sentence, involving sexually explicit or private references.",
    "We have detected objectionable words in the provided text, which may include sexually explicit or personal content.",
    "Caution: The system has flagged the sentence for containing inappropriate language, potentially involving sexual or personal information.",
    "Notification: Offensive words, including sexual and personal references, have been identified in the sentence by our monitoring system.",
    "The system has detected explicit language in the given text.",
    "Unwanted words, such as sensitive or explicit content, have been detected and flagged in the sentence.",
    "Alert: The algorithm has identified a sentence containing offensive or personal information.",
    "Warning: Inappropriate language, both sexual and personal in nature, has been detected in the provided text.",
    "The automated filters have marked the sentence as objectionable, including offensive words related to sexuality or personal matters.",
    "Our system's content analysis indicates the presence of offensive language, specifically sexual and personal references, in the sentence.",
    "The algorithm has raised concerns about the sentence due to the presence of offensive words, including sexually explicit or personally sensitive content.",
    "We have detected objectionable words in the sentence, which may include references to sexual or personal topics.",
    "Caution: The system has flagged the sentence for containing inappropriate language, potentially involving sexual or private references.",
    "Notification: Offensive words, such as sexual and personal references, have been identified in the sentence by our monitoring system.",
    "The system has identified explicit language in the given text.",
    "Unwanted words, including sensitive or explicit content, have been detected and marked in the provided sentence.",
    "Alert: The algorithm has identified a sentence containing offensive or private information.",
    "Warning: Inappropriate language, both sexual and personal in nature, has been detected in the given text.",
    "The automated filters have marked the sentence as objectionable, including offensive words related to sexuality or personal matters.",
    "Our system's content analysis indicates the presence of offensive language, specifically sexual and personal"
    ]
    pickle.dump(autoReply, file)
    file.close()
    print(random.choice(autoReply))

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

        for word in unaccepted:
            if(word in name):
                reply()
            else:
                limit = int(input("Enter the number of images you want to download \n --> "))
                if(limit <= 20):
                    pi.download(name, limit=limit)
                else:
                    print("Too many images to download in free account")

        # if(unaccepted[0] in name):
        #     reply()
        # elif(unaccepted[1] in name):
        #     reply()
        # elif(unaccepted[2] in name):
        #     reply()
        # elif(unaccepted[3] in name):
        #     reply()
        # elif(unaccepted[4] in name):
        #     reply()
        # elif(unaccepted[5] in name):
        #     reply()
        # elif(unaccepted[6] in name):
        #     reply()
        # elif(unaccepted[7] in name):
        #     reply()
        # elif(unaccepted[8] in name):
        #     reply()
        # elif(unaccepted[9] in name):
        #     reply()
        # elif(unaccepted[10] in name):
        #     reply()
        # elif(unaccepted[11] in name):
        #     reply()
        # elif(unaccepted[12] in name):
        #     reply()
        # elif(unaccepted[13] in name):
        #     reply()
        # else:
        #     limit = int(input("Enter the number of images you want to download \n --> "))
        #     if(limit <= 20):
        #         pi.download(name, limit=limit)
        #     else:
        #         print("Too many images to download in free account")
    else:
        print("Wrong choice kindly, restart the program and select 1 or 2 to proceed.")

backPart()
