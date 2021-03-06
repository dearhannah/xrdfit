import numpy as np

def curveread(curvetype,infilename):
    """
    This function is to read data from xrd curve.
    curvetype: 'character','continous','diffracton'.
    infilename: the name of input file.
    """
    StartAngle = 20
    StopAngle = 46
    NumPoints = 500
    StepSize = 0.02
    Wavelength = 1.540562
    theta2 = np.random.rand(1, NumPoints)
    intensity = np.random.rand(1,NumPoints)
    curve = np.vstack((theta2, intensity)).T
    return curve

