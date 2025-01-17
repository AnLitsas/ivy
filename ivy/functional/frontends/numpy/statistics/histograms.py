import ivy
from ivy.func_wrapper import with_supported_dtypes
from ivy.functional.frontends.numpy.func_wrapper import to_ivy_arrays_and_back


@with_supported_dtypes({"1.26.0 and below": ("int64",)}, "numpy")
@to_ivy_arrays_and_back
def bincount(x, /, weights=None, minlength=0):
    return ivy.bincount(x, weights=weights, minlength=minlength)
