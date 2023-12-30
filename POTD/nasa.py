import nasapy
# We are going to use the nasapy library to access the information provided by NASA’s API.
import os
#To store the image in a particular directory, we use the os library.
from datetime import datetime
#We use a date while sending a request to NASA API to access the information. To get a date in a specific format, we’ll use a datetime library.
import urllib.request
#The image we get from NASA API will be in a form of a URL, so we use urllib to fetch it.
from IPython.display import Image, display, Audio
#We need to display the image in a jupyter notebook using Ipython library. We will also play the audio explanation of the image using the audio module.
from gtts import gTTS
#We use Google Text to Speech library to convert the text explanation of the image into an audio file.

k="isRrdbhPhG76QlifswnyjK8KCUPToxHhSewQKidC"
nasa=nasapy.Nasa(key=k)

# d=datetime.today().strftime('%Y-%m-%d')
d=input("Enter date in YYYY-MM-DD format :")
apod=nasa.picture_of_the_day(date=d, hd=True)

#point A
#check the media type available
#POINT A:
#Check the media type available:
if(apod["media_type"] == "image"):
    
    #POINT B:
    #Displaying hd images only:
    if("hdurl" in apod.keys()):
        
        #POINT C:
        #Saving name for image:
        title = d + "_" + apod["title"].replace(" ","_").replace(":","_") + ".jpg"
        
        #POINT D:
        #Path of the directory:
        image_dir = "./Astro_Images"

        #Checking if the directory already exists?
        dir_res = os.path.exists(image_dir)
 
        #If it doesn't exist then make a new directory:
        if (dir_res==False):
            os.makedirs(image_dir)

        #If it exist then print a statement:
        else:
            print("Directory already exists!\n")
        
        #POINT E:
        #Retrieving the image:
        urllib.request.urlretrieve(url = apod["hdurl"] , filename = os.path.join(image_dir,title))
        
        #POINT F:
        #Displaying information related to image:
        
        if("date" in apod.keys()):
            print("Date image released: ",apod["date"])
            print("\n")
        if("copyright" in apod.keys()):
            print("This image is owned by: ",apod["copyright"])
            print("\n")
        if("title" in apod.keys()):
            print("Title of the image: ",apod["title"])
            print("\n")
        if("explanation" in apod.keys()):
            print("Description for the image: ",apod["explanation"])
            print("\n")
        if("hdurl" in apod.keys()):
            print("URL for this image: ",apod["hdurl"])
            print("\n")
        
        #POINT G:
        #Displaying main image:
        display(Image(os.path.join(image_dir,title)))
        
        #Point H:
        #Text to Speech Conversion:
        #Take input from user:
        print("\n")
        choice = input("Press * to hear the audio explanation : ")

        if choice=="*":
            #Text to be converted:
            mytext = apod["explanation"]
            #mytext="Good Evening Pratik."

            #Creating an object:
            myobj = gTTS(text=mytext, lang="en", slow=False) 
            
            #Generating audio file name:
            audio_title = d + "_" + apod["title"] + ".mp3"
            
            #Save the converted file:
            myobj.save(os.path.join(image_dir,audio_title)) 

            #Name of sound file:
            sound_file = os.path.join(image_dir,audio_title)

            # Playing the converted file 
            display(Audio(sound_file, autoplay=True))
            
    

#POINT I:
#If media type is not image:
else:
    print("Sorry, Image not available!")