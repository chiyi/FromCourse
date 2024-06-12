import sys
import numpy
import tensorflow as tf
import tensorflow_probability as tfp

# A high-dimensional quadratic bowl.
ndims = 60
minimum = numpy.ones([ndims], dtype='float64')
scales = numpy.arange(ndims, dtype='float64') + 1.0

# The objective function and the gradient.
def quadratic_loss_and_gradient(x):
  return tfp.math.value_and_gradient(
      lambda x: tf.reduce_sum(
          scales * tf.math.squared_difference(x, minimum), axis=-1),
      x)
start = numpy.arange(ndims, 0, -1, dtype='float64')
optim_results = tfp.optimizer.lbfgs_minimize(
    quadratic_loss_and_gradient,
    initial_position=start,
    num_correction_pairs=10,
    tolerance=1e-8)

# Check that the search converged
assert(optim_results.converged)
# Check that the argmin is close to the actual value.
numpy.testing.assert_allclose(optim_results.position, minimum)
