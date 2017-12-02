"""
This module defines the APOGEE 3D datacube Cube class.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
#from copy import deepcopy

import numpy as np
from astropy.nddata import NDDataArray
from image import Image

__all__ = ['Cube']

class Cube(NDDataArray):
    """
    A container for APOGEE datacubes, using the `~astropy.nddata.NDDataArray` interface.

    Parameters
    -----------
    data : `numpy.ndarray`-like 

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

    # String representation
    def __str__(self):
        return str(self.data)

    # Reference pixel correction
    def refpixcorr(self):
        """
        Apply the reference pixel correction
        """
        pass

    # Linearity correction
    def lincorr(self):
        """
        Apply the linearity correction
        """
        pass

    # Dark correction
    def darkcorr(self):
        """
        Apply the dark current correction
        """
        pass

    # Cosmic ray flag and repair
    def cosmicrayflag(self,repair=False):
        """
        Flag cosmic rays and optionally repair them.

        Parameters
        ----------

        repair : `bool`, optional
            If ``True`` then cosmic rays will be repaired.  The default is ``False``.

        """
        pass

    # Saturation flag and report
    def saturateflag(self,repair=False):
        """
        Flag saturated pixels and optionally repair them.

        Parameters
        ----------

        repair : `bool`, optional
            If ``True`` then saturated pixels will be repaired.  The default is ``False``.

        """
        pass

    # Collapse the cube
    def collapse(self,uptheramp=True,fowler=False):
        """
        Collapse the datacube along the time/read axis into a 2D image.

        Parameters
        ----------

        uptheramp : `bool`, optional
            If ``True`` then the up-the-ramp method will be used.  This is the default.

        fowler : `bool`, optional
            If ``True`` then the Fowler method is used.  The default is ``False``.

        """
        
        # Collapse the cube
        imarr = np.sum(self.data,axis=2)
        
        # Need to initialize an Image
        #shape = self.data.shape
        #imshape = shape[0:2]
        #imarr = np.zeros(imshape)
        im = Image(imarr)
        
        return im

    # NDDataArray has READ and WRITE function that
    # uses the astropy IO "registry".  Try using that.
    
    # Read from a file
    #def fromfile(self):
    #    pass

    # Write to a file
    #def writeto(self):
    #    pass
