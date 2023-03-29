import pytube
import validators

validInput = False
while not validInput:
    link = input("Enter url: ")
    validation = validators.url(link)
    if validation:
        validInput = True
    else:
        print("Invalid input. Please enter only youtube URL.")
# yt = pytube.YouTube(link)
print(f"Download of {yt.title} in progress please wait...")
# print(yt.streams)
# yt.streams.get_highest_resolution().download()
