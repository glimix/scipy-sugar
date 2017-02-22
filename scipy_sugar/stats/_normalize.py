from __future__ import division
from __future__ import absolute_import

from numpy import empty_like
from numpy import isfinite
from numpy import asarray

from scipy.stats import rankdata
from scipy.stats import norm

def quantile_gaussianize(x):
    """Normalize a sequence of values via rank and Normal c.d.f.

    Args:
        x (array_like): sequence of values.

    Returns:
        Gaussian-normalized values.
    """
    x = asarray(x)
    ok = isfinite(x)
    x[ok] *= -1
    y = empty_like(x)
    y[ok] = rankdata(x[ok])
    y[ok] = norm.isf(y[ok] / (sum(ok) + 1))
    y[~ok] = x[~ok]
    return y
