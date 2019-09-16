def readData(SpecObj_data, SDSS_data, DECaLS_data):
    import numpy as np
    from pythonds.basic.stack import Stack

    # Read in data from SDSS file

    # Redshift of galaxies according to sdss
    z = []
    z = SDSS_data.field('Z')

    # Unique ID for sources in SDSS
    specobjid = []
    specobjid = SDSS_data.field('SPECOBJID')

    # Class of object
    gal_class = []
    gal_class = SDSS_data.field('CLASS')

    # What survey the data is from
    survey = []
    survey = SDSS_data.field('SURVEY')

    # SPECPRIMARY; set to 1 for primary observation of object, 0 otherwise
    spec = []
    spec = SDSS_data.field('SPECPRIMARY')

    # Bitmask of spectroscopic warning values; need set to 0
    zwarn_noqso = []
    zwarn_noqso = SDSS_data.field('ZWARNING_NOQSO')

    # Spectroscopic classification for certain redshift?
    class_noqso = []
    class_noqso = SDSS_data.field('CLASS_NOQSO')

    # Array for LRG targets
    targets = []
    targets = SDSS_data.field('BOSS_TARGET1')

    # Array for tile number (cut for LOWZ LRGs is tile >= 10324)
    tile = []
    tile = SDSS_data.field('TILE')

    # Array for chunk number (cut for CMASS is chunk != 'boss1' or 'boss2'
    chunk = []
    chunk = SDSS_data.field('CHUNK')

    print('done reading in SDSS')

    # ----------------------------------------------------------------------

    # Section of code to find LRG targets

    def divideBy2(decNumber):

        # from pythonds.basic.stack import Stack
        # import numpy as np

        np.vectorize(decNumber)
        remstack = Stack()

        if decNumber == 0: return "0"

        while decNumber > 0:
            rem = decNumber % 2
            remstack.push(rem)
            decNumber = decNumber // 2

        binString = ""
        while not remstack.isEmpty():
            binString = binString + str(remstack.pop())

        return binString

    # Function to find LRG targets

    divideBy2Vec = np.vectorize(divideBy2)


    a = divideBy2Vec(targets)  # gives binary in string form

    print(a)

    b = []

    for i in range(len(a)):
        b.append(list((a[i])))
        b[i].reverse()


    lrg = []

    # Finds flags for BOSS LOWZ and CMASS sample
    for i in range(len(b)):
        try:
            if (b[i][0] == '1') or (b[i][1] == '1'):
                lrg.append(int(1))
            else:
                lrg.append(int(0))
        except IndexError:
            pass
            lrg.append(int(0))

    lrg = np.array(lrg)

    print('done finding LRG flags')

    # ----------------------------------------------------------------------

    # Read in data from SDSS row matched DECaLS file

    # Object ID from survey file; value -1 for non-matches
    objid_MATCHED = []
    objid_MATCHED = SpecObj_data.field('OBJID')

    # Add brickid
    brickid_MATCHED = []
    brickid_MATCHED = SpecObj_data.field('BRICKID')

    # Add brickname
    brickname_MATCHED = []
    brickname_MATCHED = SpecObj_data.field('BRICKNAME')

    # Only galaxies included
    gal_type_MATCHED = []
    gal_type_MATCHED = SpecObj_data.field('TYPE')

    # RA
    ra_MATCHED = []
    ra_MATCHED = SpecObj_data.field('RA')

    # Dec
    dec_MATCHED = []
    dec_MATCHED = SpecObj_data.field('DEC')

    # flux_g
    gflux_MATCHED = []
    gflux_MATCHED = SpecObj_data.field('FLUX_G')

    # flux_r
    rflux_MATCHED = []
    rflux_MATCHED = SpecObj_data.field('FLUX_R')

    # flux_z
    zflux_MATCHED = []
    zflux_MATCHED = SpecObj_data.field('FLUX_Z')

    # nobs == number of images that contribute to the central pixel
    # nobs_g
    gobs_MATCHED = []
    gobs_MATCHED = SpecObj_data.field('NOBS_G')

    # nobs_r
    robs_MATCHED = []
    robs_MATCHED = SpecObj_data.field('NOBS_R')

    # nobs_z
    zobs_MATCHED = []
    zobs_MATCHED = SpecObj_data.field('NOBS_Z')

    print('done reading in DECaLS-SDSS matched file')

    # ----------------------------------------------------------------------

    # Create a unique identifier by combinding BRICKID and OBJID

    id_MATCHED = []

    for i in range(len(objid_MATCHED)):
        if (objid_MATCHED[i] == -1):
            id_MATCHED.append(-1)
        else:
            temp1 = str(brickid_MATCHED[i]) + str(objid_MATCHED[i])
            id_MATCHED.append(temp1)

    id_MATCHED = [int(i) for i in id_MATCHED]
    id_MATCHED = np.array(id_MATCHED)


    print('done creating unique IDs for matched file')
    # ----------------------------------------------------------------------

    # Select LRGs from SpecObj file (with other cuts)

    LRG_only = ((gobs_MATCHED >= 2.) & (robs_MATCHED >= 2.) & (zobs_MATCHED >= 2.) & (gflux_MATCHED > 0.) & (rflux_MATCHED > 0.) & (zflux_MATCHED > 0.) & (objid_MATCHED != -1) & (lrg == 1) & ((gal_type_MATCHED == 'SIMP') | (gal_type_MATCHED == "DEV") | (gal_type_MATCHED == "EXP") | (gal_type_MATCHED == "REX")) & (ra_MATCHED >= 241) & (ra_MATCHED <= 246) & (dec_MATCHED >= 6.5) & (dec_MATCHED <= 11.5) & (gal_class == 'GALAXY') & (spec == 1) & (zwarn_noqso == 0) & (class_noqso == 'GALAXY') & ((survey == 'sdss') | (survey == 'boss')))

    z_LRG = z[LRG_only]
    ra_LRG = ra_MATCHED[LRG_only]
    dec_LRG = dec_MATCHED[LRG_only]
    gflux_LRG = gflux_MATCHED[LRG_only]
    rflux_LRG = rflux_MATCHED[LRG_only]
    zflux_LRG = zflux_MATCHED[LRG_only]
    id_LRG = id_MATCHED[LRG_only]
    specobjid_LRG = specobjid[LRG_only]


    print('done making LRG only cut')
    # ----------------------------------------------------------------------


    # Read in data from DECaLS bricks

    # Object ID from survey file
    objid_ALL = []
    objid_ALL = DECaLS_data.field('OBJID')
    # print(len(objid_ALL))

    # Add brickid
    brickid_ALL = []
    brickid_ALL = DECaLS_data.field('BRICKID')

    # Add brickname
    brickname_ALL = []
    brickname_ALL = DECaLS_data.field('BRICKNAME')

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

    print('done reading in DECaLS bricks')

    # ----------------------------------------------------------------------

    # Create a unique identifier by combinding BRICKID and OBJID

    id_ALL = []

    for i in range(len(objid_ALL)):
        temp2 = str(brickid_ALL[i]) + str(objid_ALL[i])
        id_ALL.append(temp2)

    id_ALL = [int(i) for i in id_ALL]
    id_ALL = np.array(id_ALL)

    print('length of id_ALL: ', len(id_ALL))
    print('done creating unique IDs for brick file')

    # ----------------------------------------------------------------------

    # Identifies LRGs in survey brick

    idcut = []

    # This creates a list that is the length of id_ALL that matches LRGs from the DECaLS/SDSS file to the DECaLS file
    # For use in narrowing down DECaLS-only file (ie 'ALL')
    # idcut = 1 if it is an LRG; idcut = 0 if it is not an LRG
    for i in range(len(id_ALL)):
        if any(id_LRG == id_ALL[i]):
            idcut.append(1)
        else:
            idcut.append(0)

    idcut = np.array(idcut)

    print('done identifying LRGs in survey brick')

    # ----------------------------------------------------------------------

    # Make relevant cuts for survey brick; eliminates LRGs

    survey_cut = ((idcut == 0) & (gobs_ALL >= 2.) & (robs_ALL >= 2.) & (zobs_ALL >= 2.) & (gflux_ALL > 0.) & (rflux_ALL > 0.) & (zflux_ALL > 0.) & ((gal_type_ALL == 'SIMP') | (gal_type_ALL == "DEV") | (gal_type_ALL == "EXP") | (gal_type_ALL == "REX")) & (ra_ALL >= 241) & (ra_ALL <= 246) & (dec_ALL >= 6.5) & (dec_ALL <= 11.5))


    ra_BKG = ra_ALL[survey_cut]
    dec_BKG = dec_ALL[survey_cut]
    gflux_BKG = gflux_ALL[survey_cut]
    rflux_BKG = rflux_ALL[survey_cut]
    zflux_BKG = zflux_ALL[survey_cut]

    print(len(ra_BKG))
    print('done making survey cuts')

    return id_LRG, specobjid_LRG, ra_LRG, dec_LRG, ra_BKG, dec_BKG, z_LRG, gflux_LRG, rflux_LRG, zflux_LRG, gflux_BKG, rflux_BKG, zflux_BKG









