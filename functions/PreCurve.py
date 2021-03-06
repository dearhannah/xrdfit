import numpy as np

def clear(curve):
    """
    This function is will delete the continuous background intensity and return a modified curve.
    Generally, the continuous curve will be a constant through out the whole curve.
    """
    curve_noBackground = np.random.randn(*curve.shape)
    return curve_noBackground

def smooth(curve):
    """
    This function is to smooth the curve, so some small noise peak will not influence the accuracy of peak finding.
    """
    curve_smooth = np.random.randn(*curve.shape)
    return curve_smooth

def picky(curve):
    """
    This function is to tell whether the curve is too noisy to be deal with.
    It will return 'True' or 'False" based on some criteria. 
    If it returns 'false', it will plot the curve. 
    So this function will be very picky and will let user make decision on some special cases.
    """
    return True

