# revision 32103
# category Package
# catalog-ctan /language/korean/kotex-utf
# catalog-date 2013-11-08 09:28:00 +0100
# catalog-license lppl1.3
# catalog-version 2.0.1
Name:		texlive-kotex-utf
Version:	2.0.1
Release:	4
Summary:	Typeset Hangul, coded in UTF-8
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/korean/kotex-utf
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-utf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-utf.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucs-cmap.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucs-enumerate.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucs-enumitem.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucs-gremph.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucs-interword.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucs-paralist.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucs-sectsty.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucs-setspace.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucs-trivcj.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucs-ucshyper.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/dhucsfn.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/kotex-logo.sty
%{_texmfdistdir}/tex/latex/kotex-utf/contrib/kotex-varioref.sty
%{_texmfdistdir}/tex/latex/kotex-utf/dhucs-nanumfont.sty
%{_texmfdistdir}/tex/latex/kotex-utf/dhucs.sty
%{_texmfdistdir}/tex/latex/kotex-utf/hfontspec.default
%{_texmfdistdir}/tex/latex/kotex-utf/kosections-utf.sty
%{_texmfdistdir}/tex/latex/kotex-utf/kotex.cfg
%{_texmfdistdir}/tex/latex/kotex-utf/kotexutf.sty
%{_texmfdistdir}/tex/latex/kotex-utf/lucenc.dfu
%{_texmfdistdir}/tex/latex/kotex-utf/lucuhcmj.fd
%{_texmfdistdir}/tex/latex/kotex-utf/tex4ht/dhucs.4ht
%{_texmfdistdir}/tex/latex/kotex-utf/tex4ht/dhucs.cfg
%{_texmfdistdir}/tex/latex/kotex-utf/tex4ht/kosections-utf.4ht
%doc %{_texmfdistdir}/doc/latex/kotex-utf/ChangeLog
%doc %{_texmfdistdir}/doc/latex/kotex-utf/README
%doc %{_texmfdistdir}/doc/latex/kotex-utf/fig/allowbreak-dhucs.pdf
%doc %{_texmfdistdir}/doc/latex/kotex-utf/fig/fntexp.pdf
%doc %{_texmfdistdir}/doc/latex/kotex-utf/fig/fntnormal.pdf
%doc %{_texmfdistdir}/doc/latex/kotex-utf/fig/histkotex.jpg
%doc %{_texmfdistdir}/doc/latex/kotex-utf/fig/linebreaktest.pdf
%doc %{_texmfdistdir}/doc/latex/kotex-utf/fig/testdhucsallowbreak.pdf
%doc %{_texmfdistdir}/doc/latex/kotex-utf/kotexdoc.pdf
%doc %{_texmfdistdir}/doc/latex/kotex-utf/kotexdoc.tex
%doc %{_texmfdistdir}/doc/latex/kotex-utf/sample-finemath-setup.tex
%doc %{_texmfdistdir}/doc/latex/kotex-utf/yettext.tex
%doc %{_texmfdistdir}/doc/latex/kotex-utf/yettext.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
