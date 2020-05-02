import numpy as np
import jax.numpy as jnp
from numpy.testing import assert_allclose
from jax_cosmo import Cosmology, Background
import pyccl as ccl

def test_distances_flat():
  # We first define equivalent CCL and jax_cosmo cosmologies
  cosmo_ccl = ccl.Cosmology(
    Omega_c=0.3, Omega_b=0.05, h=0.7, sigma8 = 0.8, n_s=0.96, Neff=0,
    transfer_function='eisenstein_hu', matter_power_spectrum='linear')

  cosmo_jax = Background(Cosmology(Omega_c=0.3, Omega_b=0.05, h=0.7, sigma8 = 0.8, n_s=0.96,
                         Omega_k=0., w0=-1., wa=0))

  # Test array of scale factors
  a = np.linspace(0.01, 1.)

  chi_ccl = ccl.comoving_radial_distance(cosmo_ccl, a)
  chi_jax = cosmo_jax.radial_comoving_distance(a)/cosmo_jax.h
  assert_allclose(chi_ccl, chi_jax, rtol=1e-3)

  chi_ccl = ccl.comoving_angular_distance(cosmo_ccl, a)
  chi_jax = cosmo_jax.transverse_comoving_distance(a)/cosmo_jax.h
  assert_allclose(chi_ccl, chi_jax, rtol=1e-3)

  chi_ccl = ccl.angular_diameter_distance(cosmo_ccl, a)
  chi_jax = cosmo_jax.angular_diameter_distance(a)/cosmo_jax.h
  assert_allclose(chi_ccl, chi_jax, rtol=1e-3)


def test_growth():
  # We first define equivalent CCL and jax_cosmo cosmologies
  cosmo_ccl = ccl.Cosmology(
    Omega_c=0.3, Omega_b=0.05, h=0.7, sigma8 = 0.8, n_s=0.96, Neff=0,
    transfer_function='eisenstein_hu', matter_power_spectrum='linear')

  cosmo_jax = Background(Cosmology(Omega_c=0.3, Omega_b=0.05, h=0.7, sigma8 = 0.8, n_s=0.96,
                         Omega_k=0., w0=-1., wa=0))

  # Test array of scale factors
  a = np.linspace(0.1, 1.)

  gccl = ccl.growth_factor(cosmo_ccl, a)
  gjax = cosmo_jax.growth_factor(a)

  assert_allclose(gccl, gjax, rtol=1e-3)
