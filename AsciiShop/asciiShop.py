"""
Braden Harrelson
Kevin Ellis

2143-OOP
3/1/16
"""

"""
REQUIREMENTS:
pillow(PIL)
urllib3  !!!

** Notice Cat has been implemented within the program**

"""

import urllib3, uuid, os, sys

url = 'http://thecatapi.com/api/images/get'

def getCat(directory=None, filename=None, format='png'):
    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), format)
    savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    downloadlink = url + '?type=%s' % format
    http = urllib3.PoolManager()
    r = http.request('GET', downloadlink)
    fp = open(savefile, 'wb')
    fp.write(r.data)
    fp.close()
    return savefile
import time
from PIL import Image

class RandomCat(object):

    def __init__(self):

        self.name = ''          # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'
        self.width = 0          # width of image
        self.height = 0         # height of image        
        self.img = None         # Pillow var to hold image

    """
    @Name: getImage
    @Description:
        This method will get a cat image from the web and timestamp it to give it a name
    @Params: None
    @Returns: None
    """
    def getImage(self):
        self.name = self.getTimeStamp()
        getCat(directory=self.path, filename=self.name, format=self.format)
        self.img = Image.open(self.name+'.'+self.format)
        
        self.width, self.heigth = self.img.size
        
    """
    @Name: saveImage
    @Description:
        This method will save the image
    @Params: None
    @Returns: None
    """
    def saveImage(self):
        pass

    """
    @Name: nameImage
    @Description:
        This method will name the image
    @Params: None
    @Returns:None
    """
    def nameImage(self):
        pass

    """
    @Name: getTimeStamp
    @Description:
        This method will get the time to name the images from the web
    @Params: None
    @Returns: time as an int
    """
    def getTimeStamp(self):
        seconds,milli = str(time.time()).split('.')
        return seconds 


""" 
The ascii character set we use to replace pixels. 
The grayscale pixel values are 0-255.
0 - 25 = '#' (darkest character)
250-255 = '.' (lightest character)
"""


class AsciiImage(RandomCat):

    def __init__(self,new_width="not_set"):
        super(AsciiImage, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0
            
        self.asciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.inverted = None
        self.imageAsAscii = []
        self.matrix = None
        
        
    """
    @Name: ConvertToAscii
    @Description:
        This method will turn an image into an ascii based image
    @Params: None
    @Returns: None
    """
    def convertToAscii(self):
    
        if self.newWidth == "not_set":
            self.newWidth = self.width
            
        self.newHeight = int((self.heigth * self.newWidth) / self.width)
            
        if self.newWidth == None:
            self.newWidth = self.width
            self.newHeight = self.height
            
        self.newImage = self.img.resize((self.newWidth, self.newHeight))
        self.newImage = self.newImage.convert("L") # convert to grayscale
        all_pixels = list(self.newImage.getdata())
        self.matrix = listToMatrix(all_pixels,self.newWidth)
        

        for pixel_value in all_pixels:
            index = pixel_value // 25 # 0 - 10
            self.imageAsAscii.append(self.asciiChars[index])
              

    """
    @Name: printImage
    @Description:
        This method will output an image in ascii
    @Params: None
    @Returns: None
    """
    def printImage(self):
        self.imageAsAscii = ''.join(ch for ch in self.imageAsAscii)
        for c in range(0, len(self.imageAsAscii), self.newWidth):
            print (self.imageAsAscii[c:c+self.newWidth])
            
    """       
    @Name: flip
    @Description:
        This method will flip an image horizontally, or vertically. 
        Vertically means all pixels in row 0 => row N, row 1 => row N-1, ... row N/2 => row N/2+1
        Horizontally means all pixels in col 0 => col N, col 1 => col N-1, ... col N/2 => col N/2+1
    @Params: direction (string) - [horizontal,vertical] The direction to flip the cat.
    @Returns: (string) - Flipped ascii image.
    """
    def flip(self,direction):
        if direction == 'V':
            return self.imageAsAscii.reverse()
        elif direction == 'H':
            array = []
            temp = listToMatrix(self.imageAsAscii,self.newWidth)
            self.imageAsAscii = []
            for h in range(self.newHeight):
                array = temp[h][:]
                array.reverse()
                self.imageAsAscii += array
            return self.imageAsAscii
                    
        else:
            print("Invalid Direction")

    """
    @Name: invert 
    @Description:
        This method will take all the lightest pixels and make them the darkest, next lightest => next darkest, etc..
    @Params: None
    @Returns: (string) - inverted image
    """
    def invert(self):
        self.imageAsAscii = []
        temp = self.asciiChars
        temp.reverse()
        self.inverted = temp
        all_pixels = list(self.newImage.getdata())
        self.matrix = listToMatrix(all_pixels,self.newWidth)
        
        for pixel_value in all_pixels:
            index = pixel_value // 25 # 0 - 10
            self.imageAsAscii.append(self.inverted[index])
        return self.imageAsAscii

"""
Convert to 2D list of lists to help with manipulating the ascii image.
Example:
    
    L = [0,1,2,3,4,5,6,7,8]
    
    L = to_matrix(L,3)
    
    L becomes:
    
    [[0,1,2],
    [3,4,5],
    [6,7,8]]
"""

"""
@Name: listToMatrix
@Description:
This method will turn a list into a 2d matrix
@Params: list , number
@Returns: matrix
"""
def listToMatrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]
    
if __name__=='__main__':
    #create an instance of the class
    awesomeCat = AsciiImage(150)
    #get an image from the web
    awesomeCat.getImage()
    #convert the image to ascii
    awesomeCat.convertToAscii()
    #print out normal ascii image
    awesomeCat.printImage()    
    #invert the image
    awesomeCat.invert()
    #Flips the image either horizontally with 'H' or vertically with 'V'
    awesomeCat.flip('H')
    #displays the image flipped and inverted!
    awesomeCat.printImage()