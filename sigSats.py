def sigSats(Nsat, percentile):
    
    # A function to calculate the number of LRGs with satellites above some percentile
    
    # sumsat is an array
    # percentile is the value of distribution at x percentile

    sumsat = []
    # Sum up number of satellite galaxies for every LRG
    for i in range(len(Nsat)):
        sumsat.append(np.sum(Nsat[i]))

    sats = []
    nosats = []
    for i in range(len(sumsat)):
        if (sumsat[i] > percentile):
            sats.append(i)
        else:
            nosats.append(i)

    return (sumsat, sats, nosats)