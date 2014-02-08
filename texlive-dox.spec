# revision 20768
# category Package
# catalog-ctan /macros/latex/contrib/dox
# catalog-date 2010-12-16 20:18:25 +0100
# catalog-license lppl
# catalog-version 2.2
Name:		texlive-dox
Version:	2.2
Release:	3
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-2
+ Revision: 751069
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 718253
- texlive-dox
- texlive-dox
- texlive-dox
- texlive-dox

