#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	OCaml variants as first class values
Summary(pl.UTF-8):	OCamlowe warianty jako wartości pierwszoklasowe
Name:		ocaml-variantslib
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/variantslib/tags
Source0:	https://github.com/janestreet/variantslib/archive/v%{version}/variantslib-%{version}.tar.gz
# Source0-md5:	a8ce0a10f2a52fc81caa7d68431c5d31
URL:		https://github.com/janestreet/variantslib
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
OCaml variants as first class values.

This package contains files needed to run bytecode executables using
variantslib library.

%description -l pl.UTF-8
OCamlowe warianty jako wartości pierwszoklasowe.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki variantslib.

%package devel
Summary:	OCaml variants as first class values - development part
Summary(pl.UTF-8):	OCamlowe warianty jako wartości pierwszoklasowe - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
variantslib library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki variantslib.

%prep
%setup -q -n variantslib-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/variantslib/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/variantslib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md
%dir %{_libdir}/ocaml/variantslib
%{_libdir}/ocaml/variantslib/META
%{_libdir}/ocaml/variantslib/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/variantslib/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/variantslib/*.cmi
%{_libdir}/ocaml/variantslib/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/variantslib/variantslib.a
%{_libdir}/ocaml/variantslib/*.cmx
%{_libdir}/ocaml/variantslib/*.cmxa
%endif
%{_libdir}/ocaml/variantslib/dune-package
%{_libdir}/ocaml/variantslib/opam
