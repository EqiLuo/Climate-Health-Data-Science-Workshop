
#########################################################################################################
#
#   Hourly tw
#   Cascade Tuholske Jan 2024 cascade (d0t) tuholske1 (at) montana (d0t) edu 
#
#   Code to calculate hourly wet bulb globe temperture (tw) following the NEWT method
#   from ERA5 surface pressure, dew point temperature, and 2m air temperature. 
#
#   NEWT code has been borrowed from: https://github.com/robwarrenwx/atmos/tree/main
#
#   Notes 2024-01-16: Set up to run on one small annual NetCDF File. Will need to be adjusted to
#   to run on full global (cpt). 
#
#########################################################################################################

# Dependencies
import dask
import os
import glob
import xarray as xr
import numpy as np
import pandas as pd
import rioxarray as rio
import sys
import rasterio
from dask.distributed import Client, LocalCluster
from atmos import moisture 
from atmos import thermo 

# Run it
if __name__ == "__main__":
    
    # start cluster 
    n_cpu = 10 # number of CPUs for dask to work with 
    cluster = LocalCluster(n_workers = n_cpu, threads_per_worker = 1) # online forms say 1 thread is fastests 
    client = Client(cluster)
    print('start!')
    print('progress url:', client.dashboard_link)
    
    # Set up path + file
    path = os.path.join('../data/raw/ERA5/')
    fn = os.path.join(path, 'BGD-WBT-Inputs-2020.nc')
    print('start: ', fn) 
    
    # Code to set up list of monthly .netcdf files if needed
    
    # File names to write hourly tw files 
    handles = fn.split(path)[1].split('-')
    fn_out = os.path.join('../data/processed/'+handles[0]+'-'+handles[1]+'-hr-'+handles[3])
    print('File out:', fn_out)
    
    # Code to stack and open as Dask Array all monthly .netcdf files 
    
    # Open as Dask Array single file                                
    chunk = dict(time='auto', latitude= 'auto', longitude= 'auto') # need  pull len the time dim automatically
                                                                   # Chunk will need reconfiged for global raster       
    ds = xr.open_dataset(fn, chunks = chunk)
    
    # Hourly WBT
    
    # first specific_humidity_from_dewpoint_temperature(p, Td) - Don't compute dask arrays yet
    q = xr.apply_ufunc(moisture.specific_humidity_from_dewpoint_temperature, ds.sp, ds.d2m, dask='parallelized')
    q = q.rename('q')
    
    # Compute dask arrays: adiabatic_wet_bulb_temperature(p, T, q, phase='liquid', pseudo_method='polynomial')
    tw = xr.apply_ufunc(thermo.adiabatic_wet_bulb_temperature, ds.sp, ds.t2m, q, dask='parallelized').compute()
    tw = tw - 273.15 # k to c
    tw = tw.rename('tw')
    
    # To ds then write to disk
    tw_ds = tw.to_dataset()
    
    # Add attributes 
    # Needs spatial data from inputfile 
    tw_ds.attrs = dict(data = 'wet buble temperature from ERA5', method='NEWT', unit = '°C')

    tw_ds.to_netcdf(fn_out)
    print('done!')