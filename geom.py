def getLine4pp(p1,p2):
    '''
    计算经过p1,p2的直线，直线方程 ax+by+c=0，返回 a,b,c
    Parameters
    ----------
    p1 : (x1,y1) 点 1
    p2 : (x2,y2) 点 2
    Returns
    -------
    a,b,c: 直线方程的3个参数
    '''
    x1,y1 = p1
    x2,y2 = p2
    if x1==x2 and y1==y2:
        return None
    else:
        return y1-y2,x2-x1,x1*y2-x2*y1
    
def getLine4kp(k,p):
    '''
    计算经过p的斜率为k的直线，直线方程 ax+by+c=0，返回 a,b,c
    Parameters
    ----------
    k : 斜率
    p : (x0,y0) 点 
    Returns
    -------
    a,b,c: 直线方程的3个参数
    '''
    x0,y0 = p
    return k,-1,y0-k*x0

def getPoint4ll(l1,l2):
    '''
    计算l1,l2交点
    Parameters
    ----------
    l1: (a1,b1,c1) 直线1
    l2: (a2,b2,c2) 直线2
    
    Returns
    -------
    x,y: 点
    '''    
    a1,b1,c1 = l1
    a2,b2,c2 = l2
    if a1*b2 == a2*b1:
        return None
    else:
        return (b1*c2-b2*c1)/(a1*b2-a2*b1), (a1*c2-a2*c1)/(b1*a2-b2*a1)
    
def getPoint4prp(p,o):
    '''
    返回p关于o的中心对称点
    
    Parameters
    ----------
    p: (x1,y1) 点
    o: (x0,y0) 对称中心
    
    Returns
    -------
    x,y: 点
    '''   
    x1,y1 = p
    x0,y0 = o
    return 2*x0-x1,2*y0-y1

def getPoint4prl(p,l):
    '''
    返回p关于直线l的对称点
    
    Parameters
    ----------
    p: (x1,y1) 点
    l: (a,b,c) 对称直线
    
    Returns
    -------
    x,y: 点
    '''   
    x1,y1 = p
    a,b,c = l
    if a == 0:
        return getPoint4prp(p,(x1,-c/b))
    elif b == 0:
        return getPoint4prp(p,(-c/a,y1))
    else:
        k = b/a
        lp = getLine4kp(k,p)
        o = getPoint4ll(l,lp)
        return getPoint4prp(p,o)
     
def getPoint4lxe(l,e):
    from math import sqrt
    '''
    返回直线与椭圆的交点
    
    Parameters
    ----------
    l: (a,b,c) 直线方程 ax+by+c=0
    e: (a,b) 椭圆方程 x^2/a^2+y^2/b^2=1 
    
    Returns
    -------
    [(x,y)]: 点列表
    ''' 
    la,lb,lc = l
    ea,eb = e
    if la == 0:
        y = -lc/lb
        if abs(y)<eb:
            x2 = ea**2 * (1-y**2/eb**2)
            return [(-sqrt(x2),y),(sqrt(x2),y)]
        elif abs(y)==eb:
            return [(0,y)]
        else:
            return None
    elif lb == 0:
        x = -lc/la
        if abs(x)<ea:
            y2 = eb**2 * (1-x**2/ea**2)
            return [(x,-sqrt(y2)),(x,sqrt(y2))]
        elif abs(x)==ea:
            return [(x,0)]
        else:
            return None
    else:
        k = -la/lb
        m = -lc/lb
        xa = eb**2+ea**2*k**2
        xb = 2*ea**2*k*m
        xc = ea**2*(m**2-eb**2)
        if xb**2 < 4*xa*xc:
            return None
        elif xb**2 == 4*xa*xc:
            x = -xb/2/xa
            y = k*x+m
            return [(x,y)]
        else:
            x1 = (-xb+sqrt(xb**2 - 4*xa*xc))/2/xa
            x2 = (-xb-sqrt(xb**2 - 4*xa*xc))/2/xa
            y1 = k*x1+m
            y2 = k*x2+m
            return [(x1,y1),(x2,y2)]

def getPointDist(p1,p2):
    from math import sqrt
    '''
    计算点p1,p2距离
    Parameters
    ----------
    p1: (x1,y1) 点1
    p2: (x2,y2) 点2
    Returns
    -------
    距离
    '''
    x1,y1 = p1
    x2,y2 = p2
    return sqrt((x1-x2)**2+(y1-y2)**2)
