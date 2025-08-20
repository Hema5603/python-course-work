class status:
    def __init__(self,upload_photo):
        self.upload_photo=upload_photo
        print(f"{self.upload_photo} is updated")
    def addcaption(self,caption):
        self.caption
class statusv1(status):
    def __init__(self,bio,upload_photo):
        self.bio=bio
        super().__init__(upload_photo)
        print(f"{self.bio} is updated")
statusv1("I am nature","hema.jpg")
class



