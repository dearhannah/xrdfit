import numpy as np
import matplotlib.pyplot as plt
import lmfit


class curve:
    """
    This class is for all curves.
    basic information will be saved.
    And plot and curve fitting and smoothing will be realized.
    """

    def __init__(self, curvetype, infilename):
        """
        curvetype: 'character','diffracton'.
        infilename: the name of input file.
        """
        # Read data and put them into variables.
        arr = np.genfromtxt(infilename, skip_header=109)

        self.theta2_deg = arr[:, 0]
        self.CPS = arr[:, 1]
        self.EDS = arr[:, 2]
        if len(self.CPS) <= 100:
            raise ValueError("You may want more data points!")

        with open(infilename) as f:
            para = f.readlines()[4:13]

        self.start_angle = float(para[1].split()[2])
        self.stop_angle = float(para[2].split()[2])
        self.num_points = float(para[3].split()[2])
        self.step_size = float(para[4].split()[2])
        self.wavelength = float(para[8].split()[1])
        if curvetype not in ['character', 'diffracton']:
            raise ValueError("The type of curve should be either 'character' or 'diffracton'. \
            'character' means that you do not know what is the material that produce the x-ray. \
            'diffracton' means that you want to learn the materials' structure.")
        else:
            self.c_type = curvetype
        self.curvename = infilename
        self.index = None
        self.peaks_position = None

        self.pick = True

    def plot(self, log_scale=False, show_points=False):
        """
        This function is used to plot the curve.
        """
        if show_points:
            line_spec = "."
        else:
            line_spec = "-"
        # plot the curve
        plt.figure(figsize=(8, 8))
        plt.plot(self.theta2_deg, self.CPS, line_spec,
                 label=self.curvename, linewidth=1)
        if log_scale:
            plt.yscale("log")
        if self.index is not None:
            for i, j in zip(self.peaks_position, self.index):
                plt.text(self.theta2_deg[i], self.CPS[i]*0.9, str(j))
        # formatting for pictures
        plt.minorticks_on()
        plt.ylabel("CPS")
        plt.xlabel('2\u03B8')
        plt.title('intensity-2\u03B8')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(self.curvename[:-4])

    def picky(self, flag=True):
        """
        This function is to tell whether the curve is too noisy to be deal with.
        If it returns 'false', this means that the curve is too noisy and it will plot the curve. 
        So this function will be very picky and will let user make decision on some special cases.
        """
        self.pick = flag
        if not flag:
            self.plot()

    def clear_background(self):
        """
        This function is will delete the continuous background intensity and return a modified curve.
        Generally, the continuous curve will be a constant through out the whole curve.
        """
        continuous = np.min(self.CPS)
        self.CPS = self.CPS - continuous
        self.plot(log_scale=False, show_points=False)

    def fit(self, maximas, show=True):
        """
        This function is for fitting the curve.
        maximas: np.array, stored the estimated peak positions from the curve. We can read this from the curve.
        """
        if isinstance(maximas, np.ndarray):
            maxima = maximas
        else:
            raise TypeError("maximas should be a np.array, stored the estimated peak positions from the curve. \
            We can read this from the curve.")
        model = None
        num_maxima = len(maxima)

        # Add one peak to the model for each maximum
        for maxima_num in range(num_maxima):
            prefix = f"maximum_{maxima_num}_"
            if model:
                model += lmfit.models.PseudoVoigtModel(prefix=prefix)
            else:
                model = lmfit.models.PseudoVoigtModel(prefix=prefix)
        fit_result = model.fit(self.CPS, x=self.theta2_deg)

        if show:
            self.plot_fit(fit_result, log_scale=False)

        return fit_result

    def plot_fit(self, fit_result, log_scale=False,):
        """
        This function is to plot fitting curve.
        """
        x_data = self.theta2_deg
        y_fit = fit_result.model.eval(fit_result.params, x=x_data)

        flag_log = log_scale
        self.plot(log_scale=flag_log, show_points=True)
        plt.plot(x_data, y_fit, 'k', lw=1, label="Fit")
        plt.legend()
        plt.savefig(self.curvename[:-4]+'_fit')
