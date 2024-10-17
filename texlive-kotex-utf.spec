Name:		texlive-kotex-utf
Version:	63690
Release:	2
Summary:	Typeset Hangul, coded in UTF-8
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/korean/kotex-utf
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-utf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-utf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-cjk-ko

%description
The package typesets Hangul, which is the native alphabet of
the Korean language; input Korean text should be encoded in
UTF-8. The bundle (of class and associated packages) belongs to
the ko.TeX bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/kotex-utf
%doc %{_texmfdistdir}/doc/latex/kotex-utf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
