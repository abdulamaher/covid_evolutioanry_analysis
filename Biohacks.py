import numpy as np


#number of strains
n = 4


#array of polymorphisms found for each pairwise alignment
seq_polys = [15856,14538,14496,13044,17252,15811]

#number of segregating sites found by doing multiple alignment of all strains
S = 22489



#arrays for later calculations
a1 = np.ones(n-1)
a2 = np.ones(n-1)
j = 0
while j < n-1:
    a1[j] = 1/(j + 1)
    a2[j] = 1/((j + 1)**2)
    j = j + 1


#Tajima's D Calculation
#----------------------
#the average number of polymorphisms betwee all pairwise comparisons
ave_poly = np.sum(seq_polys)/n

#
M = S / np.sum(a1)
#print(M)


d = ave_poly - M
print(d)


N_e = 50118.72336
mu = 0.00008
L = 28831.25
theta = 2*N_e * mu

"""
b1 = (n + 1)/(3*(n-1))
b2 = 2*(n**2 + n + 3)/(9*n*(n-1))
c1 = b1 - (1-np.sum(a1))
c2 = b2-((n+2)/(np.sum(a1)*n)) + (np.sum(a2)/np.sum(a1)**2)
e1 = c1/np.sum(a1)
e2 = c2/(np.sum(a1)**2 + np.sum(a2))



D = (theta * (S/np.sum(a1)))/(np.sqrt(e1*S + e2*S*(S-1)))
"""
D2 = theta/d
print("Tajima's D = {:}".format(D2))