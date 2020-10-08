def sigSats_usingSumsat(sumsat, percentile):

	# A function to calculate the number of LRGs with satellites above some percentile
    
    # sumsat is an array
    # percentile is the value of distribution at x percentile

    sats = []
    nosats = []
    for i in range(len(sumsat)):
        if (sumsat[i] > percentile):
            sats.append(i)
        else:
            nosats.append(i)
            
    return(sats, nosats)