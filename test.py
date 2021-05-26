import math 
import numpy as np 

upper_bound_freq = 0.45
lower_bound_freq = 0.15

passband_upper = 1.01
passband_lower = 0.99

stopband_upper = 0.06
stopband_lower = 0

passband_range = passband_upper - passband_lower
stopband_range = stopband_upper - stopband_lower

min_frequency = min([passband_range, stopband_range])
cutoff = upper_bound_freq - lower_bound_freq

dB_to_be_filtered = 20* math.log(min_frequency, 10)

windows = {'rectangular': -21, 'barlett': -25, 'hanning': -44, 'hamming': -53, 'blackman': -74}

used_window = ''

for window in windows:
    if windows[window] < dB_to_be_filtered:
        used_window = window
        break

order = int(np.ceil(3.1 / ((cutoff * math.pi) / (2 * math.pi))))

final_filter = []

for n in range(order + 1):
    first_part = math.sin( (cutoff * math.pi)  * (n - (order/2)) )
    second_part = (math.pi * (n - (order/2)))
    if second_part == 0:
        print('Zero division')
        value = 1
    else:
        value = first_part / second_part
    final_filter.append(value)



print(dB_to_be_filtered, used_window)
