import pickle
import random

from pygoogle_image import image as pi

print("Download High Resolution images")

file = open("autoareply.pkl", 'rb')


def reply():
    auto_reply = pickle.load(file)
    print(random.choice(auto_reply))
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

while True:
    try:
        name = input("Enter the name of the person you want to search in the space below \n--> ")
        limit = int(input("Enter the number of images you want to download \n --> "))
        pi.download(name, limit=limit)
    except KeyboardInterrupt:
        pass
