import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    def eval_poly(poly,x):
        result = 0
        for i in poly:
            result = result*x + i
        return result

    def deriv_poly(poly):
        n = len(poly)
        if n<= 1:
            return [0]

        deriv = []
        for i in range(n-1):
            power = n-1-i
            deriv.append(power * poly[i])
        return deriv

    g_val = eval_poly(g_coeffs,x)
    h_val = eval_poly(h_coeffs,x)

    if h_val == 0:
        raise ValueError(f"The denominator h(x) evaluates to 0 at x = {x}, making the function undefined.")


    g_val_deriv = deriv_poly(g_coeffs)
    h_val_deriv = deriv_poly(h_coeffs)

    g_val_prime = eval_poly(g_val_deriv,x)
    h_val_prime = eval_poly(h_val_deriv,x)

    numerator = (g_val_prime * h_val) - (h_val_prime * g_val)
    denom = h_val**2
 

    return numerator/denom
    
