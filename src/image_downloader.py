from pygoogle_image import image as pi

print("Bundle Image downloader\n")
name = input("Enter the name of the person you want to search in the space below \n--> ")
limit = int(input("Enter the number ofi mages you want to download \n --> "))

pi.download(name, limit=limit)