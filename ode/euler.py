# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html

def run(f, t0, x0, t1, h):
    t = t0
    x = x0
    
    a = [[t, x]]
    
    for k in range(0, 1 + int((t1 - t0) / h)):
        t = t0 + k*h
        x = x + h * f(t,x)
        a.append([t, x])
        
    return a
