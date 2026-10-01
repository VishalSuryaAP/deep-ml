def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    if len(samples)==0:
        return []
    count = {}
    for i in samples:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    count = dict(sorted(count.items(),key = lambda item: item[0]))

    result = []
    for key,value in count.items():
        result.append((key,value/len(samples)))
    
    return result
    

