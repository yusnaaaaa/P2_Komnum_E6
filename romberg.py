import numpy as np


#fungsi derajat 5
def f(x,a1,a2,a3,a4,a5,a6):
    return a1 + a2*x + a3*x**2 + a4*x**3 + a5*x**4 + a6*x**5

c1 = float(input("masukan nilai konstanta pertama: "))
c2 = float(input("masukan nilai konstanta kedua: "))
c3 = float(input("masukan nilai konstanta ketiga: "))
c4 = float(input("masukan nilai konstanta keempat: "))
c5 = float(input("masukan nilai konstanta kelima: "))
c6 = float(input("masukan nilai konstanta keenam: " ))

atas = float(input("masukan nilai dari batas atas"))
bawah = float(input("masukan nilai dari batas bawah"))

#a = batas bawah, b = batas atas, dan N adalah interval
#fungsi integrasi trapezium
def trap(f,a,b,N):
    x0 = a
    xN = b
    h = (b - a)/N  # h = segmen tiap interval
    ss = 0
    for i in range(1,N):
        xi = x0 + i*h
        ss = ss + f(xi,c1,c2,c3,c4,c5,c6)
    I = h/2 * (f(x0,c1,c2,c3,c4,c5,c6) + 2*ss + f(xN,c1,c2,c3,c4,c5,c6)) #hasil integrasi
    return I

#I1,1 setara dengan integrasi trapesium dengan satu interval
I11 = trap(f, 0, 0.8, 1)
#print(I11)

#I2,1 setara dengan integrasi trapesium dengan dua interval
I21 = trap(f, 0, 0.8, 2)
#print(I21)

#I1,2 integrasi romberg dengan satu interval
I12 = (4*I21 - I11)/3
#print(I12)

def romberg(f, a, b, es = 1e-10 , MAXIT = 10, verbose = False):
    I = np.zeros((MAXIT + 2,MAXIT + 1))
    n = 1
    I[1,1] = trap(f, a, b, n)
    iterconv = 0
    for i in range(1, MAXIT + 1):
        n = 2**i
        I[i + 1,1] = trap(f, a, b , n)

        for k in range(2,i + 2):
            j = 2 + i - k
            I[j,k] = (4**(k - 1) * I[j + 1,k -1] - I[j,k - 1]) / (4**(k - 1) - 1)

        ea = abs((I[1,i + 1] - I[2,i]) / I[1, i + 1]) * 100
        if ea <= es:
            iterconv = i
            break
        iterconv = i

    if verbose:
        print(I[1: iterconv + 2, 1: iterconv + 1])
    
    return I[1,iterconv + 1]

print("hasil dari perhitungan integrasi romberg adalah matriks dibawah")
romberg(f, bawah, atas, verbose = True)


