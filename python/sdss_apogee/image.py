"""
This module defines the APOGEE 2D image Image class.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
#from copy import deepcopy

import numpy as np
from astropy.nddata import NDDataArray

__all__ = ['Image']

class Image(NDDataArray):
    """
    A container for APOGEE 2D images, using the `~astropy.nddata.NDDataArray` interface.

    Parameters
    -----------
    data : `~numpy.ndarray` or `NDData`
        The actual data contained in this `NDData` object. Not that this
        will always be copies by *reference* , so you should make copy
        the ``data`` before passing it in if that's the  desired behavior.

    uncertainty : `~astropy.nddata.NDUncertainty`, optional
        Uncertainties on the data.

    mask : `~numpy.ndarray`-like, optional
        Mask for the data, given as a boolean Numpy array or any object that
        can be converted to a boolean Numpy array with a shape
        matching that of the data. The values must be ``False`` where
        the data is *valid* and ``True`` when it is not (like Numpy
        masked arrays). If ``data`` is a numpy masked array, providing
        ``mask`` here will causes the mask from the masked array to be
        ignored.

    flags : `~numpy.ndarray`-like or `~astropy.nddata.FlagCollection`, optional
        Flags giving information about each pixel. These can be specified
        either as a Numpy array of any type (or an object which can be converted
        to a Numpy array) with a shape matching that of the
        data, or as a `~astropy.nddata.FlagCollection` instance which has a
        shape matching that of the data.

    meta : `dict`-like object, optional
        Metadata for this object.  "Metadata" here means all information that
        is included with this object but not part of any other attribute
        of this particular object.  e.g., creation date, unique identifier,
        simulation parameters, exposure time, telescope name, etc.

    unit : `~astropy.units.UnitBase` instance or str, optional
        The units of the data.

    """

    # Initialize
    def __init__(self, data, error=None, bitmask=None,
                 meta=None, unit=None, *args, **kwd):

        self._flags = None
        
        # Initialize with the parent...
        super(NDDataArray, self).__init__(data, *args, **kwd)    

        # Should we initialize the error/bitmask, etc.
        # to reasonable values or leave them as None?
        
    # String representation
    def __str__(self):
        return str(self.data)

    # Flagging (bpm/littrow/persistence)
    def flagging(self, flag=1, mask=None):
        """
        Set bitmask flags such as BPM, Littrow or persistence flags.

        Parameters
        -----------

        flag : `int`, optional
           The flag value to give for the ``True`` values in the input ``mask``
           image (or all if ``mask`` is not input).  The default value is 1.

        mask : `~numpy.ndarray`-like, optional
           The boolean mask of same size as image that will be used to
           set the flag image with the input ``flag`` value.  If this array
           is not input then all elements are to the flag value.

        """

        # Make sure we have a flag image
        if self.flags is None:
            self.flags = np.zeros(self.data.shape,dtype='int16')
        # Apply the flag
        flagim = self.flags
        if mask is not None:
            self.flags = np.bitwise_or(self.flags,np.int16(mask)*flag)
        else:
            self.flags = np.bitwise_or(self.flags,flag)
            
    # Extraction of 1D spectra
    def extract(self,psf):
        """
        Extract 1D spectra given the necessary input information:

        Parameters
        -----------

        psf : 

        """
                                  
        pass

    # NDDataArray has READ and WRITE function that
    # uses the astropy IO "registry".  Try using that.
    
    # Read from a file
    #def fromfile(self):
    #    pass

    # Write to a file
    #def writeto(self):
    #    pass
