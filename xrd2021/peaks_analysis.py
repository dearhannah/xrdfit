import numpy as np
import math as mt
from xrd2021.element_data import crystal


def peakfinder(curve_):
    """
    This function is to find the positions of peaks in a curve.
    """
    C = curve_
    theta_peaks = []
    CPS = C.CPS
    theta2 = C.theta2_deg
    p = []

    for i in range(len(CPS)):
        if i == 0 or i == len(CPS) - 1:
            continue
        if CPS[i] > CPS[i-1] and CPS[i] > CPS[i+1]:
            theta_peaks.append(theta2[i])
            p.append(i)

    theta_peaks = np.array(theta_peaks)
    return theta_peaks, p


def peakindex(theta_peaks, wavelength, element):
    """
    This function will index the peak, giving the hkl of the peak.
    This is for diffraction, but not for element characteristic curve. 
    So, this function is about structure information.
    """
    index = np.zeros((len(theta_peaks), 3))
    cs_ref, a_ref, b_ref, c_ref = crystal(element)

    if cs_ref == 'BCC':
        index_possible = np.array(
            [[0, 1, 1], [0, 0, 2], [1, 1, 2], [0, 2, 2], [0, 1, 3]])
    elif cs_ref == 'FCC':
        index_possible = np.array(
            [[1, 1, 1], [0, 0, 2], [0, 2, 2], [1, 1, 3], [2, 2, 2]])
    elif cs_ref == 'Diamond_Cubic':
        index_possible = np.array([[1, 1, 1], [0, 2, 2], [1, 1, 3], [0, 0, 4],
                                   [1, 3, 3], [2, 2, 4], [1, 1, 5], [3, 3, 3]])
    else:
        print("Database is limited, so...")

    for index_ in index_possible:
        h = index_[0]
        k = index_[1]
        l = index_[2]
        d_p = a_ref/mt.sqrt(h**2+k**2+l**2)
        theta_p = np.arcsin(wavelength/(2*d_p))/3.14*180

        for i in range(len(theta_peaks)):
            if (index[i] == [0, 0, 0]).all():
                if abs(theta_peaks[i]-2*theta_p) <= 1:
                    index[i] = index_
                    break
    return index


def lattice_parameter_calculator(theta_peaks, wavelength, index):
    """
    This function is to calculat the real lattice parameter from the experiments.
    """
    ds = np.zeros(len(theta_peaks))
    a = 0.

    for i in range(len(theta_peaks)):
        ds[i] = wavelength/(2*mt.sin(theta_peaks[i]*3.14/180/2))
        a += ds[i]*mt.sqrt(index[i][0]**2+index[i][1]**2+index[i][2]**2)
    a /= len(theta_peaks)
    return a
