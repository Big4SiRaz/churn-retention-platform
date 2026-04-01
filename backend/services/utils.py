def get_percentile_bucket(value, thresholds):
    """
    Returns percentile approx (0–1 scale)
    """
    if value == 0: 
        return 0.0
    
    ''''
    Above has been done since 0.2 percentile gives 0 - meaninig many completely inactive users which is ok but 1st bucket
    then becomes completely meaningless & hence we start with 0.4 bucket and suppress 0.2 ones
    '''

    if value < thresholds[1]:
        return 0.4
    elif value < thresholds[2]:
        return 0.6
    elif value < thresholds[3]:
        return 0.8
    else:
        return 1.0