"""
This package contains algorithms for the computation of the influence function.

.. warning::
   Much of the code in this package is experimental or untested and is subject
   to modification. In particular, the package structure and basic API will
   probably change.

"""
from .frameworks import TorchTwiceDifferentiable, TwiceDifferentiable
from .general import compute_influence_factors, compute_influences
