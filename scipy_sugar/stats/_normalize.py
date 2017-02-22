from __future__ import division
from __future__ import absolute_import

from numpy import empty_like
from numpy import isfinite
from numpy import asarray

from scipy.stats import rankdata
from scipy.stats import norm

def quantile_gaussianize(x):
    x = asarray(x)
    ok = isfinite(x)
    x[ok] *= -1
    y = empty_like(x)
    y[ok] = rankdata(x[ok])
    y[ok] = norm.isf(y[ok] / (sum(ok) + 1))
    y[~ok] = x[~ok]
    return y
