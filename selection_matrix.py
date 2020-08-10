def selection_matrix(H3D, medzmag, zedges):
    # for use with median_zmag.py
    # lum_limit == luminosity threshold
    # x,y,z == arrays involved in the 3D histogram
    # lum = log luminosity array; same size as x (or y or z)
    # xedges,yedges,zedges = boundaries to search for x,y,z

    import numpy as np

    selection_array = np.empty_like(H3D)

    # This loop finds the cells in color-color space that are brighter in the observed zmag than the median zmag
    # and makes a mask of 1s and 0s
    for i in range(len(selection_array)):
        for j in range(len(selection_array[i])):
            for k in range(len(selection_array[i][j])):
                if (medzmag[i][j] >= zedges[k + 1]):
                    #                 if ((medzmag[i][j] >= 22.02509002685544) & (22.02509002685544 >= zedges[k+1])):
                    selection_array[i][j][k] = 1
                else:
                    selection_array[i][j][k] = 0

    return selection_array