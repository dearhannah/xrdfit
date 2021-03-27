import numpy as np


def peakfinder(curve):
    """
    This function is to find the positions of peaks in a curve.
    I will set a minmum value for peak intensity, which means that this function may ignore some small peaks.
    I will work on some make-ups.
    """
    theta_peaks = [33.350, 40.400, 56.550]
    return theta_peaks


def peakindex(theta_peaks, wavelength, element):
    """
    This function will index the peak, giving the hkl of the peak
    This is for diffraction, but not for element characteristic curve. 
    So, this function is about structure information.
    """
    index = np.random.randn(len(theta_peaks), 3)
    return index


def abd_calculator(theta_peaks, wavelength, index):
    """
    This function is to calculat the real lattice parameter from the experiments.
    """
    return a, b, c
