%global tl_name kotex-utf
%global tl_revision 63690

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0.0
Release:	%{tl_revision}.1
Summary:	Typeset Hangul, coded in UTF-8
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/korean/kotex-utf
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-utf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-utf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cjk-ko)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package typesets Hangul, which is the native alphabet of the Korean
language; input Korean text should be encoded in UTF-8. The bundle (of
class and associated packages) belongs to the ko.TeX bundle.

