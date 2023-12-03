from pytube import YouTube


def downloadVideo(link):
    try:
        video = YouTube(link)
    except Exception as e:
        print(e)
        print("Invalid link")
        exit(-1)
    print("downloading "+link + " as " + ("audio" if audio else "video"))
    if audio: video = video.streams.get_audio_only()
    else: video = video.streams.get_highest_resolution()

    try:
        name = video.default_filename  # default suffix is .mp4, even for audio only
        if audio:
            split = name.split('.')
            name = split[0] + ".mp3"
        video.download(filename=name)
    except Exception as e:
        print("Error occurred when trying to download")
        print(e)
        # exit(-1)

    print("Download ended")

def download2(link):
    try:
         print("downloading "+link)
         video = YouTube(link).streams.get_audio_only()

    except Exception as e:
        print(e)
        print("Invalid link:\t\t"+link)
        
    try:
        name = video.default_filename  # default suffix is .mp4, even for audio only
        if audio:
            split = name.split('.')
            name = split[0] + ".mp3"
        video.download(filename=name)
    except Exception as e:
        print("Error occurred when trying to download")
        print(e)


audio = True
fromfile = True

links=[]

if (fromfile):
    with open("linksfile.txt","r") as readfile:
        for line in readfile:
            links.append(line.rstrip('\n').split('&')[0])

else:
    links = ["",
            ""
         ]
for link in links:
    download2(link)
