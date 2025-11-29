# func.py

def even_odd(num):
    """Return a list describing even/odd numbers from 0 to num-1."""
    result = []
    for n in range(num):
        if n % 2 == 0:
            result.append(f"{n} is even")
        else:
            result.append(f"{n} is odd")
    return result
