'''from abc import ABC,abstractmethod
class upload(ABC):
    @abstractmethod
    def compress(self):
        pass
class image(upload):
    def compress(self):
        print("image is compressed to 3mb")
class video(upload):
    def compress(self):
        print("video is compressed to 4mb")
    def pdfconverter(self):
        print("converted to pdf")
i=image()
v=video()
i.compress()
v.compress()
v.pdfconverter()
from abc import ABC,abstractmethod
class order(ABC):
    @abstractmethod
    def foodorder(self):
        pass
class meals(order):
    def foodorder(self):
        print("meals order is successfull")
class chickenbiryani(order):
    def foodorder(self):
        print("chickenbiryani order is successful")
class manchuriya(order):
    def foodorder(self):
        print("manchuriya order is successful")
class noodles(order):
    def foodorder(self):
        print("noodles order is successful")
class vegbiryani(order):
    def foodorder(self):
        print("vegbiryani order is successful")
class fruit_juice(order):
    def foodorder(self):
        print("fruit_juice order is successful")
l=[meals(),chickenbiryani(),manchuriya(),noodles(),vegbiryani(),fruit_juice()]
def place_order(Order:order):
    Order.foodorder()
for i in l:
    place_order(i)
from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def makepayment(self,amount):
        pass
class phonepay(payment):
    def makepayment(self,amount):
        print(f"{amount} is debited through phonepay")
class gpay(payment):
    def makepayment(self,amount):
        print(f"{amount} is debited through gpay")
class paytm(payment):
    def makepayment(self,amount):
        print(f"{amount} is debited through paytm")
class paypal(payment):
    def makepayment(self,amount):
        print(f"{amount} is debited through paypal")
phonepay='''

    




