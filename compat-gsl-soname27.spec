#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v12
# autospec commit: fbcebd0
#
# Source0 file verified with key 0x245FB74BAE05B3E9 (alken@colorado.edu)
#
Name     : compat-gsl-soname27
Version  : 2.7.1
Release  : 36
URL      : https://mirrors.kernel.org/gnu/gsl/gsl-2.7.1.tar.gz
Source0  : https://mirrors.kernel.org/gnu/gsl/gsl-2.7.1.tar.gz
Source1  : https://mirrors.kernel.org/gnu/gsl/gsl-2.7.1.tar.gz.sig
Source2  : 245FB74BAE05B3E9.pkey
Summary  : GNU Scientific Library
Group    : Development/Tools
License  : GPL-3.0
Requires: compat-gsl-soname27-lib = %{version}-%{release}
Requires: compat-gsl-soname27-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gnupg
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
GSL - GNU Scientific Library
============================
This is GSL, the GNU Scientific Library, a collection of numerical
routines for scientific computing.

%package lib
Summary: lib components for the compat-gsl-soname27 package.
Group: Libraries
Requires: compat-gsl-soname27-license = %{version}-%{release}

%description lib
lib components for the compat-gsl-soname27 package.


%package license
Summary: license components for the compat-gsl-soname27 package.
Group: Default

%description license
license components for the compat-gsl-soname27 package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 245FB74BAE05B3E9' gpg.status
%setup -q -n gsl-2.7.1
cd %{_builddir}/gsl-2.7.1
pushd ..
cp -a gsl-2.7.1 buildavx2
popd
pushd ..
cp -a gsl-2.7.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1717514809
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
GOAMD64=v4
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v4 -mprefer-vector-width=256 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v4 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :
cd ../buildavx512;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1717514809
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-gsl-soname27
cp %{_builddir}/gsl-%{version}/COPYING %{buildroot}/usr/share/package-licenses/compat-gsl-soname27/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/gsl-%{version}/doc/_static/gpl.txt %{buildroot}/usr/share/package-licenses/compat-gsl-soname27/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v4
pushd ../buildavx512/
%make_install_v4
popd
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/libgslcblas.so.0
rm -f %{buildroot}*/usr/lib64/libgslcblas.so.0.0.0
rm -f %{buildroot}*/V3/usr/bin/gsl-histogram
rm -f %{buildroot}*/V3/usr/bin/gsl-randist
rm -f %{buildroot}*/V4/usr/bin/gsl-histogram
rm -f %{buildroot}*/V4/usr/bin/gsl-randist
rm -f %{buildroot}*/usr/bin/gsl-config
rm -f %{buildroot}*/usr/bin/gsl-histogram
rm -f %{buildroot}*/usr/bin/gsl-randist
rm -f %{buildroot}*/usr/include/gsl/gsl_blas.h
rm -f %{buildroot}*/usr/include/gsl/gsl_blas_types.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_char.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_complex_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_complex_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_complex_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_long.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_short.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_uchar.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_uint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_ulong.h
rm -f %{buildroot}*/usr/include/gsl/gsl_block_ushort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_bspline.h
rm -f %{buildroot}*/usr/include/gsl/gsl_bst.h
rm -f %{buildroot}*/usr/include/gsl/gsl_bst_avl.h
rm -f %{buildroot}*/usr/include/gsl/gsl_bst_rb.h
rm -f %{buildroot}*/usr/include/gsl/gsl_bst_types.h
rm -f %{buildroot}*/usr/include/gsl/gsl_cblas.h
rm -f %{buildroot}*/usr/include/gsl/gsl_cdf.h
rm -f %{buildroot}*/usr/include/gsl/gsl_chebyshev.h
rm -f %{buildroot}*/usr/include/gsl/gsl_check_range.h
rm -f %{buildroot}*/usr/include/gsl/gsl_combination.h
rm -f %{buildroot}*/usr/include/gsl/gsl_complex.h
rm -f %{buildroot}*/usr/include/gsl/gsl_complex_math.h
rm -f %{buildroot}*/usr/include/gsl/gsl_const.h
rm -f %{buildroot}*/usr/include/gsl/gsl_const_cgs.h
rm -f %{buildroot}*/usr/include/gsl/gsl_const_cgsm.h
rm -f %{buildroot}*/usr/include/gsl/gsl_const_mks.h
rm -f %{buildroot}*/usr/include/gsl/gsl_const_mksa.h
rm -f %{buildroot}*/usr/include/gsl/gsl_const_num.h
rm -f %{buildroot}*/usr/include/gsl/gsl_deriv.h
rm -f %{buildroot}*/usr/include/gsl/gsl_dft_complex.h
rm -f %{buildroot}*/usr/include/gsl/gsl_dft_complex_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_dht.h
rm -f %{buildroot}*/usr/include/gsl/gsl_diff.h
rm -f %{buildroot}*/usr/include/gsl/gsl_eigen.h
rm -f %{buildroot}*/usr/include/gsl/gsl_errno.h
rm -f %{buildroot}*/usr/include/gsl/gsl_fft.h
rm -f %{buildroot}*/usr/include/gsl/gsl_fft_complex.h
rm -f %{buildroot}*/usr/include/gsl/gsl_fft_complex_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_fft_halfcomplex.h
rm -f %{buildroot}*/usr/include/gsl/gsl_fft_halfcomplex_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_fft_real.h
rm -f %{buildroot}*/usr/include/gsl/gsl_fft_real_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_filter.h
rm -f %{buildroot}*/usr/include/gsl/gsl_fit.h
rm -f %{buildroot}*/usr/include/gsl/gsl_heapsort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_histogram.h
rm -f %{buildroot}*/usr/include/gsl/gsl_histogram2d.h
rm -f %{buildroot}*/usr/include/gsl/gsl_ieee_utils.h
rm -f %{buildroot}*/usr/include/gsl/gsl_inline.h
rm -f %{buildroot}*/usr/include/gsl/gsl_integration.h
rm -f %{buildroot}*/usr/include/gsl/gsl_interp.h
rm -f %{buildroot}*/usr/include/gsl/gsl_interp2d.h
rm -f %{buildroot}*/usr/include/gsl/gsl_linalg.h
rm -f %{buildroot}*/usr/include/gsl/gsl_machine.h
rm -f %{buildroot}*/usr/include/gsl/gsl_math.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_char.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_complex_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_complex_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_complex_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_long.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_short.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_uchar.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_uint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_ulong.h
rm -f %{buildroot}*/usr/include/gsl/gsl_matrix_ushort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_message.h
rm -f %{buildroot}*/usr/include/gsl/gsl_min.h
rm -f %{buildroot}*/usr/include/gsl/gsl_minmax.h
rm -f %{buildroot}*/usr/include/gsl/gsl_mode.h
rm -f %{buildroot}*/usr/include/gsl/gsl_monte.h
rm -f %{buildroot}*/usr/include/gsl/gsl_monte_miser.h
rm -f %{buildroot}*/usr/include/gsl/gsl_monte_plain.h
rm -f %{buildroot}*/usr/include/gsl/gsl_monte_vegas.h
rm -f %{buildroot}*/usr/include/gsl/gsl_movstat.h
rm -f %{buildroot}*/usr/include/gsl/gsl_multifit.h
rm -f %{buildroot}*/usr/include/gsl/gsl_multifit_nlin.h
rm -f %{buildroot}*/usr/include/gsl/gsl_multifit_nlinear.h
rm -f %{buildroot}*/usr/include/gsl/gsl_multilarge.h
rm -f %{buildroot}*/usr/include/gsl/gsl_multilarge_nlinear.h
rm -f %{buildroot}*/usr/include/gsl/gsl_multimin.h
rm -f %{buildroot}*/usr/include/gsl/gsl_multiroots.h
rm -f %{buildroot}*/usr/include/gsl/gsl_multiset.h
rm -f %{buildroot}*/usr/include/gsl/gsl_nan.h
rm -f %{buildroot}*/usr/include/gsl/gsl_ntuple.h
rm -f %{buildroot}*/usr/include/gsl/gsl_odeiv.h
rm -f %{buildroot}*/usr/include/gsl/gsl_odeiv2.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permutation.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_char.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_complex_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_complex_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_complex_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_long.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_char.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_complex_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_complex_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_complex_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_long.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_short.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_uchar.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_uint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_ulong.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_matrix_ushort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_short.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_uchar.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_uint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_ulong.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_ushort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_char.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_complex_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_complex_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_complex_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_long.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_short.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_uchar.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_uint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_ulong.h
rm -f %{buildroot}*/usr/include/gsl/gsl_permute_vector_ushort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_poly.h
rm -f %{buildroot}*/usr/include/gsl/gsl_pow_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_precision.h
rm -f %{buildroot}*/usr/include/gsl/gsl_qrng.h
rm -f %{buildroot}*/usr/include/gsl/gsl_randist.h
rm -f %{buildroot}*/usr/include/gsl/gsl_rng.h
rm -f %{buildroot}*/usr/include/gsl/gsl_roots.h
rm -f %{buildroot}*/usr/include/gsl/gsl_rstat.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_airy.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_bessel.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_clausen.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_coulomb.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_coupling.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_dawson.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_debye.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_dilog.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_elementary.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_ellint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_elljac.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_erf.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_exp.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_expint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_fermi_dirac.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_gamma.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_gegenbauer.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_hermite.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_hyperg.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_laguerre.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_lambert.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_legendre.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_log.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_mathieu.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_pow_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_psi.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_result.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_sincos_pi.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_synchrotron.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_transport.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_trig.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sf_zeta.h
rm -f %{buildroot}*/usr/include/gsl/gsl_siman.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_char.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_long.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_short.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_uchar.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_uint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_ulong.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_ushort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_char.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_long.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_short.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_uchar.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_uint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_ulong.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sort_vector_ushort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spblas.h
rm -f %{buildroot}*/usr/include/gsl/gsl_specfunc.h
rm -f %{buildroot}*/usr/include/gsl/gsl_splinalg.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spline.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spline2d.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_char.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_complex_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_complex_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_complex_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_long.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_short.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_uchar.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_uint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_ulong.h
rm -f %{buildroot}*/usr/include/gsl/gsl_spmatrix_ushort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_char.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_long.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_short.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_uchar.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_uint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_ulong.h
rm -f %{buildroot}*/usr/include/gsl/gsl_statistics_ushort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sum.h
rm -f %{buildroot}*/usr/include/gsl/gsl_sys.h
rm -f %{buildroot}*/usr/include/gsl/gsl_test.h
rm -f %{buildroot}*/usr/include/gsl/gsl_types.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_char.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_complex.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_complex_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_complex_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_complex_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_float.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_int.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_long.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_long_double.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_short.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_uchar.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_uint.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_ulong.h
rm -f %{buildroot}*/usr/include/gsl/gsl_vector_ushort.h
rm -f %{buildroot}*/usr/include/gsl/gsl_version.h
rm -f %{buildroot}*/usr/include/gsl/gsl_wavelet.h
rm -f %{buildroot}*/usr/include/gsl/gsl_wavelet2d.h
rm -f %{buildroot}*/usr/include/gsl/test_source.c
rm -f %{buildroot}*/usr/lib64/libgsl.so
rm -f %{buildroot}*/usr/lib64/libgslcblas.so
rm -f %{buildroot}*/usr/lib64/pkgconfig/gsl.pc
rm -f %{buildroot}*/usr/share/aclocal/gsl.m4
rm -f %{buildroot}*/usr/share/info/gsl-ref.info
rm -f %{buildroot}*/usr/share/man/man1/gsl-config.1
rm -f %{buildroot}*/usr/share/man/man1/gsl-histogram.1
rm -f %{buildroot}*/usr/share/man/man1/gsl-randist.1
rm -f %{buildroot}*/usr/share/man/man3/gsl.3
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgsl.so.27.0.0
/V4/usr/lib64/libgsl.so.27.0.0
/usr/lib64/libgsl.so.27
/usr/lib64/libgsl.so.27.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-gsl-soname27/8624bcdae55baeef00cd11d5dfcfa60f68710a02
