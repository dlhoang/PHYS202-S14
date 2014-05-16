
import matplotlib.pyplot as plt
from PIL import Image
import requests
from StringIO import StringIO

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)

class Blob():

    def __init__(self):
        self.blob = []
    def add(self,i,j):
        self.blob.append([i,j])
    def mass(self):
        return len(self.blob)
    
    # ROUND TO 4 DECIMALS
    def distanceTo(self,blob):
<<<<<<< HEAD
        distance = round((((self.centerOfMass()[0] - blob.centerOfMass()[0])**2)\
                        + ((self.centerOfMass()[1] - blob.centerOfMass()[1])**2))**0.5,4)
        return distance
    
=======
        distance = format((((self.centerOfMass()[0] - blob.centerOfMass()[0])**2)\
                        + ((self.centerOfMass()[1] - blob.centerOfMass()[1])**2))**5,'.4f')
>>>>>>> 0666384c955edbc0e2a0aec05e6d728eb2217372
    def centerOfMass(self):
        xtot, ytot = 0, 0
        for pix in self.blob:
            xtot = xtot + pix[0]
            ytot = ytot + pix[1]
        xcm = float(xtot)/float(len(self.blob))
        ycm = float(ytot)/float(len(self.blob))
        return xcm, ycm

def monochrome(picture,tau):
    xsize, ysize = picture.size
    temp = picture.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if (r+g+b)/3 >= tau:
                temp[x,y] = RED
            else:
                temp[x,y] = BLACK

def BlobFinder(picture, tau):
    '''find all blobs in the picture using the luminance threshold tau'''
    monochrome(picture,tau)
    xsize, ysize = picture.size
    temp = picture.load()
    blobs = []
    for x in range(xsize):
        for y in range(ysize):
            if temp[x,y] == RED:
                blob = Fill(temp,xsize,ysize,x,y)
                blobs.append(blob)
    return blobs
    
def Fill(picture, xsize, ysize, xstart, ystart):
    """ keep a list of pixels that need to be looked at, 
    but haven't yet been filled in - a list of the (x,y) 
    coordinates of pixels that are neighbors of ones we have 
    already examined.  Keep looping until there's nothing 
    left in this list"""
    blob = Blob()
    queue = [(xstart,ystart)]
    blob.add(xstart,ystart)
    while queue:
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
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
    '''return the number of beads with >= P pixels'''
    beads = BlobFinder(picture,tau)
    count = 0
    for bead in beads:
        if bead.mass() >= P:
            count = count + 1
    return count
    
def getBeads(P,picture,tau):
    '''return all beads with >= P pixels'''
    beads = BlobFinder(picture,tau)
    blobs = []
    for bead in beads:
        if bead.mass() >=P:
            blobs.append(bead)
    return blobs
             
def printBeads(P,picture,tau):
    beads = BlobFinder(picture,tau)
    print "Beads with at least %s pixels" %P
    for bead in beads:
        if bead.mass() >= P:
            print "mass: %s" %bead.mass()
            print "center of mass: %s %s" %bead.centerOfMass()
    print "All founded beads: "
    for bead in beads:
        print "mass: %s" %bead.mass()
        print "center of mass: %s %s" %bead.centerOfMass()