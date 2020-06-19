def making_masks(H2D, H3D, lum_limit, x, y, z, lum, xedges, yedges, zedges):
    # lum_limit == luminosity threshold
    # x,y,z == arrays involved in the 3D histogram
    # lum = luminosity array; same size as x (or y or z)
    # xedges,yedges,zedges = boundaries to search for x,y,z

    import numpy as np

    temp = []
    medzmag = np.zeros_like(H2D, dtype=float)

    # This loop finds the observed zmag that cooresponds to the luminosity limit for each cell in color-color space
    for i in range(len(xedges) - 1):
        for j in range(len(yedges) - 1):
            for m in range(len(x)):
                if ((x[m] >= xedges[i]) & (x[m] <= xedges[i + 1]) & (y[m] >= yedges[j]) & (y[m] <= yedges[j + 1])):
                    if (abs(lum[m] - lum_limit) < 5):
                        temp.append(z[m])
                    if (len(temp) > 0.):
                        medzmag[i][j] = np.median(list(temp))
        temp = []

    median_zmag_array = medzmag

    mask_array = np.empty_like(H3D)

    # This loop finds the cells in color-color space that are brighter in the observed zmag than the median zmag
    # and makes a mask of 1s and 0s
    for i in range(len(mask_array)):
        #     print(mask_array[i])
        #     print(edges2[i+1])
        #     print('----')
        for j in range(len(mask_array[i])):
            for k in range(len(mask_array[i][j])):
                if (median_zmag_array[j][k] >= zedges[i + 1]):
                    mask_array[i][j][k] = 1
                else:
                    mask_array[i][j][k] = 0


    # # Modification made to second loop to determine which axis corresponds to which porjection
    # for i in range(len(mask_array)):
    #     for j in range(len(mask_array[i])):
    #         for k in range(len(mask_array[i][j])):
    #             if ((rz_edges[i] > 2.) & (rz_edges[i] < 6.) & (zmag_edges[k] >= zmag_edges[10]) & (
    #                     zmag_edges[k] <= zmag_edges[16])):
    #                 mask_array[i][j][k] = 1
    #             elif ((rz_edges[i] > 6.) & (zmag_edges[k] >= zmag_edges[10]) & (zmag_edges[k] <= zmag_edges[16])):
    #                 mask_array[i][j][k] = 2
    #             else:
    #                 mask_array[i][j][k] = 0

    return median_zmag_array, mask_array