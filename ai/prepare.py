import h5py
import numpy as np

f = h5py.File("mytestfile.hdf5", "w")
dset = f.create_dataset("data", (45406), dtype='i')
