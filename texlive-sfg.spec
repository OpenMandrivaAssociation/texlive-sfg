Name:		texlive-sfg
Version:	20209
Release:	2
Summary:	Draw signal flow graphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sfg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sfg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sfg.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
