def read_isedfit():
    """Read the iSEDfit fitting results."""

    parentfile = '/Users/mtownsend/anaconda/Data/lrg_parent.fits.gz'
    isedfile = '/Users/mtownsend/anaconda/Data/legacysurvey_lrg_ckc14z_kroupa01_charlot_sfhgrid01.fits.gz'
    kcorrfile = '/Users/mtownsend/anaconda/Data/legacysurvey_lrg_ckc14z_kroupa01_charlot_sfhgrid01_kcorr.z0.0.fits.gz'

    print('Reading {}'.format(parentfile))
    parent = Table.read(parentfile)
    print('Reading {}'.format(isedfile))
    ised = Table.read(isedfile)
    print('Reading {}'.format(kcorrfile))
    kcorr = Table.read(kcorrfile)

    snrmin = 3.0
    chi2min = 10

    keep = np.where(
        (ised['CHI2'] < chi2min) *
        (np.sum(ised['MAGGIES'] * np.sqrt(ised['IVARMAGGIES']) > snrmin, axis=1) == 5)
    )[0]
    print('Read {} galaxies with chi2 < {} and S/N > {} in all 5 photometric bands.'.format(
        len(keep), chi2min, snrmin))

    cat = dict()
    cat['weight'] = len(keep) * parent['COUNT'][keep].data / np.sum(parent['COUNT'][keep].data)
    cat['redshift'] = kcorr['Z'][keep].data
    cat['Mstar'] = ised['MSTAR_50'][keep].data
    cat['Mg'] = kcorr['ABSMAG'][keep, 0].data
    cat['Mr'] = kcorr['ABSMAG'][keep, 1].data
    cat['Mz'] = kcorr['ABSMAG'][keep, 2].data
    cat['gr'] = cat['Mg'] - cat['Mr']
    cat['rz'] = cat['Mr'] - cat['Mz']

    with np.errstate(invalid='ignore'):
        cat['grobs'] = -2.5 * np.log10(ised['MAGGIES'][keep, 0].data / ised['MAGGIES'][keep, 1].data)
        cat['rzobs'] = -2.5 * np.log10(ised['MAGGIES'][keep, 1].data / ised['MAGGIES'][keep, 2].data)
        cat['zW1obs'] = -2.5 * np.log10(ised['MAGGIES'][keep, 2].data / ised['MAGGIES'][keep, 3].data)

    # mm = - 2.5 * np.log10(ised['MAGGIES'][keep, 0].data)
    # _ = plt.hist(mm, bins=100)

    kcorr.remove_columns(['Z', 'ISEDFIT_ID', 'MAGGIES', 'IVARMAGGIES'])
    out = hstack([ised[keep], kcorr[keep]])

    return cat, out