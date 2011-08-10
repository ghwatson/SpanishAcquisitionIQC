import logging
log = logging.getLogger(__name__)

from spacq.tool.box import Enum

"""
Figure out which plot formats can be used on this system.
"""


# 2D curve, 3D colormapped, 3D surface, 3D waveforms
formats = Enum(['two_dimensional', 'colormapped', 'surface', 'waveforms'])


# Try to import all available formats.
available_formats = {}

try:
	from .colormapped import ColormappedPlotSetupDialog
except ImportError:
	pass
else:
	available_formats[formats.colormapped] = ColormappedPlotSetupDialog

try:
	from .surface import SurfacePlotSetupDialog, WaveformsPlotSetupDialog
except ImportError:
	pass
else:
	available_formats[formats.surface] = SurfacePlotSetupDialog
	available_formats[formats.waveforms] = WaveformsPlotSetupDialog

try:
	from .two_dimensional import TwoDimensionalPlotSetupDialog
except ImportError:
	pass
else:
	available_formats[formats.two_dimensional] = TwoDimensionalPlotSetupDialog


log.debug('Available plot formats: {0}'.format(', '.join(available_formats.keys())))
