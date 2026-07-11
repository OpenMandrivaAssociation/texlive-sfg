%global tl_name sfg
%global tl_revision 20209

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.91
Release:	%{tl_revision}.1
Summary:	Draw signal flow graphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sfg
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sfg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sfg.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines some commands to draw signal flow graphs as used by electrical
and electronics engineers and graph theorists. Requires fp and pstricks
packages (and a relatively fast machine).

