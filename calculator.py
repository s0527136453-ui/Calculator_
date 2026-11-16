def add(a,b):
    return a+b

def divide(a, b):
    """מחלק a ב-b. זורק ValueError על חלוקה באפס."""
    if b == 0:
        raise ValueError("מחלק אפס אינו חוקי")
    return a / b
