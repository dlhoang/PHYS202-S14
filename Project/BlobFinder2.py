
import matplotlib.pyplot as plt
from PIL import Image
import requests
from StringIO import StringIO

# define colors
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)

# creating a blob
class Blob():

    def __init__(self):
        """ initializes a blob """
        self.blob = []
    def add(self,i,j):
        """ adds (x,y) position of a pixel that is part of a blob """
        self.blob.append([i,j])
    def mass(self):
        """ returns mass of a blob determined by how many pixels it contains """
        return len(self.blob)

    def distanceTo(self,blob):
        """ returns distance from current blob to blob being passed in """
        distance = round((((self.centerOfMass()[0] - blob.centerOfMass()[0])**2)\
                        + ((self.centerOfMass()[1] - blob.centerOfMass()[1])**2))**0.5,4)
        return distance

    def centerOfMass(self):
        """ returns (x,y) position of center of mass (center) of blob """
        xtot, ytot = 0, 0
        for pix in self.blob:
            xtot = xtot + pix[0]
            ytot = ytot + pix[1]
        xcm = float(xtot)/float(len(self.blob))
        ycm = float(ytot)/float(len(self.blob))
        return xcm, ycm

def monochrome(picture,tau):
    """ turns blobs in a picture red using luminance threshold tau and turn background noise black """
    xsize, ysize = picture.size
    temp = picture.load()

    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            # if color is higher than luminance threshold, consider a blob and turn red
            if (r+g+b)/3 <= tau:
                temp[x,y] = RED
            # else consider background noise and turn black
            else:
                temp[x,y] = BLACK

def BlobFinder(picture, tau):
    """ returns a list of all blobs in the picture using the luminance threshold tau """
    # turns picture red and black first
    monochrome(picture,tau)
    xsize, ysize = picture.size
    temp = picture.load()
    blobs = []
    for x in range(xsize):
        for y in range(ysize):
            # find blobs in picture and add to list of blobs
            if temp[x,y] == RED:
                blob = Fill(temp,xsize,ysize,x,y)
                blobs.append(blob)
    return blobs
    
def Fill(picture, xsize, ysize, xstart, ystart):
    """ keep a list of pixels that need to be looked at, 
    but haven't yet been filled in - a list of the (x,y) 
    coordinates of pixels that are neighbors of ones we have 
    already examined.  Keep looping until there's nothing 
    left in this list. Finally returns the blob. """
    # create a blob
    blob = Blob()
    queue = [(xstart,ystart)]
    # add the first red pixel found
    blob.add(xstart,ystart)
    while queue:
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
        # if neighboring pixel is red, add to queue, fill white, and add to blob object
        if picture[x,y] == RED:
            picture[x,y] = WHITE
            blob.add(x,y)
            if x > 0:
                queue.append((x-1,y))
            if x < (xsize-1):
                queue.append((x+1,y))
            if y > 0:
                queue.append((x, y-1))
            if y < (ysize-1):
                queue.append((x, y+1))
    return blob
 
                    
def countBeads(P,picture,tau):
    """ returns the number of blobs with mass >= P pixels """
    # get all blobs in a picture with luminance threshold tau
    beads = BlobFinder(picture,tau)
    count = 0
    # loop through all blobs -- if mass >= P, increment count
    for bead in beads:
        if bead.mass() >= P:
            count = count + 1
    return count
    
def getBeads(P,picture,tau):
    """ returns a list of all blobs with mass >= P pixels """
    # get all blobs in a picture with luminance threshold tau
    beads = BlobFinder(picture,tau)
    # initialize a list of blobs
    blobs = []
    # loop through all blobs -- if mass >= P, add blob to list of blobs
    for bead in beads:
        if bead.mass() >=P:
            blobs.append(bead)
    return blobs
             
def printBeads(P,picture,tau):
    """ first print mass and corresponding center of mass of blobs with mass >= P,
    then print mass and corresponding center of mass of all blobs found regardless """
    # get all blobs in a picture with luminance threshold tau
    beads = BlobFinder(picture,tau)

    # print characteristics of blobs with mass >= P
    print "Beads with at least %s pixels" %P
    for bead in beads:
        if bead.mass() >= P:
            print "mass: %s" %bead.mass()
            print "center of mass: %s %s" %bead.centerOfMass()
            
    # print characteristics of all blobs found
    print "All founded beads: "
    for bead in beads:
        print "mass: %s" %bead.mass()
        print "center of mass: %s %s" %bead.centerOfMass()