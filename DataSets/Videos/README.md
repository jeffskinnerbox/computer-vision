# Video Sources
To acquire the videos below,
you can use [`youtube-dl`][01],
which is a command-line program to download videos from [YouTube.com][05]
and a few more sites.
For youtube-dl, you'll find documentation [here][02],
and you can install it via `sudo apt-get install youtube-dl`
and use the `-k` option to get a MP4 formatted video.

The Videos needed to support these Juypter Notebooks are:

* [All-is-Full-of-Love-by-Bjork.mp4](https://www.youtube.com/watch?v=AjI2J2SQ528&list=RDAjI2J2SQ528)
* [Budapest-Hungary-people-walking-and-cars-driving.mp4](https://www.youtube.com/watch?v=N79f1znMWQ8)
* [Cisco-Meraki-AP.mp4](https://www.youtube.com/watch?v=5BWcxO66UQM)
* [Jurassic-Park-Trailer-1993.mp4](https://www.youtube.com/watch?v=p1FevaLUbTg)
* [People-Walking-Shot-From-Above.mp4](https://www.shutterstock.com/video/clip-4503176-stock-footage-diverse-group-of-young-people-walking-past-camera-shot-from-above-in-a-white-studio.html)
* [People-Walking-Shot-From-Above-2.mp4](https://www.dropbox.com/s/7mbo35zrxd1aefz/peopleCounter.avi?dl=0)
* [Charlie-Chaplin-The-Great-Dictator.mp4](https://www.youtube.com/watch?v=dLyd7v0RwNI)
* [Vincent-Van-Gogh-in-Google-Deep-Dream.mp4](https://www.youtube.com/watch?v=I2y6kS7396s)
* [Big-Buck-Bunny.mp4](https://www.youtube.com/watch?v=tQ4Swv7WXQg)
* [Car-Traffic.mp4](https://www.youtube.com/watch?v=K4NiaXmXIhE)
* [Bruno-Mars-Uptown-Funk.mp4](https://www.youtube.com/watch?v=OPf0YbXqDm0)

Want live sources? Checkout these sites:

* [30-Minutes-of-Driving](https://drive.google.com/file/d/0B_6iW8KaJFXObHp1WGtHVGlsNzQ/view)
* [Unreal Streaming Technologies -  IP camera streaming](http://umediaserver.net/umediaserver/demos.html)
* [Live Tarin Videos](https://www.railserve.com/RailCams/)
* [Insecam](http://www.insecam.org/en/)


# Video Conversion
If you have a video format that needs converting,
there are many, many tools but [CloudConver][03] may be the easiest to use.
CloudConvert supports the conversion between more than 200 different
audio, video, document, ebook, archive, image, spreadsheet and presentation formats.

If you prefer the command-line
you can [convert many file formats with `ffmpeg`][06]:

```bash
# covert avi to mp4 file
ffmpeg -i input.avi -acodec libfaac -b:a 128k -vcodec mpeg4 -b:v 1200k -flags +aic+mv4 output.mp4

# covert mkv to mp4 file
ffmpeg -i input.mkv -codec copy -strict -2 output.mp4
```

Inversely, to create AVI from MP4 with `ffmpeg`,

```bash
# convert mp4 to avi
`ffmpeg -i input.mp4 -codec copy output.avi`
```


[01]:https://github.com/rg3/youtube-dl
[02]:https://www.tecmint.com/install-youtube-dl-command-line-video-download-tool/
[03]:https://cloudconvert.com/
[04]:https://andre.blue/blog/converting-avi-to-mp4-with-ffmpeg/
[05]:https://www.youtube.com/
[06]:https://opensource.com/article/17/6/ffmpeg-convert-media-file-formats
