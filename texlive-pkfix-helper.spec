# revision 22981
# category Package
# catalog-ctan /support/pkfix-helper
# catalog-date 2011-06-13 21:57:04 +0200
# catalog-license lppl
# catalog-version 1.4
Name:		texlive-pkfix-helper
Version:	1.4
Release:	1
Summary:	Make PostScript files accessible to pkfix
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/pkfix-helper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkfix-helper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkfix-helper.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-pkfix-helper.bin = %{EVRD}

%description
Pkfix is a useful utility for replacing resolution-dependent
bitmapped fonts in a dvips-produced PostScript file with the
corresponding resolution-independent vector fonts.
Unfortunately, pkfix needs to parse certain PostScript comments
that appear only in files produced by dvips versions later than
5.58 (ca. 1996); it fails to work on PostScript files produced
by older versions of dvips. Pkfix-helper is a program that
attempts to insert newer-dvips comments into an older-dvips
PostScript file, thereby making the file suitable for
processing by pkfix. pkfix-helper can sometimes process
documents fully autonomously but does require the user to
verify and, if needed, correct its decisions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/pkfix-helper
%{_texmfdistdir}/scripts/pkfix-helper/pkfix-helper
%doc %{_texmfdistdir}/doc/support/pkfix-helper/README
%doc %{_texmfdistdir}/doc/support/pkfix-helper/encoding-samples.pdf
%doc %{_texmfdistdir}/doc/support/pkfix-helper/encoding-samples.tex
%doc %{_mandir}/man1/pkfix-helper.1*
%doc %{_texmfdir}/doc/man/man1/pkfix-helper.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/pkfix-helper/pkfix-helper pkfix-helper
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
