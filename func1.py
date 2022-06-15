# noqa: 

import numpy as np
from scipy.stats import lognorm
from scipy.optimize import curve_fit


def func_fit(surfaceV, a, b):

    return a * np.sqrt(surfaceV) + b * surfaceV


def FloodParam(ssh, nt, loc, beta1_1_c, beta1_2_c, beta2_1_c, beta2_2_c, beta1_1_w,
               beta1_2_w, beta2_1_w, beta2_2_w, alpha_c, beta_c, alpha_w, beta_w):
    mu_c = beta1_1_c * ssh + beta1_2_c
    sigma_c = abs(np.sqrt(beta2_1_c*ssh + beta2_2_c))
    mu2_c = np.log(mu_c/np.sqrt(1+sigma_c**2/mu_c**2))
    vari = np.log(1+sigma_c**2/mu_c**2)
    sigma2_c = np.sqrt(vari)

    mu_w = beta1_1_w*ssh + beta1_2_w
    sigma_w = abs(np.sqrt(beta2_1_w*ssh + beta2_2_w))
    mu2_w = np.log(mu_w/np.sqrt(1+sigma_w**2/mu_w**2))
    vari = np.log(1+sigma_w**2/mu_w**2)

    sigma2_w = np.sqrt(vari)

    surge_duration_c = lognorm.rvs(s=sigma2_c, scale=np.exp(mu2_c))
    surge_duration_w = lognorm.rvs(s=sigma2_w, scale=np.exp(mu2_w))

    waitingtime_c = np.random.exponential(lambda_c)
    waitingtime_w = np.random.exponential(lambda_w)

    riseratio_c = np.random.beta(a=alpha_c, b=beta_c)
    riseratio_w = np.random.beta(a=alpha_w, b=beta_w)

    tau_a_c = waitingtime_c - riseratio_c*surge_duration_c
    tau_b_c = tau_a_c + surge_duration_c
    tau_a_w = waitingtime_w - riseratio_w*surge_duration_w
    tau_b_w = tau_a_w + surge_duration_w

    chi_1_c = loc
    chi_2_c = ssh
    chi_1_w = loc
    chi_2_w = ssh
    omega1_c = 1/(riseratio_c*surge_duration_c)*np.log(ssh/loc)
    omega2_c = -1/(1-riseratio_c)/surge_duration_c*np.log(ssh/loc)
    omega1_w = 1/(riseratio_w*surge_duration_w)*np.log(ssh/loc)
    omega2_w = -1/(1-riseratio_w)/surge_duration_w*np.log(ssh/loc)

    time1_c = np.linspace(tau_a_c, waitingtime_c, nt)
    time2_c = np.linspace(waitingtime_c, tau_b_c, nt)
    time1_w = np.linspace(tau_a_w, waitingtime_w, nt)
    time2_w = np.linspace(waitingtime_w, tau_b_w, nt)

    cpi1_c = chi_1_c*np.exp(omega1_c*(time1_c-tau_a_c))  
    cpi2_c = chi_2_c*np.exp(omega2_c*(time2_c-waitingtime_c))
    cpi1_w = chi_1_w*np.exp(omega1_w*(time1_w-tau_a_w))
    cpi2_w = chi_2_w*np.exp(omega2_w*(time2_w-waitingtime_w))

    return time1_c, time2_c, time1_w, time2_w, cpi1_c, cpi2_c, cpi1_w, cpi2_w

def SurfaceVolFunc(surfaceV,H):
    """
    This function takes the surface volume values calculated using the Surface Volume Processor
    and interpolates the values into a surface volume function.
    """
    
    a1 = 0;  a2 = 2;  b1 = 1;  b2 = 3;     c1 = 2;  c2 = 4;  d1 = 3;  d2 = 5
    e1 = 4;  e2 = 6;  f1 = 5;  f2 = 7;     g1 = 6;  g2 = 8;  h1 = 7;  h2 = 9
    i1 = 8;  i2 = 10; j1 = 9;  j2 = 11;    k1 = 10; k2 = 12; l1 = 11; l2 = 13
    m1 = 12; m2 = 14; n1 = 13; n2 = 15;    o1 = 14; o2 = 16; p1 = 15; p2 = 17
    q1 = 16; q2 = 18; r1 = 17; r2 = 19;    s1 = 18; s2 = 20; t1 = 19; t2 = 21
    
    popt1, pcov1 = curve_fit(func_fit, surfaceV[a1:a2], H[a1:a2])
    popt2, pcov2 = curve_fit(func_fit, surfaceV[b1:b2], H[b1:b2])
    popt3, pcov3 = curve_fit(func_fit, surfaceV[c1:c2], H[c1:c2])
    popt4, pcov4 = curve_fit(func_fit, surfaceV[d1:d2], H[d1:d2])
    popt5, pcov5 = curve_fit(func_fit, surfaceV[e1:e2], H[e1:e2])
    popt6, pcov6 = curve_fit(func_fit, surfaceV[f1:f2], H[f1:f2])
    popt7, pcov7 = curve_fit(func_fit, surfaceV[g1:g2], H[g1:g2])
    popt8, pcov8 = curve_fit(func_fit, surfaceV[h1:h2], H[h1:h2])
    popt9, pcov9 = curve_fit(func_fit, surfaceV[i1:i2], H[i1:i2])
    popt10, pcov10 = curve_fit(func_fit, surfaceV[j1:j2], H[j1:j2])
    popt11, pcov11 = curve_fit(func_fit, surfaceV[k1:k2], H[k1:k2])
    popt12, pcov12 = curve_fit(func_fit, surfaceV[l1:l2], H[l1:l2])
    popt13, pcov13 = curve_fit(func_fit, surfaceV[m1:m2], H[m1:m2])
    popt14, pcov14 = curve_fit(func_fit, surfaceV[n1:n2], H[n1:n2])
    popt15, pcov15 = curve_fit(func_fit, surfaceV[o1:o2], H[o1:o2])
    popt16, pcov16 = curve_fit(func_fit, surfaceV[p1:p2], H[p1:p2])
    popt17, pcov17 = curve_fit(func_fit, surfaceV[q1:q2], H[q1:q2])
    popt18, pcov18 = curve_fit(func_fit, surfaceV[r1:r2], H[r1:r2])
    popt19, pcov19 = curve_fit(func_fit, surfaceV[s1:s2], H[s1:s2])
    popt20, pcov20 = curve_fit(func_fit, surfaceV[t1:t2], H[t1:t2])
            
    return popt1, popt2, popt3, popt4, popt5, popt6, popt7, popt8, popt9, popt10, popt11, popt12, popt13, popt14, popt15, popt16, popt17, popt18, popt19, popt20

def FloodHeight(surfaceV, slope, roughness, SVf1, SVf2, SVf3, SVf4, SVf5, SVf6, SVf7, SVf8, SVf9, SVf10, SVf11, SVf12, SVf13, SVf14, SVf15, SVf16, SVf17, SVf18, SVf19, SVf20, time1_w, time2_w, cpi1_w, cpi2_w, nt, elev, fid, l, ssh, i):
    """
    This function calculates flood heights for a given div without considering flood water redistribution
    """

    sec1_w = time1_w * 60**2; sec2_w = time2_w * 60**2  #time in seconds
    h1_w = cpi1_w;            h2_w = cpi2_w             #surge height
    V_new = 0;                v_new = np.zeros(nt*2)    # v: velocity
    
    a1 = 0;  a2 = 2;  b1 = 1;  b2 = 3;     c1 = 2;  c2 = 4;  d1 = 3;  d2 = 5
    e1 = 4;  e2 = 6;  f1 = 5;  f2 = 7;     g1 = 6;  g2 = 8;  h1 = 7;  h2 = 9
    i1 = 8;  i2 = 10; j1 = 9;  j2 = 11;    k1 = 10; k2 = 12; l1 = 11; l2 = 13
    m1 = 12; m2 = 14; n1 = 13; n2 = 15;    o1 = 14; o2 = 16; p1 = 15; p2 = 17
    q1 = 16; q2 = 18; r1 = 17; r2 = 19;    s1 = 18; s2 = 20; t1 = 19; t2 = 21

    for k in fid: #calculating incoming flood volume for a given division
        ds1 = np.tile(sec1_w[1] - sec1_w[0],(nt,1)).transpose() #delta between times in seconds
        ds2 = np.tile(sec2_w[1] - sec2_w[0],(nt,1)).transpose()
        ds  = np.concatenate((ds1,ds2),axis=1)

        h1_new = h1_w - elev[k] #difference between surge heights and elevations
        h2_new = h2_w - elev[k]
        h_new  = np.concatenate((h1_new,h2_new),axis=0)
        v_new[h_new > 0] = ((l * h_new[h_new > 0]) / (l + (2*h_new[h_new > 0])))**(2./3.)*slope**.5 / roughness #Manning's Equation
        v_new[h_new <= 0] = 0

        V_new = V_new + np.sum(h_new*l*v_new*ds) #volume to plug into surface volume functions to determine flood heights
    
    #determine flood heights based on surface volume function
    fld_h = np.zeros(np.shape(V_new))
    #fld_h = [0]

    fld_h [V_new == 0]= 0
    fld_h [(V_new <= surfaceV[a2])  &  (V_new > 0)] = func_fit(V_new[(V_new <= surfaceV[a2])  &  (V_new > 0)],*SVf1)
    fld_h [(V_new <= surfaceV[b2])  &  (V_new > surfaceV[a2])] = func_fit(V_new[(V_new <= surfaceV[b2])  &  (V_new > surfaceV[a2])],*SVf2)
    fld_h [(V_new <= surfaceV[c2])  &  (V_new > surfaceV[b2])] = func_fit(V_new[(V_new <= surfaceV[c2])  &  (V_new > surfaceV[b2])],*SVf3)
    fld_h [(V_new <= surfaceV[d2])  &  (V_new > surfaceV[c2])] = func_fit(V_new[(V_new <= surfaceV[d2])  &  (V_new > surfaceV[c2])],*SVf4)
    fld_h [(V_new <= surfaceV[e2])  &  (V_new > surfaceV[d2])] = func_fit(V_new[(V_new <= surfaceV[e2])  &  (V_new > surfaceV[d2])],*SVf5)
    fld_h [(V_new <= surfaceV[f2])  &  (V_new > surfaceV[e2])] = func_fit(V_new[(V_new <= surfaceV[f2])  &  (V_new > surfaceV[e2])],*SVf6)
    fld_h [(V_new <= surfaceV[g2])  &  (V_new > surfaceV[f2])] = func_fit(V_new[(V_new <= surfaceV[g2])  &  (V_new > surfaceV[f2])],*SVf7)
    fld_h [(V_new <= surfaceV[h2])  &  (V_new > surfaceV[f2])] = func_fit(V_new[(V_new <= surfaceV[h2])  &  (V_new > surfaceV[f2])],*SVf8)
    fld_h [(V_new <= surfaceV[i2])  &  (V_new > surfaceV[h2])] = func_fit(V_new[(V_new <= surfaceV[i2])  &  (V_new > surfaceV[h2])],*SVf9)
    fld_h [(V_new <= surfaceV[j2])  &  (V_new > surfaceV[i2])] = func_fit(V_new[(V_new <= surfaceV[j2])  &  (V_new > surfaceV[i2])],*SVf10)
    fld_h [(V_new <= surfaceV[k2])  &  (V_new > surfaceV[j2])] = func_fit(V_new[(V_new <= surfaceV[k2])  &  (V_new > surfaceV[j2])],*SVf11)
    fld_h [(V_new <= surfaceV[l2])  &  (V_new > surfaceV[k2])] = func_fit(V_new[(V_new <= surfaceV[l2])  &  (V_new > surfaceV[k2])],*SVf12)
    fld_h [(V_new <= surfaceV[m2])  &  (V_new > surfaceV[l2])] = func_fit(V_new[(V_new <= surfaceV[m2])  &  (V_new > surfaceV[l2])],*SVf13)
    fld_h [(V_new <= surfaceV[n2])  &  (V_new > surfaceV[m2])] = func_fit(V_new[(V_new <= surfaceV[n2])  &  (V_new > surfaceV[m2])],*SVf14)
    fld_h [(V_new <= surfaceV[o2])  &  (V_new > surfaceV[n2])] = func_fit(V_new[(V_new <= surfaceV[o2])  &  (V_new > surfaceV[n2])],*SVf15)
    fld_h [(V_new <= surfaceV[p2])  &  (V_new > surfaceV[o2])] = func_fit(V_new[(V_new <= surfaceV[p2])  &  (V_new > surfaceV[o2])],*SVf16)
    fld_h [(V_new <= surfaceV[q2])  &  (V_new > surfaceV[p2])] = func_fit(V_new[(V_new <= surfaceV[q2])  &  (V_new > surfaceV[p2])],*SVf17)
    fld_h [(V_new <= surfaceV[r2])  &  (V_new > surfaceV[q2])] = func_fit(V_new[(V_new <= surfaceV[r2])  &  (V_new > surfaceV[q2])],*SVf18)
    fld_h [(V_new <= surfaceV[s2])  &  (V_new > surfaceV[r2])] = func_fit(V_new[(V_new <= surfaceV[s2])  &  (V_new > surfaceV[r2])],*SVf19)
    fld_h [V_new >= surfaceV[s2]] = func_fit(V_new[V_new > surfaceV[s2]],*SVf20)
    fld_h [fld_h < 0]= 0
    
    return fld_h,V_new #outputs: total volume of water for the division and the flood height for that division

def FloodHeightWall(surfaceV,ParWall,slope,roughness,SVf1,SVf2,SVf3,SVf4,SVf5,SVf6,SVf7,SVf8,SVf9,SVf10,SVf11,SVf12,SVf13,SVf14,SVf15,SVf16,SVf17,SVf18,SVf19,SVf20,time1_w,time2_w,cpi1_w,cpi2_w,nt,elev,fid,l,ssh,i):
    """
    This function calculates flood heights with an altered Manning's Equation to account for the height of the wall.
    """
    
    sec1_w = time1_w * 60**2; sec2_w = time2_w * 60**2
    h1_w = cpi1_w;            h2_w = cpi2_w
    V_new = 0; v_new = np.zeros(nt*2)
    
    a1 = 0;  a2 = 2;  b1 = 1;  b2 = 3;     c1 = 2;  c2 = 4;  d1 = 3;  d2 = 5
    e1 = 4;  e2 = 6;  f1 = 5;  f2 = 7;     g1 = 6;  g2 = 8;  h1 = 7;  h2 = 9
    i1 = 8;  i2 = 10; j1 = 9;  j2 = 11;    k1 = 10; k2 = 12; l1 = 11; l2 = 13
    m1 = 12; m2 = 14; n1 = 13; n2 = 15;    o1 = 14; o2 = 16; p1 = 15; p2 = 17
    q1 = 16; q2 = 18; r1 = 17; r2 = 19;    s1 = 18; s2 = 20; t1 = 19; t2 = 21

    for k in fid:
        if k in ParWall:
            ds1 = np.tile(sec1_w[1] - sec1_w[0],(nt,1)).transpose()
            ds2 = np.tile(sec2_w[1] - sec2_w[0],(nt,1)).transpose()
            ds  = np.concatenate((ds1,ds2),axis=1)

            h1_new = h1_w - elev[k]
            h2_new = h2_w - elev[k]
            h_new  = np.concatenate((h1_new,h2_new),axis=0)
            cwr = 0.611 + 0.075*h_new[h_new > 0]/elev[k]        #Manning's Equation with weir       
            v_new[h_new > 0] = ((l * h_new[h_new > 0]) / (l + (2*h_new[h_new > 0])))**(2./3.)*slope**.5 / roughness * cwr
            v_new[h_new <= 0] = 0
            V_new = V_new + np.sum(h_new*l*v_new*ds)
            
        else:
            ds1 = np.tile(sec1_w[1] - sec1_w[0],(nt,1)).transpose()
            ds2 = np.tile(sec2_w[1] - sec2_w[0],(nt,1)).transpose()
            ds  = np.concatenate((ds1,ds2),axis=1)

            h1_new = h1_w - elev[k]
            h2_new = h2_w - elev[k]
            h_new  = np.concatenate((h1_new,h2_new),axis=0)
            v_new[h_new > 0] = ((l * h_new[h_new > 0]) / (l + (2*h_new[h_new > 0])))**(2./3.)*slope**.5 / roughness
            v_new[h_new <= 0] = 0
            V_new = V_new + np.sum(h_new*l*v_new*ds)
        
    fld_h = np.zeros(np.shape(V_new))
    fld_h [V_new == 0]= 0
    fld_h [(V_new <= surfaceV[a2])  &  (V_new > 0)] = func_fit(V_new[(V_new <= surfaceV[a2])  &  (V_new > 0)],*SVf1)
    fld_h [(V_new <= surfaceV[b2])  &  (V_new > surfaceV[a2])] = func_fit(V_new[(V_new <= surfaceV[b2])  &  (V_new > surfaceV[a2])],*SVf2)
    fld_h [(V_new <= surfaceV[c2])  &  (V_new > surfaceV[b2])] = func_fit(V_new[(V_new <= surfaceV[c2])  &  (V_new > surfaceV[b2])],*SVf3)
    fld_h [(V_new <= surfaceV[d2])  &  (V_new > surfaceV[c2])] = func_fit(V_new[(V_new <= surfaceV[d2])  &  (V_new > surfaceV[c2])],*SVf4)
    fld_h [(V_new <= surfaceV[e2])  &  (V_new > surfaceV[d2])] = func_fit(V_new[(V_new <= surfaceV[e2])  &  (V_new > surfaceV[d2])],*SVf5)
    fld_h [(V_new <= surfaceV[f2])  &  (V_new > surfaceV[e2])] = func_fit(V_new[(V_new <= surfaceV[f2])  &  (V_new > surfaceV[e2])],*SVf6)
    fld_h [(V_new <= surfaceV[g2])  &  (V_new > surfaceV[f2])] = func_fit(V_new[(V_new <= surfaceV[g2])  &  (V_new > surfaceV[f2])],*SVf7)
    fld_h [(V_new <= surfaceV[h2])  &  (V_new > surfaceV[f2])] = func_fit(V_new[(V_new <= surfaceV[h2])  &  (V_new > surfaceV[f2])],*SVf8)
    fld_h [(V_new <= surfaceV[i2])  &  (V_new > surfaceV[h2])] = func_fit(V_new[(V_new <= surfaceV[i2])  &  (V_new > surfaceV[h2])],*SVf9)
    fld_h [(V_new <= surfaceV[j2])  &  (V_new > surfaceV[i2])] = func_fit(V_new[(V_new <= surfaceV[j2])  &  (V_new > surfaceV[i2])],*SVf10)
    fld_h [(V_new <= surfaceV[k2])  &  (V_new > surfaceV[j2])] = func_fit(V_new[(V_new <= surfaceV[k2])  &  (V_new > surfaceV[j2])],*SVf11)
    fld_h [(V_new <= surfaceV[l2])  &  (V_new > surfaceV[k2])] = func_fit(V_new[(V_new <= surfaceV[l2])  &  (V_new > surfaceV[k2])],*SVf12)
    fld_h [(V_new <= surfaceV[m2])  &  (V_new > surfaceV[l2])] = func_fit(V_new[(V_new <= surfaceV[m2])  &  (V_new > surfaceV[l2])],*SVf13)
    fld_h [(V_new <= surfaceV[n2])  &  (V_new > surfaceV[m2])] = func_fit(V_new[(V_new <= surfaceV[n2])  &  (V_new > surfaceV[m2])],*SVf14)
    fld_h [(V_new <= surfaceV[o2])  &  (V_new > surfaceV[n2])] = func_fit(V_new[(V_new <= surfaceV[o2])  &  (V_new > surfaceV[n2])],*SVf15)
    fld_h [(V_new <= surfaceV[p2])  &  (V_new > surfaceV[o2])] = func_fit(V_new[(V_new <= surfaceV[p2])  &  (V_new > surfaceV[o2])],*SVf16)
    fld_h [(V_new <= surfaceV[q2])  &  (V_new > surfaceV[p2])] = func_fit(V_new[(V_new <= surfaceV[q2])  &  (V_new > surfaceV[p2])],*SVf17)
    fld_h [(V_new <= surfaceV[r2])  &  (V_new > surfaceV[q2])] = func_fit(V_new[(V_new <= surfaceV[r2])  &  (V_new > surfaceV[q2])],*SVf18)
    fld_h [(V_new <= surfaceV[s2])  &  (V_new > surfaceV[r2])] = func_fit(V_new[(V_new <= surfaceV[s2])  &  (V_new > surfaceV[r2])],*SVf19)
    fld_h [V_new >= surfaceV[s2]] = func_fit(V_new[V_new > surfaceV[s2]],*SVf20)
    fld_h [fld_h < 0]= 0
             
    return fld_h,V_new

def FloodTravel(surfaceV, ssh,V_new,SVf1,SVf2,SVf3,SVf4,SVf5,SVf6,SVf7,SVf8,SVf9,SVf10,SVf11,SVf12,SVf13,SVf14,SVf15,SVf16,SVf17,SVf18,SVf19,SVf20):
    """
    This function takes the volumes redistributed in FloodTravelSectGroup and calculates the new flood heights for each div based on those volumes.
    """
    
    a1 = 0;  a2 = 2;  b1 = 1;  b2 = 3;     c1 = 2;  c2 = 4;  d1 = 3;  d2 = 5
    e1 = 4;  e2 = 6;  f1 = 5;  f2 = 7;     g1 = 6;  g2 = 8;  h1 = 7;  h2 = 9
    i1 = 8;  i2 = 10; j1 = 9;  j2 = 11;    k1 = 10; k2 = 12; l1 = 11; l2 = 13
    m1 = 12; m2 = 14; n1 = 13; n2 = 15;    o1 = 14; o2 = 16; p1 = 15; p2 = 17
    q1 = 16; q2 = 18; r1 = 17; r2 = 19;    s1 = 18; s2 = 20; t1 = 19; t2 = 21
    
    fld_h = np.zeros(np.shape(V_new))
    fld_h [V_new == 0]= 0
    fld_h [(V_new <= surfaceV[a2]) & (V_new > 0)] = func_fit(V_new[(V_new <= surfaceV[a2])  &  (V_new > 0)],*SVf1)
    fld_h [(V_new <= surfaceV[b2])  &  (V_new > surfaceV[a2])] = func_fit(V_new[(V_new <= surfaceV[b2])  &  (V_new > surfaceV[a2])],*SVf2)
    fld_h [(V_new <= surfaceV[c2])  &  (V_new > surfaceV[b2])] = func_fit(V_new[(V_new <= surfaceV[c2])  &  (V_new > surfaceV[b2])],*SVf3)
    fld_h [(V_new <= surfaceV[d2])  &  (V_new > surfaceV[c2])] = func_fit(V_new[(V_new <= surfaceV[d2])  &  (V_new > surfaceV[c2])],*SVf4)
    fld_h [(V_new <= surfaceV[e2])  &  (V_new > surfaceV[d2])] = func_fit(V_new[(V_new <= surfaceV[e2])  &  (V_new > surfaceV[d2])],*SVf5)
    fld_h [(V_new <= surfaceV[f2])  &  (V_new > surfaceV[e2])] = func_fit(V_new[(V_new <= surfaceV[f2])  &  (V_new > surfaceV[e2])],*SVf6)
    fld_h [(V_new <= surfaceV[g2])  &  (V_new > surfaceV[f2])] = func_fit(V_new[(V_new <= surfaceV[g2])  &  (V_new > surfaceV[f2])],*SVf7)
    fld_h [(V_new <= surfaceV[h2])  &  (V_new > surfaceV[f2])] = func_fit(V_new[(V_new <= surfaceV[h2])  &  (V_new > surfaceV[f2])],*SVf8)
    fld_h [(V_new <= surfaceV[i2])  &  (V_new > surfaceV[h2])] = func_fit(V_new[(V_new <= surfaceV[i2])  &  (V_new > surfaceV[h2])],*SVf9)
    fld_h [(V_new <= surfaceV[j2])  &  (V_new > surfaceV[i2])] = func_fit(V_new[(V_new <= surfaceV[j2])  &  (V_new > surfaceV[i2])],*SVf10)
    fld_h [(V_new <= surfaceV[k2])  &  (V_new > surfaceV[j2])] = func_fit(V_new[(V_new <= surfaceV[k2])  &  (V_new > surfaceV[j2])],*SVf11)
    fld_h [(V_new <= surfaceV[l2])  &  (V_new > surfaceV[k2])] = func_fit(V_new[(V_new <= surfaceV[l2])  &  (V_new > surfaceV[k2])],*SVf12)
    fld_h [(V_new <= surfaceV[m2])  &  (V_new > surfaceV[l2])] = func_fit(V_new[(V_new <= surfaceV[m2])  &  (V_new > surfaceV[l2])],*SVf13)
    fld_h [(V_new <= surfaceV[n2])  &  (V_new > surfaceV[m2])] = func_fit(V_new[(V_new <= surfaceV[n2])  &  (V_new > surfaceV[m2])],*SVf14)
    fld_h [(V_new <= surfaceV[o2])  &  (V_new > surfaceV[n2])] = func_fit(V_new[(V_new <= surfaceV[o2])  &  (V_new > surfaceV[n2])],*SVf15)
    fld_h [(V_new <= surfaceV[p2])  &  (V_new > surfaceV[o2])] = func_fit(V_new[(V_new <= surfaceV[p2])  &  (V_new > surfaceV[o2])],*SVf16)
    fld_h [(V_new <= surfaceV[q2])  &  (V_new > surfaceV[p2])] = func_fit(V_new[(V_new <= surfaceV[q2])  &  (V_new > surfaceV[p2])],*SVf17)
    fld_h [(V_new <= surfaceV[r2])  &  (V_new > surfaceV[q2])] = func_fit(V_new[(V_new <= surfaceV[r2])  &  (V_new > surfaceV[q2])],*SVf18)
    fld_h [(V_new <= surfaceV[s2])  &  (V_new > surfaceV[r2])] = func_fit(V_new[(V_new <= surfaceV[s2])  &  (V_new > surfaceV[r2])],*SVf19)
    fld_h [V_new >= surfaceV[s2]] = func_fit(V_new[V_new > surfaceV[s2]],*SVf20)
    fld_h [fld_h < 0]= 0
    if fld_h > ssh:
        fld_h = ssh
    
    return fld_h

def FloodTravelSectGroup(ssh,sect0,sect1,sect2,sect3,sect_3,sect_2,sect_1,files,V,
                         SVfg1,SVfg2,SVfg3,SVfg4,SVfg5,SVfg6,SVfg7,SVfg8,SVfg9,SVfg10,SVfg11,SVfg12,SVfg13,SVfg14,SVfg15,SVfg16,SVfg17,SVfg18,SVfg19,SVfg20):
    """
    This function propagates the flooding to different divisions within a group and calls FloodTravel to resditribute the water
    """
    V_sect = np.zeros(ndiv18)
    fld_h_sect = np.zeros(ndiv18)
    V_sect_avr = np.zeros(ndiv18)
 
    # ID3~14
    for i in range(12):
        m = int(sect3[i][3])
        for s in sect3[i]:
            s = int(s)
            V_sect[m] = V_sect[m] + V[s]
        V_sect_avr[m] = V_sect[m]/7

    #ID0
    i = 10; 
    for s in sect0:
        s = int(s)
        V_sect[i] = V_sect[i] + V[s]
    V_sect_avr[i] = V_sect[i]/4

    #ID1
    i = 11; 
    for s in sect1:
        s = int(s)
        V_sect[i] = V_sect[i] + V[s]
    V_sect_avr[i] = V_sect[i]/5

    #ID2
    i = 5;
    for s in sect2:
        s = int(s)
        V_sect[i] = V_sect[i] + V[s]
    V_sect_avr[i] = V_sect[i]/6

    #ID15
    i = 7;
    for s in sect_3:
        s = int(s)
        V_sect[i] = V_sect[i] + V[s]
    V_sect_avr[i] = V_sect[i]/6

    #ID16
    i = 2;
    for s in sect_2:
        s = int(s)
        V_sect[i] = V_sect[i] + V[s]
    V_sect_avr[i] = V_sect[i]/5

    #ID17
    i = 6;
    for s in sect_1:
        s = int(s)
        V_sect[i] = V_sect[i] + V[s]
    V_sect_avr[i] = V_sect[i]/4

    for i in range(ndiv18):    
        # redistribute the water
        fld_h_sect[i] = FloodTravel(ssh,V_sect[i],SVfg1[i,:],SVfg2[i,:],SVfg3[i,:],SVfg4[i,:],SVfg5[i,:],SVfg6[i,:],SVfg7[i,:],SVfg8[i,:],SVfg9[i,:],SVfg10[i,:],SVfg11[i,:],SVfg12[i,:],SVfg13[i,:],SVfg14[i,:],SVfg15[i,:],SVfg16[i,:],SVfg17[i,:],SVfg18[i,:],SVfg19[i,:],SVfg20[i,:])

    fld_h_sect[fld_h_sect<0] = 0
    
    return fld_h_sect,V_sect_avr #new flood height and volume for each division
