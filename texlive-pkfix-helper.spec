%global tl_name pkfix-helper
%global tl_revision 56061

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Make PostScript files accessible to pkfix
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/pkfix-helper
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pkfix-helper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pkfix-helper.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pkfix-helper.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Pkfix is a useful utility for replacing resolution-dependent bitmapped
fonts in a dvips-produced PostScript file with the corresponding
resolution-independent vector fonts. Unfortunately, pkfix needs to parse
certain PostScript comments that appear only in files produced by dvips
versions later than 5.58 (ca. 1996); it fails to work on PostScript
files produced by older versions of dvips. Pkfix-helper is a program
that attempts to insert newer-dvips comments into an older-dvips
PostScript file, thereby making the file suitable for processing by
pkfix. pkfix-helper can sometimes process documents fully autonomously
but does require the user to verify and, if needed, correct its
decisions.

