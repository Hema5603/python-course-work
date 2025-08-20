#single Inheritance
class status:
    def upload_image(self,imageurl):
        self.imageurl=imageurl
        return f"{self.imageurl} is uploaded"
Hema=status()
print(Hema.upload_image("selfie.png"))
class statusv1(status):
    def caption(self,text):
        self.text=text
        return f"{self.txt} is added"
vishnu=statusv1()
print(vishnu.upload_image("rakshabandhan.png"))
print(vishnu.upload_image("Happy raksha bandhan"))
#hierarical inheritance
class status:
    def upload_image(self,imageurl):
        self.imageurl=imageurl
        return f"{self.imageurl} is uploaded"
Hema=status()
print(Hema.upload_image("selfie.png"))
class statusv1(status):
    def caption(self,text):
        self.text=text
        return f"{self.txt} is added"
vishnu=statusv1()
print(vishnu.upload_image("rakshabandhan.png"))
print(vishnu.upload_image("Happy raksha bandhan"))
class statusv2(status):
    def addmusic(self,music):
        self.music=music
        return f"{self.music} is added"
sravani=statusv2()
print(sravani.upload_image("trecking.jpng"))
print(sravani.addmusic("krishnafute.mp3"))
#multipe inheritance
class status:
    def upload_image(self,imageurl):
        self.imageurl=imageurl
        return f"{self.imageurl} is uploaded"
Hema=status()
print(Hema.upload_image("selfie.png"))
class statusv1(status):
    def caption(self,text):
        self.text=text
        return f"{self.text} is added"
vishnu=statusv1()
print(vishnu.upload_image("rakshabandhan.png"))
print(vishnu.upload_image("Happy raksha bandhan"))
class statusv2(status):
    def addmusic(self,music):
        self.music=music
        return f"{self.music} is added"
sravani=statusv2()
print(sravani.upload_image("trecking.jpng"))
print(sravani.addmusic("krishnafute.mp3"))
class statusv3(statusv1,statusv2):
    def videoduration(self,duration):
        self.duration=duration
        return f"{self.duration} minutes is video duration"
krishna=statusv3()
print(krishna.upload_image("Ganesh image.jpng"))
print(krishna.addmusic("ganeshsong.mp3"))
print(krishna.caption("Happy vinayaka chavithi"))
print(krishna.videoduration(4))
#multilevel inheritance
class status:
    def upload_image(self,imageurl):
        self.imageurl=imageurl
        return f"{self.imageurl} is uploaded"
Hema=status()
print(Hema.upload_image("selfie.png"))
class statusv1(status):
    def addmusic(self,music):
        self.music=music
        return f"{self.music} is added"
vishnu=statusv1()
print(vishnu.upload_image("rakshabandhan.jpg"))
print(vishnu.addmusic("sistersong.mp3"))

class statusv2(statusv1):
    def like(self,canlike):
        self.canlike=canlike
        return f"{self.canlike} is updated"
krishna=statusv2()
print(krishna.upload_image("vinayaka.jpg"))
print(krishna.addmusic("vinayakasong.mp3"))
print(krishna.like("emoji"))
class statusv3(statusv2):
    def addcaption(self,caption):
        self.caption=caption
        return f"{caption} is added"
ramadevi=statusv3()
print(ramadevi.upload_image("family photo.jpg"))
print(ramadevi.addmusic("familysong.mp3"))
print(ramadevi.like("happyemoji"))
print(ramadevi.addcaption("Mylife"))










        
