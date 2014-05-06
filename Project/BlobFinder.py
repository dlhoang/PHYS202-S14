%pylab inline
import numpy as np
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
        self.blob.append[(i,j)]
    def mass():
        return len(self.blob)
    def distanceTo(blob):
        distance = round(sqrt(((self.centerOfMass()[0] - blob.centerOfMass()[0])**2)\
                        + ((self.centerOfMass()[1] - blob.centerOfMass()[1])**2)),4)
    def centerOfMass():
        xtot, ytot = 0, 0
        for pix in self.blob:
            xtot = xtot + pix[0]
            ytot = ytot + pix[1]
        xcm = float(xtot)/float(len(self.blob))
        ycm = float(ytot)/float(len(self.blob))
        return xcm, ycm

def monochrome(picture, tau):
    xsize, ysize = picture.size
    temp = picture.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b <= threshold: 
                temp[x,y] = BLACK
            else:
                temp[x,y] = WHITE   
    
def fill(picture, xsize, ysize, xstart, ystart):
    queue = [(xstart,ystart)]
    blob = Blob()
    blob.add(xstart,ystart)
    while queue:
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
        if picture[x,y] == BLACK:
            picture[x,y] = RED
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
                
                
def BlobFinder(picture, tau):
    '''find all blobs in the picture using the luminance threshold tau'''
    blobs = []   
    blob = fill(picture, tau)
    blobs.append(blob)
    return beads
                    
def countBeads(P,picture,tau):
    '''return the number of beads with >= P pixels'''
    blob = Blob()
    beads = BlobFinder(picture,tau)
    count = 0
    for blob in beads:
        if blob.mass() >= P:
            count = count + 1
    return count
    
def getBeads(P,picture,tau):
    '''return all beads with >= P pixels'''
    blob = Blob()
    beads = BlobFinder(picture,tau)
    blobs = []
    for blob in beads:
        if blob.mass() >=P:
            blobs.append(blob)
    return blobs
             
def printBeads(P,picture,tau):
    pic = Image.open(picture)
    beads = BlobFinder(pic,tau)
    for bead in getBeads(P,picture,tau):
        if bead.mass() >= P:
            print "Beads with at least %s pixels", %P + "\n"
            print "mass: " + bead.mass() + "\n"
            print "center of mass: " + bead.centerOfMass() + "\n"
    
    for bead in getBeads(P,picture,tau):
        print "All founded beads: " + "\n"
        print "mass: " + bead.mass() + "\n"
        print "center of mass: " + bead.centerOfMass() + "\n"
        
blob = Blob()
blob.add(1,3)
print blob