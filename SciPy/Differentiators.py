
def twoPtForwardDiff(x,y):
        """takes arguments as arrays of values x and y(x) and return derivates
        of y with respect to x using Forward Difference"""
        
        # get values of f(x+h) - f(x)
        dy = np.diff(y)
        # get values of h
        dx = np.diff(x)
        
        # dydx with Forward Difference
        dydxF = np.zeros(y.shape,float)
        dydxF[0:-1] = np.diff(y)/np.diff(x)
        
        # dydx with Centered Difference for the last element since there is
        # no f(x+h) to calculate Forward Difference
        dydxF[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
          
        return dydxF
        
def twoPtCenteredDiff(x,y):
    """takes arguments as arrays of values x and y(x) and return derivates
    of y with respect to x using Centered Difference"""
        
    # dydx with Centered Difference
    dydxC = np.zeros(y.shape,float)
    dydxC[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
        
    # dydx with Forward Difference for first element since there is no
    # previous data point to calculate Centered Difference
    dydxC[0] = (y[1]-y[0])/(x[1]-x[0])
        
    # dydx with Backward Difference for last element since there is no
    # next data point to calculate Centered Difference
    dydxC[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
        
    return dydxC

def fourPtCenteredDiff(x,y):
    """ take x and y arrays and calculate dy/dx using Center Difference """
    
    # calculate dy/dx using 4-pt Centered Difference
    dydx4 = np.zeros(y.shape, float)
    dydx4[2:-2] = (y[:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:]) / (12 * (x[1]-x[0]))
    
    # Forward difference
    dydx4[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx4[1] = (y[2]-y[1])/(x[2]-x[1])
    
    # Backward difference
    dydx4[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    dydx4[-2] = (y[-2] - y[-3])/(x[-2] - x[-3])
    
    return dydx4