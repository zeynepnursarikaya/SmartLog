import statistics


def detect_anomaly(value: float, values: list[float], threshold: float = 2.0) -> bool:
    if len(values) < 2:
        return False

    mean = statistics.mean(values)
    stdev = statistics.stdev(values)

    if stdev == 0:
        return False

    z_score = abs(value - mean) / stdev
    return z_score > threshold