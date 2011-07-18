Smooth reset
============

The smooth reset panel provides a convenient way to reset all resources tied to enabled and **constant** variables. Each step is always 100 ms.

.. figure:: smooth_reset.*
   :alt: Smooth reset panel.

   ..

   1. Sweep from constant values to zero.
   2. Sweep from zero to constant values.
   3. The number of steps to use.

.. note::

   Those variables which are not set to "const" will not be reset.

.. warning::

   For both directions, the smooth reset panel makes the assumption that the **from** value is the current value of the resource. For example, if the voltage source port behind the resource is sitting at 5 V, and the constant value of the variable is 5, pressing the "To zero" button is safe. If this is not the case, a jump will occur at the beginning of the reset.