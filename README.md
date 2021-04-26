# X-Ray diffraction analysis

In this program, I developde a set of tools to analyse the X-ray diffraction spectrum.

First of all, my code can read data files and plot the corresponding spectrums. The inputs are usually txt files, which saved thetas and the corresponding light intensities (usually called counts per second (CPS) because intensity is measured by counting the number of phonons).

Second, I can prepare the data for future analysis through the following steps:
1. clear the background.
2. smooth the curve (or fitting the curve).
3. label the data if it is not reliable.

Finally, I can do common analysis of spectrums:
1. find the peaks and label them.
2. calculate the lattice parameter. 