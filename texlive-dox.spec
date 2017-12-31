Name:		texlive-dox
Version:	2.4
Release:	1
Summary:	Extend the doc package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dox.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
