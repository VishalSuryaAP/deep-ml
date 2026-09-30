import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    data = np.array(data)
    mean = np.mean(data)
    median = np.median(data)
    vals, counts = np.unique(data, return_counts=True)
    mode = vals[np.argmax(counts)]
    variance = np.var(data)
    std_dev = np.std(data)
    q1, q2, q3 = np.percentile(data, [25, 50, 75])
    IQR = q3-q1
    return  {"mean":mean,
              "median":median,
              "mode":mode,
              "variance":variance,
              "standard_deviation":std_dev,
              "25th_percentile":q1,
              "50th_percentile":q2,
              "75th_percentile":q3,
              "interquartile_range":IQR}

