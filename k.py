import numpy as np
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging

# read in lon,lat and precipitation as a float
lats = [ float(line.rstrip('\n')) for line in open('lat.dat') ]
lons = [ float(line.rstrip('\n')) for line in open('lon.dat') ]
rains =[ float(line.rstrip('\n')) for line in open('rain.dat') ]

#print (lats[23],lons[23],rains[23])

#
mn=779334
latt=np.full(mn,0.0)
lont=np.full(mn,0.0)
raint=np.full(mn,0.0)

#
j=1
for i in range(len(lats)):
    if lats[i] >= 23. and lats[i] <= 25. and lons[i] >= 119. and lons[i] <= 122:
        latt[j]=lats[i]
        lont[j]=lons[i]
        raint[j]=rains[i]
        j += 1

print(j)
lat=np.full(j,0.0)
lon=np.full(j,0.0)
rain=np.full(j,0.0)
i=0
while i < j:
    lat[i]=latt[i]
    lon[i]=lont[i]
    rain[i]=raint[i]
    i += 1 

print(len(lat),len(lon),len(rain))

# 
OK = OrdinaryKriging(lon, lat, rain, variogram_model='linear',
                     verbose=False, enable_plotting=False,coordinates_type='geographic' )
print("ok")
# Creates the kriged grid and the variance grid. Allows for kriging on a rectangular
# grid of points, on a masked rectangular grid of points, or with arbitrary points.
# (See OrdinaryKriging.__doc__ for more information.)
z, ss = OK.execute('points', 120.6975, 24.3496)
print(z)
# Writes the kriged grid to an ASCII grid file.
#kt.write_asc_grid(gridx, gridy, z, filename="output.asc")
