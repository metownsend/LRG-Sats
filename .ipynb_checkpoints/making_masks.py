def making_masks(H1, lum_limit, x, y, z, lum, xedges, yedges, zedges):
    # lum_limit == luminosity threshold
    # x,y,z == arrays involved in the 3D histogram
    # lum = luminosity array; same size as x (or y or z)
    # xedges,yedges,zedges = boundaries to search for x,y,z

    import numpy as np

    temp = []
    lumlist = np.zeros_like(H1, dtype=float)
    #     indexlist = np.zeros((2,2,2),dtype=list)

    for i in range(len(xedges) - 1):
        for j in range(len(yedges) - 1):
            for k in range(len(zedges) - 1):
                for m in range(len(x)):
                    if ((x[m] >= xedges[i]) & (x[m] <= xedges[i + 1]) & (y[m] >= yedges[j]) & (
                            y[m] <= yedges[j + 1]) & (z[m] >= zedges[k]) & (z[m] <= zedges[k + 1])):
                        temp.append(lum[m])
                    if (len(temp) > 0.):
                        lumlist[i][j][k] = np.median(list(temp))
                    #                         indexlist[i][j][k] = list(temp)
                    else:
                        lumlist[i][j][k] = 0.
            temp = []

    test_array = lumlist

    mask_array = np.empty_like(H1)
    for i in range(len(test_array)):
        for j in range(len(test_array[i])):
            for k in range(len(test_array[i][j])):
                if (test_array[i][j][k] > lum_limit):
                    mask_array[i][j][k] = 1
                else:
                    mask_array[i][j][k] = 0

    return mask_array