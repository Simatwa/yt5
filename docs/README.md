<p align="center">
<a href="https://github.com/Simatwa/yt5"><img src="https://img.shields.io/static/v1?logo=github&color=blueviolet&label=Test&message=Pass"/></a>
<a href="LICENSE"><img src="https://img.shields.io/static/v1?logo=MIT&color=Blue&message=MIT&label=License"/></a>
<a href="#" alt="coverage"><img src="https://img.shields.io/static/v1?logo=Coverage&label=Coverage&message=80%&color=yellowgreen"/></a>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/static/v1?label=Code style&message=black&color=Black"/></a>
<a href="#"><img alt="progress" src="https://img.shields.io/static/v1?logo=Progress&label=Progress&message=60%&color=green"/></a>
<a href="https://wakatime.com/badge/user/321c8a21-57bc-4782-bb00-8733ff579c0d/project/9681babc-aedd-4a02-ae7c-f91f914ad9b3"><img src="https://wakatime.com/badge/user/321c8a21-57bc-4782-bb00-8733ff579c0d/project/9681babc-aedd-4a02-ae7c-f91f914ad9b3.svg" alt="wakatime"/></a>
</p>

```
                                                                   
                                                                   
                                  tttt          555555555555555555 
                               ttt:::t          5::::::::::::::::5 
                               t:::::t          5::::::::::::::::5 
                               t:::::t          5:::::555555555555 
yyyyyyy           yyyyyyyttttttt:::::ttttttt    5:::::5            
 y:::::y         y:::::y t:::::::::::::::::t    5:::::5            
  y:::::y       y:::::y  t:::::::::::::::::t    5:::::5555555555   
   y:::::y     y:::::y   tttttt:::::::tttttt    5:::::::::::::::5  
    y:::::y   y:::::y          t:::::t          555555555555:::::5 
     y:::::y y:::::y           t:::::t                      5:::::5
      y:::::y:::::y            t:::::t                      5:::::5
       y:::::::::y             t:::::t    tttttt5555555     5:::::5
        y:::::::y              t::::::tttt:::::t5::::::55555::::::5
         y:::::y               tt::::::::::::::t 55:::::::::::::55 
        y:::::y                  tt:::::::::::tt   55:::::::::55   
       y:::::y                     ttttttttttt       555555555     
      y:::::y                                                      
     y:::::y                                                       
    y:::::y                                                        
   y:::::y                                                         
  yyyyyyy                                                          
                                                                   
                                                                   
```
- **yt5** is a [Python](https://python.org) script that downloads [YouTube](https://www.youtube.com) ***Videos*** & ***audios*** at `console` environment.

## Installation ##
- From Github - *source*

```
git clone https://github.com/Simatwa/yt5.git
cd yt5
python setup.py install

```

- From Pypi

```
pip install yt5
```

## Usage ##

#### Video #### 

- Videos can be downloaded by parsing a `URI` <sup>prefixed</sup> or <sub>postfixed</sub> by its category:
- For instances:
1. Single video :

```
$ yt5 url <Video-URI>

```		
![yt52](https://github.com/Simatwa/yt5/raw/main/assets/yt52.jpg)
     
- Alternatively, this can be done by omitting `url` command since it's the default category.

```
$ yt5 <Video-URI>

```
![yt51](https://github.com/Simatwa/yt5/raw/main/assets/yt51.jpg)


2. All videos in a Playlist :

```
$ yt5 playlist <Playlist-URI>

```
![yt53](https://github.com/Simatwa/yt5/raw/main/assets/yt53.jpg)
	 
3. All videos in a Channel : 

```
$ yt5 channel <Channel-URI>

```
![yt54](https://github.com/Simatwa/yt5/raw/main/assets/yt54.jpg)
		
4. Collection of single-video's URI contained in a text file : 

```
$ yt5 fnm <file-path>

```
![yt55](https://github.com/Simatwa/yt5/raw/main/assets/yt55.jpg)
			
####  Audio #### 

- Audio of a video can be downloaded by adding `--mp3` to the commands parsed.
  - For instance:
1. Single audio : 
  		
```
$ yt5 url <Video-URI>  --mp3

```

![yt56](https://github.com/Simatwa/yt5/raw/main/assets/yt56.jpg)
       
- Similarly, this can be done to **other** ***categories***.

- For further information you can run:
	
```
$ yt5 -h

```  

* Output :

```
usage: yt5 [-h] [-v] [-res [720p|480p|360p|240p|144p]] [-max MAXIMUM] [-dir DIRECTORY] [--mp3]
           [--show] [--static] [--usage]
           [[fnm|url|playlist|channel]] url

positional arguments:
  [fnm|url|playlist|channel]
                        Category of the videos referred by the link or filename[fnm] containing
                        links
  url                   Link of the video

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -res [720p|480p|360p|240p|144p], --resolution [720p|480p|360p|240p|144p]
                        Resolution [quality] of videos to be downloaded in
  -max MAXIMUM, --maximum MAXIMUM
                        Maximum videos to be downloaded
  -dir DIRECTORY, --directory DIRECTORY
                        Directory for saving downloaded file
  --mp3                 Specify to download audio only
  --show                Show the downloaded file-path
  --static              Restricts stdout of file-path in prose-format
  --usage               Show this help info in more stylistic way

```


## Independencies ##

1. [pytube](https://github.com/pytube/pytube)
2. [colorama](https://github.com/pytube/pytube)
3. [tabulate](https://github.com/astanin/python-tabulate)
 
 * [Review](requirements.txt).


## Acknowledgements ##

- [x] [Pytube](https://github.com/pytube/pytube)
- [x] [Python Team](https://python.org)
