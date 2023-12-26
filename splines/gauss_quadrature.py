
def gauss_3_pontos(m,xi,i,j):
    
    h = H
     
    P1 = 5/9 * m( -0.6**(1/2), xi, i ,j)
    P2 = 8/9 * m( 0, xi, i , j)
    P3 = 5/9 * m( 0.6**(1/2), xi, i , j)
    
    return P1 + P2 + P3


def m_ap(u, xi, i, j):
    
    h = H
    x = X
    
    return p( u*h/2 + x[xi]/2 + x[xi+1]/2 ) * g_derivada(i, u*h/2 + x[xi]/2 + x[xi+1]/2 ) * g_derivada(j, u*h/2 + x[xi]/2 + x[xi+1]/2 )

def m_aq(u, xi, gi, gj):
    
    h = H
    x = X
    
    return q( u*h/2 + x[xi]/2 + x[xi+1]/2 ) * g(gi, u*h/2 + x[xi]/2 + x[xi+1]/2 ) * g(gj, u*h/2 + x[xi]/2 + x[xi+1]/2 )

def m_d(u , xi, bi, j):
    
    h = H
    x = X    
    
    
    return f( u*h/2 + x[xi]/2 + x[xi+1]/2 )*B( bi , u*h/2 + x[xi]/2 + x[xi+1]/2 )
    
    