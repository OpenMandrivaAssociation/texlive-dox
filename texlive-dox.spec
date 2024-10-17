Name:		texlive-dox
Version:	46011
Release:	2
Summary:	Extend the doc package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The doc package provides LaTeX developers with means to
describe the usage and the definition of new macros and
environments. However, there is no simple way to extend this
functionality to other items (options or counters, for
instance). The DoX package is designed to circumvent this
limitation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dox
%doc %{_texmfdistdir}/doc/latex/dox
#- source
%doc %{_texmfdistdir}/source/latex/dox

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
