def cmdHistograms(H, edges):

    # This function plots a color-magnitude 2D histogram for satellites around LRG; produces a histogram for every LRG

    import matplotlib.pyplot as plt
    import numpy as np

    plt.rcParams.update({'figure.max_open_warning': 0})

    for i in range(len(H)):
        # make 2D projections of 3D histogram
        rz_v_zmag = H[i][:, :, :].sum(axis=2)
        rz_vs_zmag = np.flipud(rz_v_zmag)
        gr_v_zmag = H[i][:, :, :].sum(axis=0)
        gr_vs_zmag = np.flipud(gr_v_zmag.T)
        gr_v_rz = H[i][:, :, :].sum(axis=1)
        gr_vs_rz = np.flipud(gr_v_rz.T)

        # plot 2D histograms using matshow; 3 plots per image
#         f, axarr = plt.subplots(111, figsize=(10, 10))
#         f.suptitle("Satellite Density CMD (LRG {})".format(i))

        im1 = plt.matshow(rz_vs_zmag, cmap=plt.cm.Purples, extent=[edges[1][0], edges[1][len(edges[1]) - 1], edges[0][0], edges[0][len(edges[0]) - 1]])
        plt.scatter(zmag_LRG[i], rzcolor_LRG[i], color='red', label="LRG")
        plt.title("Satellite Color-Magnitude Diagram (LRG {})".format(i), fontsize=15, pad=5)
#         plt.xaxis.set_ticks_position('bottom')
#         plt.invert_xaxis()
        plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
        plt.gca().invert_xaxis()
#         plt.xlim(22, 10)
        plt.ylim(-5, 5)
#         plt.set(xlabel='zmag', ylabel='(r-z)')
#         plt.set_ylim(bottom=-5, top=5)
        plt.colorbar(im1, fraction=0.08, pad=0.05)
        s = 'LRG redshift: {0:.2f}'.format(z_LRG[i])
        t = 'LRG coords: {:.2f}, {:.2f}'.format(ra_LRG[i], dec_LRG[i])
        plt.text(16, -2, s, family='sans-serif', fontsize=14)
        plt.text(16, -2.5, t, family='sans-serif', fontsize=14)
#         axarr[0].title("Satellite Color-Magnitude Diagram (LRG {})".format(i), fontsize=15)
        plt.xlabel(r'$z-mag$', fontsize=12)
        plt.ylabel(r'$(r-z)$ $color$', fontsize=12)
        plt.legend(loc='upper right', prop={'size': 12})

        # save image with incrementing file name
        plt.savefig('/Users/mtownsend/Desktop/satHistCMDs/satHistCMD{}.jpeg'.format(i))
        # plt.show()