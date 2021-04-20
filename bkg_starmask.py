import numpy as np

# read in data

# LRG
data_raLRG = np.load('/Users/mtownsend/Documents/LRG_Data/expanded-data/new-cats/LRG/ra_LRG-TOTAL-v2-dr9.npz')
ra_LRG = data_raLRG['raLRG']

data_decLRG = np.load('/Users/mtownsend/Documents/LRG_Data/expanded-data/new-cats/LRG/dec_LRG-TOTAL-v2-dr9.npz')
dec_LRG = data_decLRG['decLRG']

raLRG = ra_LRG[np.where((ra_LRG >= 1.) & (ra_LRG <= 5.) & (dec_LRG >= -11.) & (dec_LRG <= -7.))]
print(len(ra_LRG))
print(len(raLRG))
print('ra done')
print('----')

decLRG = dec_LRG[np.where((ra_LRG >= 1.) & (ra_LRG <= 5.) & (dec_LRG >= -11.) & (dec_LRG <= -7.))]
print(len(dec_LRG))
print(len(decLRG))
print('dec done')
print('----')


# BKG

ra_dat = np.load('/Users/mtownsend/Documents/LRG_Data/expanded-data/new-cats/BKG/ra_BKG-TOTAL-dr9.npz')
ra_BKG = ra_dat['arr_0']

dec_dat = np.load('/Users/mtownsend/Documents/LRG_Data/expanded-data/new-cats/BKG/dec_BKG-TOTAL-dr9.npz')
dec_BKG = dec_dat['arr_0']

maskbits_dat = np.load('/Users/mtownsend/Documents/LRG_Data/expanded-data/new-cats/BKG/maskbits_BKG-TOTAL-dr9.npz')
maskbits_BKG = maskbits_dat['arr_0']


raBKG = ra_BKG[np.where((ra_BKG >= 0.) & (ra_BKG <= 6.) & (dec_BKG >= -12.) & (dec_BKG <= -6.))]
print(len(ra_BKG))
print(len(raBKG))
print('ra done')
print('----')


decBKG = dec_BKG[np.where((ra_BKG >= 0.) & (ra_BKG <= 6.) & (dec_BKG >= -12.) & (dec_BKG <= -6.))]
print(len(dec_BKG))
print(len(decBKG))
print('dec done')

print('----')

maskbitsBKG = maskbits_BKG[np.where((ra_BKG >= 0.) & (ra_BKG <= 6.) & (dec_BKG >= -12.) & (dec_BKG <= -6.))]
print(len(maskbits_BKG))
print(len(maskbitsBKG))
print('maskbits done')
print('----')

maskbits = maskbitsBKG.astype(int)

maskbit_cut = (((maskbits & 2**1)==0) & ((maskbits & 2**12)==0) & ((maskbits & 2**13)==0))



def area_mod(raLRG, decLRG, nside, ra_BKG, dec_BKG, pixarea):

    import healpy as hp
    import numpy as np
    
    lrg_vec = hp.ang2vec(raLRG, decLRG, lonlat=True) # creates 3D position vector for LRGs
#     print('1. ', lrg_vec)
    
    find_pix_inner = hp.query_disc(nside, lrg_vec, radius=np.radians(0.4), nest=True) # finds pixels within 0.4 deg
#     print('2. ', len(find_pix_inner))
    
    find_pix_outer = hp.query_disc(nside, lrg_vec, radius=np.radians(0.5), nest=True) # finds pixels within 0.5 deg
#     print('3. ', len(find_pix_outer))
    
    annulus_pix = np.setdiff1d(find_pix_outer, find_pix_inner) # finds the differences in pix_inner and pix_outer, result is pix in annulus; returns values that are in arr1 but not in arr2
#     print('4. ', len(annulus_pix))
    
    bitmasked_pixels = hp.ang2pix(nside, ra_BKG, dec_BKG, nest=True, lonlat=True) # find pixels for bitmasked sources
#     print('5. ', len(bitmasked_pixels))
    
    bitmasked_intersect = np.intersect1d(annulus_pix, bitmasked_pixels) # find which pixels are in annulus
#     print('6. ', len(bitmasked_intersect))
    
    percent_excluded = ((pixarea * len(bitmasked_intersect)) / (pixarea * len(annulus_pix))) # what background area should be muliplied by to find better area approximation
#     print('7. ', percent_excluded)
    
#     print()
    return percent_excluded, annulus_pix, bitmasked_pixels, bitmasked_intersect
    
    


import healpy as hp

nside = 1024*2
pixarea = hp.nside2pixarea(nside, degrees=True)
print(pixarea)

# ra = raLRG[0:10]
# dec = decLRG[0:10]

percent_excluded = []
annulus_pix = []
bitmasked_pixels = []
bitmasked_intersect = []
for i in range(len(raLRG)):
    temp1, temp2, temp3, temp4 = area_mod(raLRG[i], decLRG[i], nside, raBKG[maskbit_cut], decBKG[maskbit_cut], pixarea)
    percent_excluded.append(temp1)
    annulus_pix.append(temp2)
    bitmasked_pixels.append(temp3)
    bitmasked_intersect.append(temp4)
#     print("finished ", i)
    
    
    
np.savez('/Users/mtownsend/Documents/LRG_Data/percent_excluded.npz', percent_excluded=percent_excluded)
np.savez('/Users/mtownsend/Documents/LRG_Data/annulus_pix.npz', annulus_pix=annulus_pix)
np.savez('/Users/mtownsend/Documents/LRG_Data/bitmasked_pixels.npz', bitmasked_pixels=bitmasked_pixels)
np.savez('/Users/mtownsend/Documents/LRG_Data/bitmasked_intersect.npz', bitmasked_intersect=bitmasked_intersect)

print('finished')



