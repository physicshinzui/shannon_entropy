import numpy as np
import sys
import matplotlib.pyplot as plt

def shannon_entropy(P):
  H = -np.sum(np.log2(P) * P)
  return H

def main():
  #fname = "pca_sngl_ctd.dat"
  fname = "pca_bound_ctd.dat"
  print "Input File Name: ", fname, "\n"
  points = np.loadtxt(fname)

  #Specialised only for two-dimensional space points
  x1 = points[:,0]
  x2 = points[:,1]

  pdf,xedges,yedges = np.histogram2d(x1,x2,bins=50,range=None,normed=False,weights=None)
  print "The No. of Elements (pdf): ", pdf.size
  #pdf[pdf == 0.] = np.nan
  print "Sum of data : ", pdf.sum(), "\n"#Must be the no of confs
  norm_pdf = pdf/pdf.sum()
  print "Some Non-Zero Vals of Normalised PDF   : ", norm_pdf[norm_pdf !=0.0][0:5] 
  print "The no of elements of the non-zero vals: ", len(norm_pdf[norm_pdf !=0.0]), "\n"

  print "Sum of it(Normalised?)   : ", norm_pdf.sum()
  print "Shape of it              : ", norm_pdf.shape, "\n"

  print "Shannon Entropy (H) = ", shannon_entropy(norm_pdf[norm_pdf!=0.0])
  print "  Note: H is expressed as -sum_i [log2(P_i)*P_i]."
  sys.exit()

#***just for a plot of the histogram
  fig = plt.figure(figsize=(7, 3))
  im = plt.imshow(norm_pdf, interpolation='nearest', origin='low')
  plt.colorbar()
  plt.show()
#***
 
if __name__ =="__main__":
  main()
