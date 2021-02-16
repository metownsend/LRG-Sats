def readBricks(DECaLS_data):

    # Read in data from DECaLS bricks

    # Only galaxies included
    gal_type_ALL = []
    gal_type_ALL = DECaLS_data.field('TYPE')

    # RA
    ra_ALL = []
    ra_ALL = DECaLS_data.field('RA')

    # Dec
    dec_ALL = []
    dec_ALL = DECaLS_data.field('DEC')

    # flux_g
    gflux_ALL = []
    gflux_ALL = DECaLS_data.field('FLUX_G')

    # flux_r
    rflux_ALL = []
    rflux_ALL = DECaLS_data.field('FLUX_R')

    # flux_z
    zflux_ALL = []
    zflux_ALL = DECaLS_data.field('FLUX_Z')

    # flux_W1
    w1flux_ALL = []
    w1flux_ALL = DECaLS_data.field('flux_w1')

    # flux_W2
    w2flux_ALL = []
    w2flux_ALL = DECaLS_data.field('flux_w2')

    # flux_W3
    w3flux_ALL = []
    w3flux_ALL = DECaLS_data.field('flux_w3')

    # flux_W4
    w4flux_ALL = []
    w4flux_ALL = DECaLS_data.field('flux_w4')

    # nobs == number of images that contribute to the central pixel
    # nobs_g
    gobs_ALL = []
    gobs_ALL = DECaLS_data.field('NOBS_G')

    # nobs_r
    robs_ALL = []
    robs_ALL = DECaLS_data.field('NOBS_R')

    # nobs_z
    zobs_ALL = []
    zobs_ALL = DECaLS_data.field('NOBS_Z')

    # flux errors
    gflux_ivar_ALL = []
    gflux_ivar_ALL = DECaLS_data.field('flux_ivar_g')

    rflux_ivar_ALL = []
    rflux_ivar_ALL = DECaLS_data.field('flux_ivar_r')

    zflux_ivar_ALL = []
    zflux_ivar_ALL = DECaLS_data.field('flux_ivar_z')

    w1flux_ivar_ALL = []
    w1flux_ivar_ALL = DECaLS_data.field('flux_ivar_w1')

    w2flux_ivar_ALL = []
    w2flux_ivar_ALL = DECaLS_data.field('flux_ivar_w2')

    w3flux_ivar_ALL = []
    w3flux_ivar_ALL = DECaLS_data.field('flux_ivar_w3')

    w4flux_ivar_ALL = []
    w4flux_ivar_ALL = DECaLS_data.field('flux_ivar_w4')

    mw_transmission_g_ALL = []
    mw_transmission_g_ALL = DECaLS_data.field('mw_transmission_g')

    mw_transmission_r_ALL = []
    mw_transmission_r_ALL = DECaLS_data.field('mw_transmission_r')

    mw_transmission_z_ALL = []
    mw_transmission_z_ALL = DECaLS_data.field('mw_transmission_z')

    mw_transmission_w1_ALL = []
    mw_transmission_w1_ALL = DECaLS_data.field('mw_transmission_w1')

    mw_transmission_w2_ALL = []
    mw_transmission_w2_ALL = DECaLS_data.field('mw_transmission_w2')

    mw_transmission_w3_ALL = []
    mw_transmission_w3_ALL = DECaLS_data.field('mw_transmission_w3')

    mw_transmission_w4_ALL = []
    mw_transmission_w4_ALL = DECaLS_data.field('mw_transmission_w4')

    # maskbits
    maskbits_ALL = []
    maskbits_ALL = DECaLS_data.field('maskbits')

    print('done reading in DECaLS bricks')

    survey_cut = (((maskbits_ALL & 2**1)==0) & ((maskbits_ALL & 2**11)==0) & ((maskbits_ALL & 2**12)==0) & ((maskbits_ALL & 2**13)==0) & ((maskbits_ALL & 2**5)==0) & ((maskbits_ALL & 2**6)==0) & ((maskbits_ALL & 2**7)==0) & (gobs_ALL >= 2.) & (robs_ALL >= 2.) & (zobs_ALL >= 2.) & (gflux_ALL > 0.) & (rflux_ALL > 0.) & (zflux_ALL > 0.) & ((gal_type_ALL == 'SIMP') | (gal_type_ALL == "DEV") | (gal_type_ALL == "EXP") | (gal_type_ALL == "REX")))
    # survey_cut = (((maskbits_ALL & 2**1)==0) & ((maskbits_ALL & 2**12)==0) & ((maskbits_ALL & 2**13)==0) & ((maskbits_ALL & 2**5)==0) & ((maskbits_ALL & 2**6)==0) & ((maskbits_ALL & 2**7)==0) & (gobs_ALL >= 2.) & (robs_ALL >= 2.) & (zobs_ALL >= 2.) & (gflux_ALL > 0.) & (rflux_ALL > 0.) & (zflux_ALL > 0.) & ((gal_type_ALL == 'SIMP') | (gal_type_ALL == "DEV") | (gal_type_ALL == "EXP") | (gal_type_ALL == "REX")))


    ra_BKG = ra_ALL[survey_cut]
    dec_BKG = dec_ALL[survey_cut]
    gflux_BKG = gflux_ALL[survey_cut]
    rflux_BKG = rflux_ALL[survey_cut]
    zflux_BKG = zflux_ALL[survey_cut]
    w1flux_BKG = w1flux_ALL[survey_cut]
    w2flux_BKG = w2flux_ALL[survey_cut]
    w3flux_BKG = w3flux_ALL[survey_cut]
    w4flux_BKG = w4flux_ALL[survey_cut]
    gflux_ivar_BKG = gflux_ivar_ALL[survey_cut]
    rflux_ivar_BKG = rflux_ivar_ALL[survey_cut]
    zflux_ivar_BKG = zflux_ivar_ALL[survey_cut]
    w1flux_ivar_BKG = w1flux_ivar_ALL[survey_cut]
    w2flux_ivar_BKG = w2flux_ivar_ALL[survey_cut]
    w3flux_ivar_BKG = w3flux_ivar_ALL[survey_cut]
    w4flux_ivar_BKG = w4flux_ivar_ALL[survey_cut]
    mw_transmission_g_BKG = mw_transmission_g_ALL[survey_cut]
    mw_transmission_r_BKG = mw_transmission_r_ALL[survey_cut]
    mw_transmission_z_BKG = mw_transmission_z_ALL[survey_cut]
    mw_transmission_w1_BKG = mw_transmission_w1_ALL[survey_cut]
    mw_transmission_w2_BKG = mw_transmission_w2_ALL[survey_cut]
    mw_transmission_w3_BKG = mw_transmission_w3_ALL[survey_cut]
    mw_transmission_w4_BKG = mw_transmission_w4_ALL[survey_cut]

    return ra_BKG, dec_BKG, gflux_BKG, rflux_BKG, zflux_BKG, w1flux_BKG, w2flux_BKG, w3flux_BKG, w4flux_BKG, gflux_ivar_BKG, rflux_ivar_BKG, zflux_ivar_BKG, w1flux_ivar_BKG, w2flux_ivar_BKG, w3flux_ivar_BKG, w4flux_ivar_BKG, mw_transmission_g_BKG, mw_transmission_r_BKG, mw_transmission_z_BKG, mw_transmission_w1_BKG, mw_transmission_w2_BKG, mw_transmission_w3_BKG, mw_transmission_w4_BKG
