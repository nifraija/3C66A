######################################################
######################################################
#### In this program we can get the points of the ####
#### plot and make the chage of basis to get the  ####
#### points and make the fit.                     ####
######################################################
######################################################

import matplotlib.pyplot as plt
from pylab import *
from sys import *

def convert_points(filesArray):

    x1,y1,xizq,xder,yarr,yaba=[],[],[],[],[],[]
    name = ' '
    #walk along the array of file paths

    for x in range(0,len(filesArray)):

        try:

            #We now try to
            pathFile = filesArray[x]
            
            name = pathFile
            rfile = open(pathFile+'.dat', 'r')

            if rfile:

                for line in rfile:

                    a, b, c, d, e, f = [float(t) for t in line.split()]
                    x1.append(pow(10,a))
                    y1.append(pow(10,b))

                    if c != 0: 
                        xizq.append(abs(pow(10,a)-pow(10,c)))
                    else:
                        xizq.append(0.0)

                    if d != 0:
                        xder.append(abs(pow(10,a)-pow(10,d)))
                    else:
                        xder.append(0.0)
                        
                    if e != 0:
                        yarr.append(abs(pow(10,b)-pow(10,e)))
                    else:
                        yarr.append(0.0)

                    if f != 0:
                        yaba.append(abs(pow(10,b)-pow(10,f)))
                    else:
                        yaba.append(0.0)
                

            final_array = open(name+'_new_base.dat','w')

            for elem in range(0,len(x1)):
                final_array.write(str(x1[elem])+'\t')
                final_array.write(str(y1[elem])+'\t')
                final_array.write(str(xizq[elem])+'\t')
                final_array.write(str(xder[elem])+'\t')
                final_array.write(str(yarr[elem])+'\t')
                final_array.write(str(yaba[elem])+'\t')
                final_array.write('\n')
            final_array.close()
            x1,y1,xizq,xder,yarr,yaba=[],[],[],[],[],[]
        except:
            
            
            print "Error in" + name
            print "Revisa la ruta de tus archivos"


def plotPoints():

     X1,Y1, X1_izq, X1_der, Y1_arr, Y1_aba = loadtxt('/home/antonio/3C66A/Fermi-LAT_darkrun_new_base.dat', unpack = True)
     X2,Y2, X2_izq, X2_der, Y2_arr, Y2_aba = loadtxt('/home/antonio/3C66A/F-GAMMA_new_base.dat', unpack = True)
     X3,Y3, X3_izq, X3_der, Y3_arr, Y3_aba = loadtxt('/home/antonio/3C66A/GASP_new_base.dat', unpack = True)
     X4,Y4, X4_izq, X4_der, Y4_arr, Y4_aba = loadtxt('/home/antonio/3C66A/MDM_Oct10_new_base.dat', unpack = True)
     X5,Y5, X5_izq, X5_der, Y5_arr, Y5_aba = loadtxt('/home/antonio/3C66A/UVOT_Oct05_new_base.dat', unpack = True)
     X6,Y6, X6_izq, X6_der, Y6_arr, Y6_aba = loadtxt('/home/antonio/3C66A/VERITAS_darkrun_new_base.dat', unpack = True)
     X7,Y7, X7_izq, X7_der, Y7_arr, Y7_aba = loadtxt('/home/antonio/3C66A/VERITAS_flare_new_base.dat', unpack = True)
     X8,Y8, X8_izq, X8_der, Y8_arr, Y8_aba = loadtxt('/home/antonio/3C66A/XRT_Oct05_new_base.dat', unpack = True)
     plt.figure('Graficas Errores')
     plt.errorbar(X1,Y1, Y1_arr, Y1_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '1')
     plt.errorbar(X2,Y2, Y2_arr, Y2_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '2')
     plt.errorbar(X3,Y3, Y3_arr, Y3_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '3')
     plt.errorbar(X4,Y4, Y4_arr, Y4_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '4')
     plt.errorbar(X5,Y5, Y5_arr, Y5_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '5')
     plt.errorbar(X6,Y6, Y6_arr, Y6_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '6')
     plt.errorbar(X7,Y7, Y7_arr, Y7_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '7')
     plt.errorbar(X8,Y8, Y8_arr, Y8_aba, linestyle="none", marker="o", color="blue", markersize=4.0, capsize=3.0, label = '8')

     a=plt.gca()
     a.set_yscale('log')
     a.set_xscale('log')
     plt.show()



#filesArray = ['Fermi-LAT_darkrun', 'Fermi-LAT_flare.dat', 'F-GAMMA', 'GASP', 'MDM_Oct10', 'UVOT_Oct05', 'VERITAS_darkrun',
#              'VERITAS_flare', 'XRT_Oct05']


filesArray = ['Fermi-LAT_darkrun',  'F-GAMMA', 'GASP', 'MDM_Oct10', 'UVOT_Oct05', 'VERITAS_darkrun',
              'VERITAS_flare', 'XRT_Oct05']

convert_points(filesArray)
plotPoints()
