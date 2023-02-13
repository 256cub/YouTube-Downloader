#  YouTube Downloader

## Installation

To install from pypi with pip:

```bash
$ python -m pip install pytube
```

Sometime, the pypi release becomes slightly outdated. To install from the source with pip:

```bash
$ python -m pip install git+https://github.com/pytube/pytube
```

## Description
YouTube is the most popular video-sharing platform in the world and as a hacker you may encounter a situation where you want to script something to download videos.  For this I present to you *pytube*.

*pytube* is a lightweight library written in Python. It has no third party dependencies and aims to be highly reliable.

*pytube* also makes pipelining easy, allowing you to specify callback functions for different download events, such as  ``on progress`` or ``on complete``.

Finally *pytube* also includes a command-line utility, allowing you to quickly download videos right from terminal.

### Behold, a perfect balance of simplicity versus flexibility:

```python
 >>> YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
 >>> yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
 >>> yt.streams
  ... .filter(progressive=True, file_extension='mp4')
  ... .order_by('resolution')
  ... .desc()
  ... .first()
  ... .download()
```

## Features
- Support for Both Progressive & DASH Streams
- Support for downloading complete playlist
- Easily Register ``on_download_progress`` & ``on_download_complete`` callbacks
- Command-line Interfaced Included
- Caption Track Support
- Outputs Caption Tracks to .srt format (SubRip Subtitle)
- Ability to Capture Thumbnail URL.
- Extensively Documented Source Code
- No Third-Party Dependencies

## Getting started

Let's begin with showing how easy it is to download a video with pytube:

```python
>>> from pytube import YouTube
>>> YouTube('https://youtube.com/watch?v=2lAe1cqCOXo').streams.first().download()
```
This example will download the highest quality progressive download stream available.

Next, let's explore how we would view what video streams are available:

```python
>>> yt = YouTube('https://youtube.com/watch?v=2lAe1cqCOXo')
>>> yt.streams
 [<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">,
 <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
 <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">,
 <Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="399" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.08M.08" progressive="False" type="video">,
 <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">,
 <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="398" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.05M.08" progressive="False" type="video">,
 <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">,
 <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="397" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.04M.08" progressive="False" type="video">,
 <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">,
 <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="396" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.01M.08" progressive="False" type="video">,
 <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">,
 <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="395" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.00M.08" progressive="False" type="video">,
 <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">,
 <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="394" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.00M.08" progressive="False" type="video">,
 <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">,
 <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">,
 <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">,
 <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]
```
You may notice that some streams listed have both a video codec and audio codec, while others have just video or just audio, this is a result of YouTube supporting a streaming technique called Dynamic Adaptive Streaming over HTTP (DASH).

In the context of pytube, the implications are for the highest quality streams; you now need to download both the audio and video tracks and then post-process them with software like FFmpeg to merge them.

The legacy streams that contain the audio and video in a single file (referred to as "progressive download") are still available, but only for resolutions 720p and below.

To only view these progressive download streams:

```python
 >>> yt.streams.filter(progressive=True)
  [<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">,
  <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">]
```

Conversely, if you only want to see the DASH streams (also referred to as "adaptive") you can do:

```python
>>> yt.streams.filter(adaptive=True)
 [<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">,
 <Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="399" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.08M.08" progressive="False" type="video">,
 <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">,
 <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="398" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.05M.08" progressive="False" type="video">,
 <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">,
 <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="397" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.04M.08" progressive="False" type="video">,
 <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">,
 <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="396" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.01M.08" progressive="False" type="video">,
 <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">,
 <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="395" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.00M.08" progressive="False" type="video">,
 <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">,
 <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="394" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.00M.08" progressive="False" type="video">,
 <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">,
 <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">,
 <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">,
 <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]
```

You can also interact with Youtube playlists:

```python
>>> from pytube import Playlist
>>> pl = Playlist("https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU")
>>> for video in pl.videos:
>>>     video.streams.first().download()
```

Pytube allows you to filter on every property available (see the documentation for the complete list), let's take a look at some of the most useful ones.

To list the audio only streams:

```python
>>> yt.streams.filter(only_audio=True)
  [<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">,
  <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">,
  <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">,
  <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]
```

To list only ``mp4`` streams:

```python
>>> yt.streams.filter(subtype='mp4').all()
 [<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">,
 <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
 <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">,
 <Stream: itag="399" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.08M.08" progressive="False" type="video">,
 <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">,
 <Stream: itag="398" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.05M.08" progressive="False" type="video">,
 <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">,
 <Stream: itag="397" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.04M.08" progressive="False" type="video">,
 <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">,
 <Stream: itag="396" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.01M.08" progressive="False" type="video">,
 <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">,
 <Stream: itag="395" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.00M.08" progressive="False" type="video">,
 <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">,
 <Stream: itag="394" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.00M.08" progressive="False" type="video">,
 <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">]
```

Multiple filters can also be specified:

```python
>>> yt.streams.filter(subtype='mp4', progressive=True).all()
>>> # this can also be expressed as:
>>> yt.streams.filter(subtype='mp4').filter(progressive=True).all()
  [<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">,
  <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">]
```
You also have an interface to select streams by their itag, without needing to filter:

```python
>>> yt.streams.get_by_itag(22)
  <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">
```

If you need to optimize for a specific feature, such as the "highest resolution" or "lowest average bitrate":

```python
>>> yt.streams.filter(progressive=True).order_by('resolution').desc().all()
  [<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
  <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">]
```
Note that ``order_by`` cannot be used if your attribute is undefined in any of the Stream instances, so be sure to apply a filter to remove those before calling it.

If your application requires post-processing logic, pytube allows you to specify an "on download complete" callback function:

```python
 >>> def convert_to_aac(stream, file_handle):
         return  # do work

 >>> yt.register_on_complete_callback(convert_to_aac)
```

Similarly, if your application requires on-download progress logic, pytube exposes a callback for this as well:

```python
 >>> def show_progress_bar(stream, chunk, bytes_remaining):
         return  # do work

 >>> yt.register_on_progress_callback(show_progress_bar)
```

You can also download videos to a specific directory with specific filename:

```python
>>> yt = YouTube('https://youtube.com/watch?v=2lAe1cqCOXo')
>>> yt.streams.first().download(output_path="/tmp" ,filename='output')
```

## Command-line interface (CLI)

Pytube also ships with a tiny CLI for interacting with videos and playlists.

To download the highest resolution progressive stream:

```bash
$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo
```

To view available streams:

```bash
$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo --list
```

To download a specific stream, use the itag

```bash
$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo --itag=22
```

To get a list of all subtitles (caption codes) 

```bash
$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo --list-captions
```

To download a specific subtitle (caption code) - in this case the
english subtitles (in srt format) - use:

```bash
$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo -c en
```

It is also possible to just download the audio stream (default AAC/mp4):

```bash
$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo -a
```


---

## Support

The team is always here to help you. 
Happen to face an issue? Want to report a bug? 
You can submit one here on GitHub using the [Issue Tracker](https://github.com/256cub/YouTube-Downloader/issues/new). 


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create.
Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
You can also simply open an issue with the tag "feature". 
Don't forget to give the project a star! 

**Thanks again !!!**


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourNewFeature`)
3. Commit your Changes (`git commit -m 'Add some YourNewFeature'`)
4. Push to the Branch (`git push origin feature/YourNewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



## Security

If you discover any security-related issues, please email 256cub@gmail.com instead of using the issue tracker.


## Buy Me a Coffee

This project will be always an open source, even if I don't get donations. 
That being said, I know there are amazing people who may still want to donate just to show their appreciation.


<a href="https://www.buymeacoffee.com/256cub" target="_blank">
<img src="https://cdn.buymeacoffee.com/buttons/arial-orange.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>


**Thank you very much in advance !!!**


We accept donations through Ko-fi, PayPal, BTC or ETH. 
You can use the buttons below to donate through your method of choice.

|   Donate With   |                      Address                       |
|:---------------:|:--------------------------------------------------:|
|      Ko-fi      |       [Click Here](https://ko-fi.com/256cub)       |
|     PayPal      | [Click Here](https://paypal.me/256cub) |
|   BTC Address   |         3MsUYeUfmpwVS2QrnRbLpCjGaVn2WDD6sj         |
|   ETH Address   |     0x10cd16ba338661d2FB683B2481f8F5000FEd5663     |


## Credits

- [256cub](https://github.com/256cub)

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
