# Pendulum Experiment

I did a physics lab measuring g with my phone hung on a string. Tested 5 lengths (0.2m, 0.3m, 0.4m, 0.5m, 0.7m) and ran each length 2 times, so 10 csv files in total.

I checked the plots to pick the right axis for each file and put them in `AXIS` inside `analyze.py`. Then used `find_peaks` to get period T.

Line of best fit came out to T^2 = 2.60 * L + 0.39, which gave g = 15.20 m/s^2.

This is way higher than 9.81. The main reason is that my data for L=0.5m and L=0.7m was really messy between the two runs. The phone spun around during the swing, so find_peaks caught fake peaks and messed up the period calculation, pulling down the slope.
