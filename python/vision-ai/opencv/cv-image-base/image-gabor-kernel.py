import cv2
import matplotlib.pyplot as plt
import math
import numpy as np

import getopt
import sys

def func_usage():
    print(sys.argv)
    # help(np.complex128)
    help(cv2.getGaborKernel)
    
def usage():
    print("""
        Usage:sys.args[0] [option]
        -h or --help
        -v or --version
        -g or --group: garbor kernel group""")
    func_usage()

def unit_img_display(title, images, num_cols=5):
    num      = len(images)
    num_rows = math.ceil(num/num_cols)
    fig = plt.figure(figsize = (num_cols*5,num_rows*5))
    fig.suptitle(title)
    for i in range(num):
        ax=fig.add_subplot(num_rows, num_cols, i + 1)
        ax.imshow(images[i], cmap ='gray')
    plt.show()

# fourier transform
def unit_img_fft(img):
    f = np.fft.fft2(img)
    # print(f.shape,f.size,f.dtype)
    fshift = np.fft.fftshift(f).astype(np.float32)
    # fshift=fshift.real
    
    # calculate the magnitude image
    fshift=np.sqrt(np.power(fshift.imag,2)+np.power(fshift.real,2))
    # print(fshift.shape,fshift.size,fshift.dtype)
    
    # maximum and minimum normalization
    fshift=(fshift-np.min(fshift))/(np.max(fshift)-np.min(fshift))
    return fshift

def garbor_deviation():
    # Gaussian functions with different standard deviations
    wh = 128
    kernel1 = cv2.getGaborKernel((wh, wh),  5, 0, 5, 0.5, 0, cv2.CV_32F)
    kernel2 = cv2.getGaborKernel((wh, wh), 10, 0, 5, 0.5, 0, cv2.CV_32F)
    kernel3 = cv2.getGaborKernel((wh, wh), 20, 0, 5, 0.5, 0, cv2.CV_32F)
    kernel4 = cv2.getGaborKernel((wh, wh), 40, 0, 5, 0.5, 0, cv2.CV_32F)
    images  = [kernel1, kernel2, kernel3, kernel4,
               unit_img_fft(kernel1), unit_img_fft(kernel2), unit_img_fft(kernel3), unit_img_fft(kernel4)]
    title   = "Gaussian functions with different standard deviations"
    unit_img_display(title, images, num_cols=4)

def garbor_cosine_degree():
    # Gaussian functions with different cosine degrees
    wh = 128
    kernel1 = cv2.getGaborKernel((wh, wh), 10, np.degrees(0),  5, 0.5, 0, cv2.CV_32F)
    kernel2 = cv2.getGaborKernel((wh, wh), 10, np.degrees(30), 5, 0.5, 0, cv2.CV_32F)
    kernel3 = cv2.getGaborKernel((wh, wh), 10, np.degrees(60), 5, 0.5, 0, cv2.CV_32F)
    kernel4 = cv2.getGaborKernel((wh, wh), 10, np.degrees(90), 5, 0.5, 0, cv2.CV_32F)
    images = [kernel1, kernel2, kernel3, kernel4,
              unit_img_fft(kernel1), unit_img_fft(kernel2), unit_img_fft(kernel3), unit_img_fft(kernel4)]
    title   = "Gaussian functions with different cosine degrees"
    unit_img_display(title, images, num_cols=4)


def garbor_cosine_wavelength():
    # Gaussian functions with different cosine wavelength
    wh = 128
    kernel1 = cv2.getGaborKernel((wh, wh), 10, 0,  5, 0.5, 0, cv2.CV_32F)
    kernel2 = cv2.getGaborKernel((wh, wh), 10, 0, 10, 0.5, 0, cv2.CV_32F)
    kernel3 = cv2.getGaborKernel((wh, wh), 10, 0, 15, 0.5, 0, cv2.CV_32F)
    kernel4 = cv2.getGaborKernel((wh, wh), 10, 0, 20, 0.5, 0, cv2.CV_32F)
    images = [kernel1,kernel2,kernel3,kernel4, unit_img_fft(kernel1),
              unit_img_fft(kernel2), unit_img_fft(kernel3), unit_img_fft(kernel4)]
    title   = "Gaussian functions with different cosine wavelength"
    unit_img_display(title, images, num_cols=4)

def garbor_cosine_phase_shift():
    # Gaussian functions with different cosine-phase-shift
    wh = 128
    kernel1 = cv2.getGaborKernel((wh, wh), 10, 0, 20, 1,  0, cv2.CV_32F)
    kernel2 = cv2.getGaborKernel((wh, wh), 10, 0, 20, 1, 20, cv2.CV_32F)
    kernel3 = cv2.getGaborKernel((wh, wh), 10, 0, 20, 1, 40, cv2.CV_32F)
    kernel4 = cv2.getGaborKernel((wh, wh), 10, 0, 20, 1, 60, cv2.CV_32F)
    images = [kernel1,kernel2,kernel3,kernel4, unit_img_fft(kernel1),
              unit_img_fft(kernel2), unit_img_fft(kernel3), unit_img_fft(kernel4)]
    title   = "Gaussian functions with different cosine-phase-shift"
    unit_img_display(title, images, num_cols=4)

def garbor_wh_ratio():
    # Gaussian functions with different width-height ratio
    wh = 128
    kernel1 = cv2.getGaborKernel((wh, wh), 10, 0, 5, 0.25, 0, cv2.CV_32F)
    kernel2 = cv2.getGaborKernel((wh, wh), 10, 0, 5, 0.50, 0, cv2.CV_32F)
    kernel3 = cv2.getGaborKernel((wh, wh), 10, 0, 5, 2.00, 0, cv2.CV_32F)
    kernel4 = cv2.getGaborKernel((wh, wh), 10, 0, 5, 4.00, 0, cv2.CV_32F)
    images = [kernel1,kernel2,kernel3,kernel4, unit_img_fft(kernel1),
              unit_img_fft(kernel2), unit_img_fft(kernel3), unit_img_fft(kernel4)]
    title   = "Gaussian functions with different width-height ratio"
    unit_img_display(title, images, num_cols=4)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage()
        sys.exit()
 
    try:
        opts, args = getopt.getopt(sys.argv[1:], '-h-g-v',['help','group','version'])
    except getopt.GetoptError:
        usage()
        sys.exit()

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
            sys.exit()
        elif cmd in ("-v", "--version"):
            print("%s version 1.0" % sys.argv[0])
        elif cmd in ("-g", "--group"):
            garbor_deviation()
            garbor_cosine_degree()
            garbor_cosine_wavelength()
            garbor_cosine_phase_shift()
            garbor_wh_ratio();