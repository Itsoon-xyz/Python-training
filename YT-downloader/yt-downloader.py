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


def downloadProgress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(percent)


yt = pytube.YouTube(link)

yt.register_on_progress_callback(downloadProgress)

print(f"Download of \"{yt.title}\" in progress please wait...")
# print(yt.streams)
stream = yt.streams.get_highest_resolution()
stream.download()
print("The download is done")
