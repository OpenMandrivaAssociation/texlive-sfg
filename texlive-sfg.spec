# revision 20209
# category Package
# catalog-ctan /macros/latex/contrib/sfg
# catalog-date 2010-10-25 17:10:20 +0200
# catalog-license lppl
# catalog-version 0.91
Name:		texlive-sfg
Version:	0.91
Release:	9
Summary:	Draw signal flow graphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sfg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sfg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sfg.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines some commands to draw signal flow graphs as used by
electrical and electronics engineers and graph theorists.
Requires fp and pstricks packages (and a relatively fast
machine).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sfg/sfg.sty
%doc %{_texmfdistdir}/doc/latex/sfg/Changes
%doc %{_texmfdistdir}/doc/latex/sfg/README
%doc %{_texmfdistdir}/doc/latex/sfg/sfg-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sfg/sfg-doc.tex
%doc %{_texmfdistdir}/doc/latex/sfg/sfg_test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.91-2
+ Revision: 755925
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.91-1
+ Revision: 719517
- texlive-sfg
- texlive-sfg
- texlive-sfg
- texlive-sfg

