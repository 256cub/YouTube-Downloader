
from pytube import Playlist
from pytube import YouTube
from pathlib import Path

# YouTube('https://www.youtube.com/watch?v=UNDX77GvDwQ').streams.first().download()
# YouTube('httPFUpF0').streams.first().download()
# YouTube('httjDA').streams.first().download()
# YouTube('htpPA').streams.first().download()

PATH = "/"

# p = Playlist("https://www.youtube.com/watch?v=eYSWkfRZMQQ&list=PLdXLsjL7A9k1yM3CT73ZIaKLXpywH-mGQ")
p = Playlist("https://www.youtube.com/watch?v=J5WBTUr0QBE&list=UUTuplgOBi6tJIlesIboymGA")
print(f'PlayList Title: {p.title}')

Path(PATH + p.title).mkdir(parents=True, exist_ok=True)
# Path(p.title).mkdir(parents=True, exist_ok=True)

total = (len(p))
i = 1

for video in p.videos:
    try:
        video.streams.first().download(output_path=PATH + p.title)
        print(' + [{} - {}] Downloading Video: {}'.format(i, total, video.title))
    except:
        print(' - [{} - {}] Can\'t Download Video'.format(i, total))

    i += 1
