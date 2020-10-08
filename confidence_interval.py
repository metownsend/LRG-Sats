def confidence_interval(data):

    from scipy import stats

    mean = np.mean(data)
    N = len(data)
    SE = np.std(data)

    # confidence interval = mean +/- SE for 68% confidence
    CI_lower = mean - SE
    CI_upper = mean + SE

    return(CI_lower, CI_upper)