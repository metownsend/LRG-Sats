def making_masks(lum_limit, x, y, z, lum, xedges, yedges, zedges):
    # lum_limit == luminosity threshold
    # x,y,z == arrays involved in the 3D histogram
    # lum = luminosity array; same size as x (or y or z)
    # xedges,yedges,zedges = boundaries to search for x,y,z

    import numpy as np

    lumlistmed = []
    lumlist = []
    temp = []
    for j in range(len(xedges) - 1):
        for k in range(len(yedges) - 1):
            for m in range(len(zedges) - 1):
                for i in range(len(x)):
                    if ((x[i] >= xedges[j]) & (x[i] <= xedges[j + 1]) & (y[i] >= yedges[k]) & (
                            y[i] <= yedges[k + 1]) & (z[i] >= zedges[m]) & (z[i] <= zedges[m + 1])):
                        temp.append(lum[i])
                if (np.median(temp) > 0.):
                    lumlistmed.append(np.median(temp))
                    lumlist.append(temp)
                else:
                    lumlistmed.append(0)
                temp = []

    lumlistmed3D = np.reshape(lumlistmed, (3, 3, 3))

    mask_array = np.empty((3, 3, 3))
    for i in range(len(lumlistmed3D)):
        for j in range(len(lumlistmed3D[i])):
            for k in range(len(lumlistmed3D[i][j])):
                if (lumlistmed3D[i][j][k] > lum_limit):
                    mask_array[i][j][k] = 1
                else:
                    mask_array[i][j][k] = 0
    return mask_array