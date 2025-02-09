# import pyshorteners
#
#
# long_url = input("Enter Your Url Link \n")
# myTinyUrl= pyshorteners.Shortener()
# short_url= myTinyUrl.tinyurl.short(long_url)
# print("My Short Url Is "+short_url)
#

#
# from rembg import remove
# from PIL import Image
#
#
# inputImgPath="image.jpeg"
# outImgPath="image.png"
#
#
# input=Image.open(inputImgPath)
#
# output= remove(input)
#
# output.save(outImgPath)

# import requests
# from pytube import YouTube
#
# url = input("Enter Your Youtube url here ...")
# ytUrl= requests.get(url)
# urlstr=ytUrl.text
# yt= YouTube(urlstr)
#
#
# audioMP3 =yt.streams.filter(only_audio=True).first()
#
# audioMP3.download()


# 