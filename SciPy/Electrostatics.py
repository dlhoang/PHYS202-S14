
import numpy as np

def pointPotential(x,y,q,Xc,Yc):
    """ return electric potential for point charge q at (Xc,Yc)"""
    
    k = 8.987551787997912e9 #(Nm^2/C^2)
    
    Vxy = k*q/np.sqrt(((x-Xc)**2 + (y-Yc)**2))
    return Vxy

def dipolePotential(x,y,q,d):
    """ return electric potential for a pair of point charges +/- q separated by distance d along x axis
    with their midpoint as (0,0)"""
    
    Vxy = pointPotential(x,y,q,-d/2.,0.) + pointPotential(x,y,-q,+d/2.,0.)
    return Vxy