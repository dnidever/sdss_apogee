"""
This module defines the APOGEE 2D Spectrum2D class.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
from astropy.nddata import NDDataArray
from specutils import Spectrum1D
from spectrum import Spectrum

__all__ = ['Spectrum2D']

class Spectrum2D(Spectrum):
    """
    A container for APOGEE 2D spectra, using the `~spectrum.Spectrum` interface.

    Parameters
    ----------
    data : `~numpy.ndarray`
        flux of the spectrum

    unit : `~astropy.unit.Unit` or None, optional
        unit of the flux, default=None

    flags : `~numpy.ndarray`, optional
        Bitmask flag image for the data.

    mask : `~numpy.ndarray`, optional
        Mask for the data, given as a boolean Numpy array with a shape
        matching that of the data. The values must be ``False`` where
        the data is *valid* and ``True`` when it is not (like Numpy
        masked arrays). If `data` is a numpy masked array, providing
        `mask` here will causes the mask from the masked array to be
        ignored.

    meta : `dict`-like object, optional
        Metadata for this object.  "Metadata" here means all information that
        is included with this object but not part of any other attribute
        of this particular object.  e.g., creation date, unique identifier,
        simulation parameters, exposure time, telescope name, etc.

    """

    # Initialize
    def __init__(self, data, error=None, flags=None,
                 meta=None, unit=None, *args, **kwd):

        self._flags = None
        
        # Initialize with the parent...
        super(Spectrum, self).__init__(data, *args, **kwd)

        # Should we initialize the error/bitmask, etc.
        # to reasonable values or leave them as None?
        
    # String representation
    def __str__(self):
        return str(self.data)

    # Sky subtract
    def skysub(self):
        """
        Perform sky subtraction using the sky fibers.

        Parameters
        -----------

        
        """
        pass
        
    # Telluric correct
        """
        Perform telluric correction using the telluric/hot star fibers.

        Parameters
        -----------

        
        """
        pass
    
    # Wavelength correct
        """
        Apply a wavelength correction (shift) for each fiber using the airglow lines.

        Parameters
        -----------

        
        """
        pass
    
    # Relative flux calibration
        """
        Perform relative flux calibration.

        Parameters
        -----------

        
        """
        pass
    
    # Absolute flux calibration
        """
        Perform absolute flux calibration using the H-band magnitude for the stars.

        Parameters
        -----------

        
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
