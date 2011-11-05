# revision 20209
# category Package
# catalog-ctan /macros/latex/contrib/sfg
# catalog-date 2010-10-25 17:10:20 +0200
# catalog-license lppl
# catalog-version 0.91
Name:		texlive-sfg
Version:	0.91
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Defines some commands to draw signal flow graphs as used by
electrical and electronics engineers and graph theorists.
Requires fp and pstricks packages (and a relatively fast
machine).

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
%{_texmfdistdir}/tex/latex/sfg/sfg.sty
%doc %{_texmfdistdir}/doc/latex/sfg/Changes
%doc %{_texmfdistdir}/doc/latex/sfg/README
%doc %{_texmfdistdir}/doc/latex/sfg/sfg-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sfg/sfg-doc.tex
%doc %{_texmfdistdir}/doc/latex/sfg/sfg_test.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
