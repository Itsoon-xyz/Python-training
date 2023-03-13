import pytube

vlink = "https://www.youtube.com/watch?v=h3-naWSga9I"
yt = pytube.YouTube(vlink)
yt.streams.get_highest_resolution().download()
print("download", vlink)
