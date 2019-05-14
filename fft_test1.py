import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np

Fs = 150.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,1,Ts) # time vector

ff = 5;   # frequency of the signal



y = np.cos(2*np.pi*ff*t)




modulation = np.cos(((3*np.pi)/2*ff*t)+12)

y+=modulation

n = len(y) # length of the signal
k = np.arange(n)


T = n/Fs


frq = k/T # two sides frequency range


frq = frq[range(int(n/2))] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]


##########################################
#Reverse fft normalization and noise red.#
##########################################
NM = np.fft.fft(modulation)/n
NM = NM[range(int(n/2))]


#print("pre-ifft y-val:", y)
#print("")
noisefixed = np.fft.ifft(Y-NM)
nt = t[range(int(n/2))]
#print("post-ifft y-val", y)

#########
#End seg#
#########


if __name__ == '__main__':
  print(len(y))
  print(len(t))


  fig, ax = plt.subplots(5, 1)


  ax[1].plot(t,y)
  #ax[1].set_xlabel('Time')
  #ax[1].set_ylabel('Modulated Amplitude')

  ax[2].plot(frq,abs(Y), 'r') # plotting the spectrum
  #ax[2].set_xlabel('Modulated Freq (Hz)')
  #ax[2].set_ylabel('Modulated |Y(freq)|')

  ax[3].plot(frq, abs(Y-NM), 'r')
  #ax[3].set_xlabel('Freq (Hz)')
  #ax[3].set_ylabel('|Y(freq)|')


  ax[4].plot(nt, (noisefixed*200))
  #ax[4].set_xlabel('Time')
  #ax[4].set_ylabel('Amplitude')

  ax[0].plot(t,(np.cos(2*np.pi*ff*t)))
  #ax[0].set_xlabel('Original Time')
  #ax[0].set_ylabel('Original Amplitude')

  plot_url = py.plot_mpl(fig, filename='mpl-basic-fft')
