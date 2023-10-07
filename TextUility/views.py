from itertools import tee
from django.http import HttpResponse
from django.shortcuts import render

panchud = ''
# def index(request):
#     return HttpResponse(" <h1 style='text-align:center;'> Home </h1> </br>  <h1>  <a style='margin:5px;background:#7cd76b;' href='/remove'> Remove Punc </a> <a style='margin:5px;background:#7cd76b;' href='/cap'> Capitalize First </a><a style='margin:5px;background:#7cd76b;' href='/newline'> new line remove first </a><a style='margin:5px;background:#7cd76b;' href='/space'> Space Remover </a><a style='margin:5px;background:#7cd76b;' href='/char'> chartCount </a></h1> ")

# def removefunc(request):
#     return HttpResponse("<h1 style='text-align:center;'> Remove Function </h1> <a  href='/'> <-Back </a>")
# def capfirst(request):
#     return HttpResponse("<h1 style='text-align:center;'> Capitalize First </h1> <a  href='/'> <-Back </a>")

# def newlineremove(request):
#     return HttpResponse("<h1 style='text-align:center;'> new line remove first </h1> <a  href='/'> <-Back </a>")

# def spaceremove(request):
#     return HttpResponse("<h1 style='text-align:center;'> Space Remover </h1> <a  href='/'> <-Back </a>")

# def charcount(request):
#     return HttpResponse("<h1 style='text-align:center;'> chartCount </h1> <a  href='/'> <-Back </a>")


def index(request):
    caption = {
        'vill': 'kandoli',
        'disc': 'dausa'
    }
    return render(request, 'index.html', caption)


def copytext(re):
    global panchud, djtext
    import pyperclip as pc
    print('copy  : ', djtext)
    pc.copy(djtext)

    return HttpResponse("Copied <br> <a href='/' >Home</a>")


def Analyze(re):
    global panchud, djtext
    djtext = re.GET.get('text', 'defalut')
    djcheck = re.GET.get('check', 'off')

    panchu = '''!"#$%&'()*+,-./:;<=>?@[^]\_`{|}~'''

    panchud = ' '
    # Panchuation remover Function

    # if not chcked not for any Text Utility Operation
    if re.GET.get('check', 'off') == 'of':
        panchud = 'Sorry !! You are not chacked for `Any Text Utility` !!'
        color = 'red'
    color = 'blue'
    if djcheck == 'on':
        for char in djtext:
            if char not in panchu:
                panchud += char
        djtext = panchud
    # Convert to UPPERCASE Function
    if re.GET.get('uppercase', 'off') == 'on':
        panchud = ''
        for char in djtext:
            panchud += char.upper()
        djtext = panchud

    # new line remover Function
    if re.GET.get('newline', 'off') == 'on':
        panchud = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                panchud = panchud + char

        djtext = panchud
        # print(panchud)

    # Extra Space Remover funtion
    if re.GET.get('spacere', 'off') == 'on':
        panchud = ''
        for i, char in enumerate(djtext):
            if not (djtext[i] == ' ' and djtext[i+1] == ' '):
                panchud = panchud+char

        djtext = panchud

    # Charctor Counter  funtion
    if re.GET.get('charcount', 'off') == 'on':
        panchud = len(djtext)

    variables = {
        'purpose': 'Remove Panchuations',
        'text': panchud,
        'color': color

    }
    return render(re, 'panch.html', variables)

from pytube import Playlist,YouTube
import json
# @csrf_exempt

def ExtractPlaylistVideos(request):
    dataUrls = {}
    PlaylistVideos = []
    
    if request.method=="POST":

        playlistId = request.POST.get('videoid')
        print("Video id  ",playlistId) #https://www.youtube.com/playlist?list=PL9bw4S5ePsEEqCMJSiYZ-KTtEjzVy0YvK
        PlaylistVideos = Playlist(url=f"https://www.youtube.com/watch?list={playlistId}")
        # PlaylistVideos._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        print("Video id  ",PlaylistVideos)
        
        VideoUrls =  PlaylistVideos.video_urls if len(PlaylistVideos)>0 else []

        data = {}  
        for i,item in enumerate(VideoUrls):
            data[i] = item

        dataUrls['title'] = PlaylistVideos.title if len(PlaylistVideos)>0 else '' 
        dataUrls['length'] = PlaylistVideos.length if len(PlaylistVideos)>0 else '' 
        dataUrls['Views'] = PlaylistVideos.views if len(PlaylistVideos)>0 else '' 
        dataUrls['Urls'] = data
        return HttpResponse(json.dumps(dataUrls))

    return HttpResponse(json.dumps(dataUrls))
        
def LoadVideos(request):
    if request.method=='POST':
        videoId = request.POST.get('url')
        print("video Url is : ",videoId)
        VideoUlr = YouTube(videoId).streams.get_audio_only()
        return HttpResponse(json.dumps({'url':VideoUlr.url,'title':VideoUlr.title,'size':VideoUlr.filesize_mb}))

