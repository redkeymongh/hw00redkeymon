# redkeymon/differential/discrete.py

def diff(t: list, x: list) -> list:
    """
    Computes the discrete derivative v(t) of a time series x(t).
    Formula:
        v(t_k) = (x(t_k) - x(t_{k-1})) / (t_k - t_{k-1})
    """
    # Check for equality of lengths[cite: 1]
    if len(t) != len(x):
        raise ValueError("Inputs 't' and 'x' must have equal lengths.")
    if len(t) < 2:
        raise ValueError("Inputs must contain at least two data points to compute derivative.")

    v = [0.0]  # Initial condition/boundary value for v(t_0)
    
    for k in range(1, len(t)):
        dt = t[k] - t[k-1]
        if dt == 0:
            raise ZeroDivisionError(f"Duplicate consecutive time value at index {k}.")
        dx = x[k] - x[k-1]
        v.append(dx / dt)
        
    return v
