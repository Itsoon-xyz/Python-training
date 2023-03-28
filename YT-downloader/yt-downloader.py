import pytube


link = input("Enter url: ")
yt = pytube.YouTube(link)
print(f"Download of {yt.title} in progress please wait...")
# print(yt.streams)
yt.streams.get_highest_resolution().download()
