#SUBIN LAZAR
#10/17/2016
#CS524-02
#Version : Python 3.5.2
#This program illustrates how a ppm image is read and multiple filters are applied to it and stored in a different output file.

"""Importing randint for generation of random numbers and package sys to invoke exit() to exit from the program."""
from random import randint
import sys
s=[]

"""Function enables adding filter invert color on the ppm image. This function reads the image from the input file specified in the parameter 'inputfile'
   and applies filter invert colors on the image and writes to the file mentioned under parameter 'outputfile'.
   Input: 1.inputfile--> Name of the input .ppm file which contains the image.
          2.outputfile--> Name of file which consists of image after applying filter invert colors"""

def invert_ppmimage(inputfile,outputfile): 
    try:
        ipfile = open(inputfile,'r')
        invfile = open(outputfile ,'w')
    except IOError:
       print ("Error: can\'t find file or read data "+inputfile)
       print ("Please enter valid file to read data. File doesn't exist!!!")
       sys.exit()
    else:
        for x in range(0, 3):
            invfile.write(ipfile.readline()) 
        for line in ipfile.readlines():
            linesplit=line.split()
            for word in linesplit:
                word = 255 - int(word)
                invfile.write(str(word))
                invfile.write(' ')
            invfile.write('\n')
        ipfile.close()
        invfile.close()

"""Function enables adding filter grayscale on the ppm image. This function reads the image from the input file specified in the parameter 'inputfile'
   and applies filter grayscale on the image and writes to the file mentioned under parameter 'outputfile'.
   Input: 1.inputfile--> Name of the input .ppm file which contains the image.
          2.outputfile--> Name of file which consists of image after applying filter invert colors"""

def gray_ppmimage(inputfile,outputfile):  
    try:
        ipfile = open(inputfile,'r')
        grayfile = open(outputfile ,'w')
    except IOError:
       print ("Error: can\'t find file or read data "+inputfile)
       print ("Please enter valid file to read data. File doesn't exist!!!")
       sys.exit()
    else:
        for x in range(0, 3):
            grayfile.write(ipfile.readline()) 
        for line in ipfile.readlines():
            linesplit=line.split()
            for word in range(0,len(linesplit),3):
                mean = (int(linesplit[word]) + int(linesplit[word+1]) + int(linesplit[word+2]))/3
                for i in range(0, 3):
                    linesplit[word+i] = int(mean)
                    grayfile.write(str(linesplit[word+i]))
                    grayfile.write(' ')
            grayfile.write('\n')
        ipfile.close()
        grayfile.close()
        
"""Function enables adding filter flatten image on the ppm image. This function reads the image from the input file specified in the parameter 'inputfile'
   and applies filter invert colors on the image and writes to the file mentioned under parameter 'outputfile'.
   Input: 1.inputfile--> Name of the input .ppm file which contains the image.
          2.outputfile--> Name of file which consists of image after applying filter invert colors
          3.color-->Can hold three values as shown below
                    a. 0 - Flattens red
                    b. 1 - Flattens green
                    c. 2 - Flattens blue"""

def flatten_ppmimage(inputfile,outputfile,color):  
    try:
        ipfile = open(inputfile,'r')
        flatfile = open(outputfile ,'w')
    except IOError:
       print ("Error: can\'t find file or read data "+inputfile)
       print ("Please enter valid file to read data. File doesn't exist!!!")
       sys.exit()
    else:
        for x in range(0, 3):
            flatfile.write(ipfile.readline()) 
        for line in ipfile.readlines():
            linesplit=line.split()
            for word in range(0,len(linesplit),3):
                for i in range(0, 3):
                    linesplit[word+color] = 0
                    flatfile.write(str(linesplit[word+i]))
                    flatfile.write(' ')
            flatfile.write('\n')
        ipfile.close()
        flatfile.close()
        
"""Function enables adding filter extreme contrast on the ppm image. This function reads the image from the input file specified in the parameter 'inputfile'
   and applies filter extreme contrast on the image and writes to the file mentioned under parameter 'outputfile'.
   Input: 1.inputfile--> Name of the input .ppm file which contains the image.
          2.outputfile--> Name of file which consists of image after applying filter invert colors"""

def extreme_contrast_ppmimage(inputfile,outputfile):  
    flag='f'
    min=0
    try:
        ipfile = open(inputfile,'r')
        opfile = open(outputfile ,'w')
    except IOError:
       print ("Error: can\'t find file or read data "+inputfile)
       print ("Please enter valid file to read data. File doesn't exist!!!")
       exit()
    else:
        for x in range(0, 3):
            ipfile.readline()
        for line in ipfile.readlines():
            linesplit=line.split()        
            for word in range(0,len(linesplit)-1):
                if flag == 'f':
                    min=int(linesplit[word])
                    flag='t'
                if int(linesplit[word+1])<min:
                    min=int(linesplit[word+1])            
        mid=(min+255)/2
        ipfile = open(inputfile,'r')
        for x in range(0, 3):
            opfile.write(ipfile.readline())
        for line in ipfile.readlines():        
            linesplit=line.split() 
            for word in range(0,len(linesplit)):
                if int(linesplit[word])<=int(mid):
                    linesplit[word]=int(0)
                else:
                    linesplit[word]=int(255)            
                opfile.write(str(linesplit[word]))
                opfile.write(' ')
            opfile.write('\n')    
        ipfile.close()
        opfile.close()
        
"""Function enables adding filter random noise on the ppm image. This function reads the image from the input file specified in the parameter 'inputfile'
   and applies filter random noise on the image and writes to the file mentioned under parameter 'outputfile'.
   Input: 1.inputfile--> Name of the input .ppm file which contains the image.
          2.outputfile--> Name of file which consists of image after applying filter invert colors"""

def rnoise_ppmimage(inputfile,outputfile):  
    try:
        ipfile = open(inputfile,'r')
        noisefile = open(outputfile ,'w')
    except IOError:
       print ("Error: can\'t find file or read data "+inputfile)
       print ("Please enter valid file to read data. File doesn't exist!!!")
       sys.exit()
    else:
        for x in range(0, 3):
            noisefile.write(ipfile.readline()) 
        for line in ipfile.readlines():
            linesplit=line.split()
            for word in range(0,len(linesplit)):
                linesplit[word]=int(linesplit[word])+randint(0,50)
                noisefile.write(str(linesplit[word]))
                noisefile.write(' ')
            noisefile.write('\n')
        ipfile.close()
        noisefile.close()

"""Function takes the name of .ppm file as input from the user, which contains the image on which filters need to be applied.
User will be able to apply multiple filters one after the other. So each time the program is run the desired filter by the user is applied.
So if the user wants to apply 2 filters such as invert colors and flatten red he/she needs to run the program twice firstly selecting the option as 2 which
will apply the filter invert colors and secondly with option 3 which will go ahead and apply the filter flatten red on image with inverted colors.
If the input file to read mentioned by user is not valid or if it is present in the correct location, the program will terminate raising an appropriate
exception displaying the reason to the user"""

def main():
    inputfile= input('Enter name of image file you need to add filters:')
    try:
        ipfile = open(inputfile,'r')        
    except IOError:
       print ("Error: can\'t find file or read data "+inputfile)
       print ("Please enter valid file to read data. File doesn't exist!!!")
       sys.exit()
    else:
        c=0    
        while(True):
            c=c+1
            print ('1.Convert to greyscale')
            print ('2.Invert image colors')
            print ('3.Flatten red')
            print ('4.Flatten green')
            print ('5.Flatten blue')
            print ('6.Extreme contrast')
            print ('7.Random Noise')
            print ('press 0 to exit')
            if c>1:            
                inputfile=filterfile
            filterfile="outputfilter"
            filterfile=filterfile+str(c)
            filterfile=filterfile+".ppm"                
            option= input('Enter your option:')        
            if(option=='1'):
                gray_ppmimage(inputfile,filterfile)
                print('Your ppm image now is in grayscale.The output is in '+filterfile)
            elif(option=='2'):
                invert_ppmimage(inputfile,filterfile)
                print('Your ppm image now is inverted.The output is in '+filterfile)
            elif(option=='3'):
                flatten_ppmimage(inputfile,filterfile,0)
                print('Your ppm image now is flattened red.The output is in '+filterfile)
            elif(option=='4'):
                flatten_ppmimage(inputfile,filterfile,1)
                print('Your ppm image now is flattened green.The output is in '+filterfile)
            elif(option=='5'):
                flatten_ppmimage(inputfile,filterfile,2)
                print('Your ppm image now is flattened blue.The output is in '+filterfile)
            elif(option=='6'):
                extreme_contrast_ppmimage(inputfile,filterfile)
                print('Your ppm image now has extreme contrast.The output is in '+filterfile)
            elif(option=='7'):
                rnoise_ppmimage(inputfile,filterfile)
                print('Your ppm image now has been exposed some random noise.The output is in '+filterfile)        
            elif(option=='0'):
                sys.exit()
            print(" ")
            input1= input("Press any key to continue!")
main()                     

