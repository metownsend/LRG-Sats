def median_zmag(H2D, lum_limit, lum, x, y, z, xedges, yedges):
    # For use with selection_matrix.py
    # lum_limit == log(luminosity threshold)
    # x,y,z == arrays involved in the 3D histogram
    # lum = log luminosity array; same size as x (or y or z)
    # xedges,yedges = boundaries to search for x,y

    import numpy as np

    temp = []
    medzmag = np.full_like(H2D, -999., dtype=float)

    # This loop finds the observed zmag that cooresponds to the luminosity limit for each cell in color-color space
    for i in range(len(xedges) - 1):
        for j in range(len(yedges) - 1):
            for m in range(len(x)):
                if ((x[m] >= xedges[i]) & (x[m] <= xedges[i + 1]) & (y[m] >= yedges[j]) & (y[m] <= yedges[j + 1])):
                    if (abs(lum[m] - lum_limit) < 0.2):
                        temp.append(z[m])
                    if (len(temp) > 0.):
                        medzmag[i][j] = np.median(list(temp))

        temp = []

    return medzmag