Name:		texlive-dox
Version:	2.2
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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The doc package provides LaTeX developers with means to
describe the usage and the definition of new macros and
environments. However, there is no simple way to extend this
functionality to other items (options or counters, for
instance). The DoX package is designed to circumvent this
limitation.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dox/dox.sty
%doc %{_texmfdistdir}/doc/latex/dox/NEWS
%doc %{_texmfdistdir}/doc/latex/dox/README
%doc %{_texmfdistdir}/doc/latex/dox/dox.el
%doc %{_texmfdistdir}/doc/latex/dox/dox.pdf
%doc %{_texmfdistdir}/doc/latex/dox/header.inc
#- source
%doc %{_texmfdistdir}/source/latex/dox/dox.dtx
%doc %{_texmfdistdir}/source/latex/dox/dox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
