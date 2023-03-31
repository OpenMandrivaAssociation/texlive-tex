Name:		texlive-tex
Version:	62387
Release:	2
Summary:	A sophisticated typesetting engine
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/tex
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-tetex
Requires:	texlive-kpathsea
Requires:	texlive-plain
Requires:	texlive-tex.bin

%description
TeX is a typesetting system that incorporates a macro
processor. A TeX source document specifies or incorporates a
number of macro definitions that instruct the TeX engine how to
typeset the document. The TeX engine also uses font metrics
generated by Metafont, or by any of several other mechanisms
that incorporate fonts from other sources into an environment
suitable for TeX. TeX has been, and continues, a basis and an
inspiration for several other programs, including e-TeX and
PDFTeX. The distribution includes the source of Knuth's TeX
book; this source is there to read, as an example of writing
TeX -- it should not be processed without Knuth's direct
permission.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%_texmf_fmtutil_d/tex
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/tex <<EOF
#
# from tex:
tex tex - tex.ini
EOF
