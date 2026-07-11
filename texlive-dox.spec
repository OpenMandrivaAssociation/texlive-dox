%global tl_name dox
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Extend the doc package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The doc package provides LaTeX developers with means to describe the
usage and the definition of new macros and environments. However, there
is no simple way to extend this functionality to other items (options or
counters, for instance). The DoX package is designed to circumvent this
limitation.

