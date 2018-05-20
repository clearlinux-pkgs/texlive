#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : texlive
Version  : 20180414
Release  : 2
URL      : http://ctan.mirrors.hoobly.com/systems/texlive/Source/texlive-20180414-source.tar.xz
Source0  : http://ctan.mirrors.hoobly.com/systems/texlive/Source/texlive-20180414-source.tar.xz
Summary  : Descriptive vector graphics language
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSD-3-Clause-Clear BSL-1.0 CPL-1.0 FTL GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-2.1+ LGPL-3.0 Libpng MIT MPL-1.1 MakeIndex NCSA NPL-1.1 Zlib
Requires: texlive-bin
Requires: texlive-man
Requires: texlive-data
BuildRequires : LuaJIT
BuildRequires : LuaJIT-dev
BuildRequires : bison
BuildRequires : cairo-dev
BuildRequires : cmake
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : flex
BuildRequires : freetype
BuildRequires : freetype-dev
BuildRequires : ghostscript
BuildRequires : ghostscript-dev
BuildRequires : gmp-dev
BuildRequires : grep
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : harfbuzz-dev
BuildRequires : icu4c
BuildRequires : icu4c-dev
BuildRequires : libXmu-dev
BuildRequires : libgd-dev
BuildRequires : libpng-dev
BuildRequires : libxslt-bin
BuildRequires : mpfr-dev
BuildRequires : pixman-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-ft)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(xpm)
BuildRequires : poppler
BuildRequires : poppler-dev
BuildRequires : qtbase-dev
BuildRequires : sed

%description
Asymptote is a powerful descriptive vector graphics language for technical
drawings, inspired by MetaPost but with an improved C++-like syntax.
Asymptote provides for figures the same high-quality level of typesetting
that LaTeX does for scientific text.

%package bin
Summary: bin components for the texlive package.
Group: Binaries
Requires: texlive-data
Requires: texlive-man

%description bin
bin components for the texlive package.


%package data
Summary: data components for the texlive package.
Group: Data

%description data
data components for the texlive package.


%package dev
Summary: dev components for the texlive package.
Group: Development
Requires: texlive-bin
Requires: texlive-data
Provides: texlive-devel

%description dev
dev components for the texlive package.


%package doc
Summary: doc components for the texlive package.
Group: Documentation
Requires: texlive-man

%description doc
doc components for the texlive package.


%package man
Summary: man components for the texlive package.
Group: Default

%description man
man components for the texlive package.


%prep
%setup -q -n texlive-20180414-source

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526786577
%configure --disable-static --enable-build-in-source-tree \
--with-system-poppler \
--with-system-mpfr \
--with-system-gmp \
--with-system-cairo \
--with-system-libpng \
--with-system-pixman \
--with-system-gd \
--with-system-zlib \
--with-system-freetype \
--disable-native-texlive-build \
--disable-web2c \
--disable-dvisvgm \
--disable-xdvik
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1526786577
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/a2ping
/usr/bin/a5toa4
/usr/bin/adhocfilelist
/usr/bin/afm2afm
/usr/bin/afm2pl
/usr/bin/afm2tfm
/usr/bin/allcm
/usr/bin/allec
/usr/bin/allneeded
/usr/bin/arara
/usr/bin/arlatex
/usr/bin/authorindex
/usr/bin/autoinst
/usr/bin/autosp
/usr/bin/axohelp
/usr/bin/bbl2bib
/usr/bin/bbox
/usr/bin/bg5+latex
/usr/bin/bg5+pdflatex
/usr/bin/bg5conv
/usr/bin/bg5latex
/usr/bin/bg5pdflatex
/usr/bin/bib2gls
/usr/bin/bibdoiadd
/usr/bin/bibexport
/usr/bin/bibmradd
/usr/bin/bibtex8
/usr/bin/bibtexu
/usr/bin/biburl2doi
/usr/bin/bibzbladd
/usr/bin/bundledoc
/usr/bin/cachepic
/usr/bin/cef5conv
/usr/bin/cef5latex
/usr/bin/cef5pdflatex
/usr/bin/cefconv
/usr/bin/ceflatex
/usr/bin/cefpdflatex
/usr/bin/cefsconv
/usr/bin/cefslatex
/usr/bin/cefspdflatex
/usr/bin/cfftot1
/usr/bin/checkcites
/usr/bin/checklistings
/usr/bin/chktex
/usr/bin/chkweb
/usr/bin/cjk-gs-integrate
/usr/bin/context
/usr/bin/contextjit
/usr/bin/convbkmk
/usr/bin/convertgls2bib
/usr/bin/ctan-o-mat
/usr/bin/ctanify
/usr/bin/ctanupload
/usr/bin/de-macro
/usr/bin/depythontex
/usr/bin/detex
/usr/bin/devnag
/usr/bin/deweb
/usr/bin/diadia
/usr/bin/disdvi
/usr/bin/dosepsbin
/usr/bin/dt2dv
/usr/bin/dtxgen
/usr/bin/dv2dt
/usr/bin/dvi2fax
/usr/bin/dvi2tty
/usr/bin/dviasm
/usr/bin/dvibook
/usr/bin/dviconcat
/usr/bin/dvidvi
/usr/bin/dvigif
/usr/bin/dvihp
/usr/bin/dviinfox
/usr/bin/dvilj
/usr/bin/dvilj2p
/usr/bin/dvilj4
/usr/bin/dvilj4l
/usr/bin/dvilj6
/usr/bin/dvipdfm
/usr/bin/dvipdfmx
/usr/bin/dvipdft
/usr/bin/dvipng
/usr/bin/dvipos
/usr/bin/dvips
/usr/bin/dvired
/usr/bin/dviselect
/usr/bin/dvitodvi
/usr/bin/e2pall
/usr/bin/ebb
/usr/bin/ebong
/usr/bin/epsffit
/usr/bin/epspdf
/usr/bin/epspdftk
/usr/bin/epstopdf
/usr/bin/exceltex
/usr/bin/extconv
/usr/bin/extractbb
/usr/bin/extractres
/usr/bin/fig4latex
/usr/bin/findhyph
/usr/bin/fmtutil
/usr/bin/fmtutil-sys
/usr/bin/fmtutil-user
/usr/bin/fontinst
/usr/bin/fragmaster
/usr/bin/gbklatex
/usr/bin/gbkpdflatex
/usr/bin/getmapdl
/usr/bin/gregorio
/usr/bin/gsftopk
/usr/bin/hbf2gf
/usr/bin/ht
/usr/bin/htcontext
/usr/bin/htlatex
/usr/bin/htmex
/usr/bin/httex
/usr/bin/httexi
/usr/bin/htxelatex
/usr/bin/htxetex
/usr/bin/includeres
/usr/bin/installfont-tl
/usr/bin/jamo-normalize
/usr/bin/jfmutil
/usr/bin/kanji-config-updmap
/usr/bin/kanji-config-updmap-sys
/usr/bin/kanji-config-updmap-user
/usr/bin/kanji-fontmap-creator
/usr/bin/komkindex
/usr/bin/kpseaccess
/usr/bin/kpsepath
/usr/bin/kpsereadlink
/usr/bin/kpsestat
/usr/bin/kpsetool
/usr/bin/kpsewhere
/usr/bin/kpsewhich
/usr/bin/kpsexpand
/usr/bin/l3build
/usr/bin/lacheck
/usr/bin/latex-git-log
/usr/bin/latex-papersize
/usr/bin/latex2man
/usr/bin/latex2nemeth
/usr/bin/latexdef
/usr/bin/latexdiff
/usr/bin/latexdiff-vc
/usr/bin/latexfileversion
/usr/bin/latexindent
/usr/bin/latexmk
/usr/bin/latexpand
/usr/bin/latexrevise
/usr/bin/lily-glyph-commands
/usr/bin/lily-image-commands
/usr/bin/lily-rebuild-pdfs
/usr/bin/listbib
/usr/bin/listings-ext.sh
/usr/bin/ltx2crossrefxml
/usr/bin/ltxfileinfo
/usr/bin/ltximg
/usr/bin/lua2dox_filter
/usr/bin/luaotfload-tool
/usr/bin/luatools
/usr/bin/lwarpmk
/usr/bin/m-tx
/usr/bin/mag
/usr/bin/make4ht
/usr/bin/makedtx
/usr/bin/makeglossaries
/usr/bin/makeglossaries-lite
/usr/bin/makeindex
/usr/bin/makejvf
/usr/bin/match_parens
/usr/bin/mathspic
/usr/bin/mendex
/usr/bin/mf2pt1
/usr/bin/mk4ht
/usr/bin/mkgrkindex
/usr/bin/mkindex
/usr/bin/mkjobtexmf
/usr/bin/mkpic
/usr/bin/mkt1font
/usr/bin/mktexfmt
/usr/bin/mktexlsr
/usr/bin/mktexmf
/usr/bin/mktexpk
/usr/bin/mktextfm
/usr/bin/mmafm
/usr/bin/mmpfb
/usr/bin/mptopdf
/usr/bin/msxlint
/usr/bin/mtxrun
/usr/bin/mtxrunjit
/usr/bin/multibibliography
/usr/bin/musixflx
/usr/bin/musixtex
/usr/bin/ot2kpx
/usr/bin/otfinfo
/usr/bin/otftotfm
/usr/bin/pdf180
/usr/bin/pdf270
/usr/bin/pdf90
/usr/bin/pdfannotextractor
/usr/bin/pdfatfi
/usr/bin/pdfbook
/usr/bin/pdfbook2
/usr/bin/pdfclose
/usr/bin/pdfcrop
/usr/bin/pdfflip
/usr/bin/pdfjam
/usr/bin/pdfjam-pocketmod
/usr/bin/pdfjam-slides3up
/usr/bin/pdfjam-slides6up
/usr/bin/pdfjoin
/usr/bin/pdflatexpicscale
/usr/bin/pdfnup
/usr/bin/pdfopen
/usr/bin/pdfpun
/usr/bin/pdfxup
/usr/bin/pedigree
/usr/bin/perltex
/usr/bin/pfarrei
/usr/bin/pfb2pfa
/usr/bin/pk2bm
/usr/bin/pkfix
/usr/bin/pkfix-helper
/usr/bin/pmxab
/usr/bin/pmxchords
/usr/bin/pn2pdf
/usr/bin/prepmx
/usr/bin/ps2eps
/usr/bin/ps2frag
/usr/bin/ps2pk
/usr/bin/ps4pdf
/usr/bin/psbook
/usr/bin/psjoin
/usr/bin/pslatex
/usr/bin/psnup
/usr/bin/psresize
/usr/bin/psselect
/usr/bin/pst2pdf
/usr/bin/pstops
/usr/bin/ptex2pdf
/usr/bin/purifyeps
/usr/bin/pygmentex
/usr/bin/pythontex
/usr/bin/repstopdf
/usr/bin/rpdfcrop
/usr/bin/rubibtex
/usr/bin/rubikrotation
/usr/bin/rumakeindex
/usr/bin/rungs
/usr/bin/scor2prt
/usr/bin/simpdftex
/usr/bin/sjisconv
/usr/bin/sjislatex
/usr/bin/sjispdflatex
/usr/bin/splitindex
/usr/bin/srcredact
/usr/bin/sty2dtx
/usr/bin/svn-multi
/usr/bin/t1ascii
/usr/bin/t1asm
/usr/bin/t1binary
/usr/bin/t1disasm
/usr/bin/t1dotlessj
/usr/bin/t1lint
/usr/bin/t1mac
/usr/bin/t1rawafm
/usr/bin/t1reencode
/usr/bin/t1testpage
/usr/bin/t1unmac
/usr/bin/t4ht
/usr/bin/tex2aspc
/usr/bin/tex4ebook
/usr/bin/tex4ht
/usr/bin/texconfig
/usr/bin/texconfig-dialog
/usr/bin/texconfig-sys
/usr/bin/texcount
/usr/bin/texdef
/usr/bin/texdiff
/usr/bin/texdirflatten
/usr/bin/texdoc
/usr/bin/texdoctk
/usr/bin/texexec
/usr/bin/texfot
/usr/bin/texhash
/usr/bin/texlinks
/usr/bin/texliveonfly
/usr/bin/texloganalyser
/usr/bin/texmfstart
/usr/bin/texosquery
/usr/bin/texosquery-jre5
/usr/bin/texosquery-jre8
/usr/bin/thumbpdf
/usr/bin/tlcockpit
/usr/bin/tlmgr
/usr/bin/tlshell
/usr/bin/tpic2pdftex
/usr/bin/ttf2kotexfont
/usr/bin/ttf2pk
/usr/bin/ttf2tfm
/usr/bin/ttfdump
/usr/bin/ttftotype42
/usr/bin/typeoutfileinfo
/usr/bin/ulqda
/usr/bin/updmap
/usr/bin/updmap-sys
/usr/bin/updmap-user
/usr/bin/upmendex
/usr/bin/urlbst
/usr/bin/vlna
/usr/bin/vpe
/usr/bin/vpl2ovp
/usr/bin/vpl2vpl
/usr/bin/wordcount
/usr/bin/xdvipdfmx
/usr/bin/xhlatex
/usr/bin/yplan

%files data
%defattr(-,root,root,-)
/usr/share/texmf-dist/bibtex/csf/base/88591lat.csf
/usr/share/texmf-dist/bibtex/csf/base/88591sca.csf
/usr/share/texmf-dist/bibtex/csf/base/ascii.csf
/usr/share/texmf-dist/bibtex/csf/base/cp437lat.csf
/usr/share/texmf-dist/bibtex/csf/base/cp850lat.csf
/usr/share/texmf-dist/bibtex/csf/base/cp850sca.csf
/usr/share/texmf-dist/bibtex/csf/base/cp866rus.csf
/usr/share/texmf-dist/bibtex/csf/base/csfile.txt
/usr/share/texmf-dist/chktex/chktexrc
/usr/share/texmf-dist/doc/bibtex8/00readme.txt
/usr/share/texmf-dist/doc/bibtex8/HISTORY
/usr/share/texmf-dist/doc/bibtex8/csfile.txt
/usr/share/texmf-dist/doc/bibtex8/file_id.diz
/usr/share/texmf-dist/doc/chktex/ChkTeX.pdf
/usr/share/texmf-dist/dvipdfmx/dvipdfmx.cfg
/usr/share/texmf-dist/dvips/base/color.pro
/usr/share/texmf-dist/dvips/base/crop.pro
/usr/share/texmf-dist/dvips/base/finclude.pro
/usr/share/texmf-dist/dvips/base/hps.pro
/usr/share/texmf-dist/dvips/base/special.pro
/usr/share/texmf-dist/dvips/base/tex.pro
/usr/share/texmf-dist/dvips/base/texc.pro
/usr/share/texmf-dist/dvips/base/texps.pro
/usr/share/texmf-dist/dvips/gsftopk/render.ps
/usr/share/texmf-dist/fonts/cmap/dvipdfmx/EUC-UCS2
/usr/share/texmf-dist/fonts/enc/dvips/base/7t.enc
/usr/share/texmf-dist/fonts/enc/ttf2pk/base/T1-WGL4.enc
/usr/share/texmf-dist/fonts/map/dvipdfmx/cid-x.map
/usr/share/texmf-dist/fonts/map/glyphlist/glyphlist.txt
/usr/share/texmf-dist/fonts/map/glyphlist/pdfglyphlist.txt
/usr/share/texmf-dist/fonts/map/glyphlist/texglyphlist.txt
/usr/share/texmf-dist/fonts/sfd/ttf2pk/Big5.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/EUC.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/HKSCS.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/KS-HLaTeX.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/SJIS.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/UBg5plus.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/UBig5.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/UGB.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/UGBK.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/UJIS.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/UKS-HLaTeX.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/UKS.sfd
/usr/share/texmf-dist/fonts/sfd/ttf2pk/Unicode.sfd
/usr/share/texmf-dist/hbf2gf/b5ka12.cfg
/usr/share/texmf-dist/hbf2gf/b5kr12.cfg
/usr/share/texmf-dist/hbf2gf/b5so12.cfg
/usr/share/texmf-dist/hbf2gf/c1so12.cfg
/usr/share/texmf-dist/hbf2gf/c2so12.cfg
/usr/share/texmf-dist/hbf2gf/c3so12.cfg
/usr/share/texmf-dist/hbf2gf/c4so12.cfg
/usr/share/texmf-dist/hbf2gf/c5so12.cfg
/usr/share/texmf-dist/hbf2gf/c6so12.cfg
/usr/share/texmf-dist/hbf2gf/c7so12.cfg
/usr/share/texmf-dist/hbf2gf/csso12.cfg
/usr/share/texmf-dist/hbf2gf/gsfs14.cfg
/usr/share/texmf-dist/hbf2gf/j2so12.cfg
/usr/share/texmf-dist/hbf2gf/jsso12.cfg
/usr/share/texmf-dist/hbf2gf/ksso17.cfg
/usr/share/texmf-dist/psutils/paper.cfg
/usr/share/texmf-dist/scripts/a2ping/a2ping.pl
/usr/share/texmf-dist/scripts/accfonts/mkt1font
/usr/share/texmf-dist/scripts/accfonts/vpl2ovp
/usr/share/texmf-dist/scripts/accfonts/vpl2vpl
/usr/share/texmf-dist/scripts/adhocfilelist/adhocfilelist.sh
/usr/share/texmf-dist/scripts/arara/arara.sh
/usr/share/texmf-dist/scripts/authorindex/authorindex
/usr/share/texmf-dist/scripts/bib2gls/bib2gls.sh
/usr/share/texmf-dist/scripts/bib2gls/convertgls2bib.sh
/usr/share/texmf-dist/scripts/bibexport/bibexport.sh
/usr/share/texmf-dist/scripts/bundledoc/arlatex
/usr/share/texmf-dist/scripts/bundledoc/bundledoc
/usr/share/texmf-dist/scripts/cachepic/cachepic.tlu
/usr/share/texmf-dist/scripts/checkcites/checkcites.lua
/usr/share/texmf-dist/scripts/checklistings/checklistings.sh
/usr/share/texmf-dist/scripts/chktex/chkweb.sh
/usr/share/texmf-dist/scripts/chktex/deweb.pl
/usr/share/texmf-dist/scripts/cjk-gs-integrate/cjk-gs-integrate.pl
/usr/share/texmf-dist/scripts/context/perl/mptopdf.pl
/usr/share/texmf-dist/scripts/context/stubs/unix/context
/usr/share/texmf-dist/scripts/context/stubs/unix/contextjit
/usr/share/texmf-dist/scripts/context/stubs/unix/luatools
/usr/share/texmf-dist/scripts/context/stubs/unix/mtxrun
/usr/share/texmf-dist/scripts/context/stubs/unix/mtxrunjit
/usr/share/texmf-dist/scripts/context/stubs/unix/texexec
/usr/share/texmf-dist/scripts/context/stubs/unix/texmfstart
/usr/share/texmf-dist/scripts/convbkmk/convbkmk.rb
/usr/share/texmf-dist/scripts/crossrefware/bbl2bib.pl
/usr/share/texmf-dist/scripts/crossrefware/bibdoiadd.pl
/usr/share/texmf-dist/scripts/crossrefware/bibmradd.pl
/usr/share/texmf-dist/scripts/crossrefware/biburl2doi.pl
/usr/share/texmf-dist/scripts/crossrefware/bibzbladd.pl
/usr/share/texmf-dist/scripts/crossrefware/ltx2crossrefxml.pl
/usr/share/texmf-dist/scripts/ctan-o-mat/ctan-o-mat.pl
/usr/share/texmf-dist/scripts/ctanify/ctanify
/usr/share/texmf-dist/scripts/ctanupload/ctanupload.pl
/usr/share/texmf-dist/scripts/de-macro/de-macro
/usr/share/texmf-dist/scripts/diadia/diadia.lua
/usr/share/texmf-dist/scripts/dosepsbin/dosepsbin.pl
/usr/share/texmf-dist/scripts/dtxgen/dtxgen
/usr/share/texmf-dist/scripts/dviasm/dviasm.py
/usr/share/texmf-dist/scripts/dviinfox/dviinfox.pl
/usr/share/texmf-dist/scripts/ebong/ebong.py
/usr/share/texmf-dist/scripts/epspdf/epspdf.tlu
/usr/share/texmf-dist/scripts/epspdf/epspdftk.tcl
/usr/share/texmf-dist/scripts/epstopdf/epstopdf.pl
/usr/share/texmf-dist/scripts/exceltex/exceltex
/usr/share/texmf-dist/scripts/fig4latex/fig4latex
/usr/share/texmf-dist/scripts/findhyph/findhyph
/usr/share/texmf-dist/scripts/fontools/afm2afm
/usr/share/texmf-dist/scripts/fontools/autoinst
/usr/share/texmf-dist/scripts/fontools/ot2kpx
/usr/share/texmf-dist/scripts/fragmaster/fragmaster.pl
/usr/share/texmf-dist/scripts/getmap/getmapdl.lua
/usr/share/texmf-dist/scripts/glossaries/makeglossaries
/usr/share/texmf-dist/scripts/glossaries/makeglossaries-lite.lua
/usr/share/texmf-dist/scripts/installfont/installfont-tl
/usr/share/texmf-dist/scripts/jfmutil/jfmutil.pl
/usr/share/texmf-dist/scripts/kotex-utils/jamo-normalize.pl
/usr/share/texmf-dist/scripts/kotex-utils/komkindex.pl
/usr/share/texmf-dist/scripts/kotex-utils/ttf2kotexfont.pl
/usr/share/texmf-dist/scripts/l3build/l3build.lua
/usr/share/texmf-dist/scripts/latex-git-log/latex-git-log
/usr/share/texmf-dist/scripts/latex-papersize/latex-papersize.py
/usr/share/texmf-dist/scripts/latex2man/latex2man
/usr/share/texmf-dist/scripts/latex2nemeth/latex2nemeth
/usr/share/texmf-dist/scripts/latexdiff/latexdiff-vc.pl
/usr/share/texmf-dist/scripts/latexdiff/latexdiff.pl
/usr/share/texmf-dist/scripts/latexdiff/latexrevise.pl
/usr/share/texmf-dist/scripts/latexfileversion/latexfileversion
/usr/share/texmf-dist/scripts/latexindent/latexindent.pl
/usr/share/texmf-dist/scripts/latexmk/latexmk.pl
/usr/share/texmf-dist/scripts/latexpand/latexpand
/usr/share/texmf-dist/scripts/lilyglyphs/lily-glyph-commands.py
/usr/share/texmf-dist/scripts/lilyglyphs/lily-image-commands.py
/usr/share/texmf-dist/scripts/lilyglyphs/lily-rebuild-pdfs.py
/usr/share/texmf-dist/scripts/listbib/listbib
/usr/share/texmf-dist/scripts/listings-ext/listings-ext.sh
/usr/share/texmf-dist/scripts/ltxfileinfo/ltxfileinfo
/usr/share/texmf-dist/scripts/ltximg/ltximg.pl
/usr/share/texmf-dist/scripts/lua2dox/lua2dox_filter
/usr/share/texmf-dist/scripts/luaotfload/luaotfload-tool.lua
/usr/share/texmf-dist/scripts/lwarp/lwarpmk.lua
/usr/share/texmf-dist/scripts/m-tx/m-tx.lua
/usr/share/texmf-dist/scripts/make4ht/make4ht
/usr/share/texmf-dist/scripts/makedtx/makedtx.pl
/usr/share/texmf-dist/scripts/match_parens/match_parens
/usr/share/texmf-dist/scripts/mathspic/mathspic.pl
/usr/share/texmf-dist/scripts/mf2pt1/mf2pt1.pl
/usr/share/texmf-dist/scripts/mkgrkindex/mkgrkindex
/usr/share/texmf-dist/scripts/mkjobtexmf/mkjobtexmf.pl
/usr/share/texmf-dist/scripts/mkpic/mkpic
/usr/share/texmf-dist/scripts/multibibliography/multibibliography.pl
/usr/share/texmf-dist/scripts/musixtex/musixflx.lua
/usr/share/texmf-dist/scripts/musixtex/musixtex.lua
/usr/share/texmf-dist/scripts/oberdiek/pdfatfi.pl
/usr/share/texmf-dist/scripts/pax/pdfannotextractor.pl
/usr/share/texmf-dist/scripts/pdfbook2/pdfbook2
/usr/share/texmf-dist/scripts/pdfcrop/pdfcrop.pl
/usr/share/texmf-dist/scripts/pdfjam/pdf180
/usr/share/texmf-dist/scripts/pdfjam/pdf270
/usr/share/texmf-dist/scripts/pdfjam/pdf90
/usr/share/texmf-dist/scripts/pdfjam/pdfbook
/usr/share/texmf-dist/scripts/pdfjam/pdfflip
/usr/share/texmf-dist/scripts/pdfjam/pdfjam
/usr/share/texmf-dist/scripts/pdfjam/pdfjam-pocketmod
/usr/share/texmf-dist/scripts/pdfjam/pdfjam-slides3up
/usr/share/texmf-dist/scripts/pdfjam/pdfjam-slides6up
/usr/share/texmf-dist/scripts/pdfjam/pdfjoin
/usr/share/texmf-dist/scripts/pdfjam/pdfnup
/usr/share/texmf-dist/scripts/pdfjam/pdfpun
/usr/share/texmf-dist/scripts/pdflatexpicscale/pdflatexpicscale.pl
/usr/share/texmf-dist/scripts/pdfxup/pdfxup
/usr/share/texmf-dist/scripts/pedigree-perl/pedigree.pl
/usr/share/texmf-dist/scripts/perltex/perltex.pl
/usr/share/texmf-dist/scripts/petri-nets/pn2pdf
/usr/share/texmf-dist/scripts/pfarrei/a5toa4.tlu
/usr/share/texmf-dist/scripts/pfarrei/pfarrei.tlu
/usr/share/texmf-dist/scripts/pkfix-helper/pkfix-helper
/usr/share/texmf-dist/scripts/pkfix/pkfix.pl
/usr/share/texmf-dist/scripts/pmxchords/pmxchords.lua
/usr/share/texmf-dist/scripts/ps2eps/ps2eps.pl
/usr/share/texmf-dist/scripts/pst-pdf/ps4pdf
/usr/share/texmf-dist/scripts/pst2pdf/pst2pdf.pl
/usr/share/texmf-dist/scripts/psutils/extractres.pl
/usr/share/texmf-dist/scripts/psutils/includeres.pl
/usr/share/texmf-dist/scripts/psutils/psjoin.pl
/usr/share/texmf-dist/scripts/ptex-fontmaps/kanji-config-updmap-sys.sh
/usr/share/texmf-dist/scripts/ptex-fontmaps/kanji-config-updmap-user.sh
/usr/share/texmf-dist/scripts/ptex-fontmaps/kanji-config-updmap.pl
/usr/share/texmf-dist/scripts/ptex-fontmaps/kanji-fontmap-creator.pl
/usr/share/texmf-dist/scripts/ptex2pdf/ptex2pdf.lua
/usr/share/texmf-dist/scripts/purifyeps/purifyeps
/usr/share/texmf-dist/scripts/pygmentex/__pycache__/pygmentex.cpython-36.pyc
/usr/share/texmf-dist/scripts/pygmentex/pygmentex.py
/usr/share/texmf-dist/scripts/pythontex/__pycache__/depythontex.cpython-36.pyc
/usr/share/texmf-dist/scripts/pythontex/__pycache__/pythontex.cpython-36.pyc
/usr/share/texmf-dist/scripts/pythontex/depythontex.py
/usr/share/texmf-dist/scripts/pythontex/pythontex.py
/usr/share/texmf-dist/scripts/rubik/rubikrotation.pl
/usr/share/texmf-dist/scripts/simpdftex/simpdftex
/usr/share/texmf-dist/scripts/splitindex/splitindex.pl
/usr/share/texmf-dist/scripts/srcredact/srcredact.pl
/usr/share/texmf-dist/scripts/sty2dtx/sty2dtx.pl
/usr/share/texmf-dist/scripts/svn-multi/svn-multi.pl
/usr/share/texmf-dist/scripts/tex4ebook/tex4ebook
/usr/share/texmf-dist/scripts/tex4ht/ht.sh
/usr/share/texmf-dist/scripts/tex4ht/htcontext.sh
/usr/share/texmf-dist/scripts/tex4ht/htlatex.sh
/usr/share/texmf-dist/scripts/tex4ht/htmex.sh
/usr/share/texmf-dist/scripts/tex4ht/httex.sh
/usr/share/texmf-dist/scripts/tex4ht/httexi.sh
/usr/share/texmf-dist/scripts/tex4ht/htxelatex.sh
/usr/share/texmf-dist/scripts/tex4ht/htxetex.sh
/usr/share/texmf-dist/scripts/tex4ht/mk4ht.pl
/usr/share/texmf-dist/scripts/tex4ht/xhlatex.sh
/usr/share/texmf-dist/scripts/texcount/texcount.pl
/usr/share/texmf-dist/scripts/texdef/texdef.pl
/usr/share/texmf-dist/scripts/texdiff/texdiff
/usr/share/texmf-dist/scripts/texdirflatten/texdirflatten
/usr/share/texmf-dist/scripts/texdoc/texdoc.tlu
/usr/share/texmf-dist/scripts/texdoctk/texdoctk.pl
/usr/share/texmf-dist/scripts/texfot/texfot.pl
/usr/share/texmf-dist/scripts/texlive/allcm.sh
/usr/share/texmf-dist/scripts/texlive/allneeded.sh
/usr/share/texmf-dist/scripts/texlive/dvi2fax.sh
/usr/share/texmf-dist/scripts/texlive/dvired.sh
/usr/share/texmf-dist/scripts/texlive/e2pall.pl
/usr/share/texmf-dist/scripts/texlive/fmtutil-sys.sh
/usr/share/texmf-dist/scripts/texlive/fmtutil-user.sh
/usr/share/texmf-dist/scripts/texlive/fmtutil.pl
/usr/share/texmf-dist/scripts/texlive/fontinst.sh
/usr/share/texmf-dist/scripts/texlive/kpsetool.sh
/usr/share/texmf-dist/scripts/texlive/kpsewhere.sh
/usr/share/texmf-dist/scripts/texlive/ps2frag.sh
/usr/share/texmf-dist/scripts/texlive/pslatex.sh
/usr/share/texmf-dist/scripts/texlive/rubibtex.sh
/usr/share/texmf-dist/scripts/texlive/rumakeindex.sh
/usr/share/texmf-dist/scripts/texlive/rungs.tlu
/usr/share/texmf-dist/scripts/texlive/texconfig-dialog.sh
/usr/share/texmf-dist/scripts/texlive/texconfig-sys.sh
/usr/share/texmf-dist/scripts/texlive/texconfig.sh
/usr/share/texmf-dist/scripts/texlive/texlinks.sh
/usr/share/texmf-dist/scripts/texlive/tlmgr.pl
/usr/share/texmf-dist/scripts/texlive/updmap-sys.sh
/usr/share/texmf-dist/scripts/texlive/updmap-user.sh
/usr/share/texmf-dist/scripts/texlive/updmap.pl
/usr/share/texmf-dist/scripts/texliveonfly/__pycache__/texliveonfly.cpython-36.pyc
/usr/share/texmf-dist/scripts/texliveonfly/texliveonfly.py
/usr/share/texmf-dist/scripts/texloganalyser/texloganalyser
/usr/share/texmf-dist/scripts/texosquery/texosquery-jre5.sh
/usr/share/texmf-dist/scripts/texosquery/texosquery-jre8.sh
/usr/share/texmf-dist/scripts/texosquery/texosquery.sh
/usr/share/texmf-dist/scripts/thumbpdf/thumbpdf.pl
/usr/share/texmf-dist/scripts/tlcockpit/tlcockpit.sh
/usr/share/texmf-dist/scripts/tlshell/tlshell.tcl
/usr/share/texmf-dist/scripts/typeoutfileinfo/typeoutfileinfo.sh
/usr/share/texmf-dist/scripts/ulqda/ulqda.pl
/usr/share/texmf-dist/scripts/urlbst/urlbst
/usr/share/texmf-dist/scripts/vpe/vpe.pl
/usr/share/texmf-dist/scripts/wordcount/wordcount.sh
/usr/share/texmf-dist/scripts/yplan/yplan
/usr/share/texmf-dist/source/fonts/zhmetrics/ttfonts.map
/usr/share/texmf-dist/texconfig/tcfmgr
/usr/share/texmf-dist/texconfig/tcfmgr.map
/usr/share/texmf-dist/ttf2pk/VPS.rpl
/usr/share/texmf-dist/ttf2pk/ttf2pk.cfg
/usr/share/texmf-dist/web2c/fmtutil.cnf
/usr/share/texmf-dist/web2c/mktex.opt
/usr/share/texmf-dist/web2c/mktexdir
/usr/share/texmf-dist/web2c/mktexdir.opt
/usr/share/texmf-dist/web2c/mktexnam
/usr/share/texmf-dist/web2c/mktexnam.opt
/usr/share/texmf-dist/web2c/mktexupd
/usr/share/texmf-dist/web2c/texmf.cnf

%files dev
%defattr(-,root,root,-)
/usr/include/kpathsea/absolute.h
/usr/include/kpathsea/c-auto.h
/usr/include/kpathsea/c-ctype.h
/usr/include/kpathsea/c-dir.h
/usr/include/kpathsea/c-errno.h
/usr/include/kpathsea/c-fopen.h
/usr/include/kpathsea/c-limits.h
/usr/include/kpathsea/c-memstr.h
/usr/include/kpathsea/c-minmax.h
/usr/include/kpathsea/c-namemx.h
/usr/include/kpathsea/c-pathch.h
/usr/include/kpathsea/c-pathmx.h
/usr/include/kpathsea/c-proto.h
/usr/include/kpathsea/c-stat.h
/usr/include/kpathsea/c-std.h
/usr/include/kpathsea/c-unistd.h
/usr/include/kpathsea/cnf.h
/usr/include/kpathsea/concatn.h
/usr/include/kpathsea/config.h
/usr/include/kpathsea/debug.h
/usr/include/kpathsea/expand.h
/usr/include/kpathsea/getopt.h
/usr/include/kpathsea/hash.h
/usr/include/kpathsea/knj.h
/usr/include/kpathsea/kpathsea.h
/usr/include/kpathsea/lib.h
/usr/include/kpathsea/line.h
/usr/include/kpathsea/magstep.h
/usr/include/kpathsea/mingw32.h
/usr/include/kpathsea/paths.h
/usr/include/kpathsea/pathsearch.h
/usr/include/kpathsea/proginit.h
/usr/include/kpathsea/progname.h
/usr/include/kpathsea/readable.h
/usr/include/kpathsea/simpletypes.h
/usr/include/kpathsea/str-list.h
/usr/include/kpathsea/str-llist.h
/usr/include/kpathsea/systypes.h
/usr/include/kpathsea/tex-file.h
/usr/include/kpathsea/tex-glyph.h
/usr/include/kpathsea/tex-hush.h
/usr/include/kpathsea/tex-make.h
/usr/include/kpathsea/types.h
/usr/include/kpathsea/variable.h
/usr/include/kpathsea/version.h
/usr/include/kpathsea/win32lib.h
/usr/include/ptexenc/ptexenc.h
/usr/include/ptexenc/unicode.h
/usr/lib64/pkgconfig/kpathsea.pc
/usr/lib64/pkgconfig/ptexenc.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/afm2pl.1
/usr/share/man/man1/afm2tfm.1
/usr/share/man/man1/allcm.1
/usr/share/man/man1/allec.1
/usr/share/man/man1/allneeded.1
/usr/share/man/man1/autosp.1
/usr/share/man/man1/axohelp.1
/usr/share/man/man1/bbox.1
/usr/share/man/man1/bg5conv.1
/usr/share/man/man1/cef5conv.1
/usr/share/man/man1/cefconv.1
/usr/share/man/man1/cefsconv.1
/usr/share/man/man1/cfftot1.1
/usr/share/man/man1/chktex.1
/usr/share/man/man1/chkweb.1
/usr/share/man/man1/detex.1
/usr/share/man/man1/devnag.1
/usr/share/man/man1/deweb.1
/usr/share/man/man1/disdvi.1
/usr/share/man/man1/dt2dv.1
/usr/share/man/man1/dv2dt.1
/usr/share/man/man1/dvi2fax.1
/usr/share/man/man1/dvi2tty.1
/usr/share/man/man1/dvibook.1
/usr/share/man/man1/dviconcat.1
/usr/share/man/man1/dvidvi.1
/usr/share/man/man1/dvigif.1
/usr/share/man/man1/dvihp.1
/usr/share/man/man1/dvilj.1
/usr/share/man/man1/dvilj2p.1
/usr/share/man/man1/dvilj4.1
/usr/share/man/man1/dvilj4l.1
/usr/share/man/man1/dvilj6.1
/usr/share/man/man1/dvipdfm.1
/usr/share/man/man1/dvipdfmx.1
/usr/share/man/man1/dvipdft.1
/usr/share/man/man1/dvipng.1
/usr/share/man/man1/dvipos.1
/usr/share/man/man1/dvips.1
/usr/share/man/man1/dvired.1
/usr/share/man/man1/dviselect.1
/usr/share/man/man1/dvitodvi.1
/usr/share/man/man1/e2pall.1
/usr/share/man/man1/ebb.1
/usr/share/man/man1/epsffit.1
/usr/share/man/man1/extconv.1
/usr/share/man/man1/extractbb.1
/usr/share/man/man1/extractres.1
/usr/share/man/man1/fmtutil-sys.1
/usr/share/man/man1/fmtutil.1
/usr/share/man/man1/fontinst.1
/usr/share/man/man1/gsftopk.1
/usr/share/man/man1/hbf2gf.1
/usr/share/man/man1/includeres.1
/usr/share/man/man1/kpseaccess.1
/usr/share/man/man1/kpsepath.1
/usr/share/man/man1/kpsereadlink.1
/usr/share/man/man1/kpsestat.1
/usr/share/man/man1/kpsetool.1
/usr/share/man/man1/kpsewhere.1
/usr/share/man/man1/kpsewhich.1
/usr/share/man/man1/kpsexpand.1
/usr/share/man/man1/lacheck.1
/usr/share/man/man1/mag.1
/usr/share/man/man1/makeindex.1
/usr/share/man/man1/makejvf.1
/usr/share/man/man1/mendex.1
/usr/share/man/man1/mkindex.1
/usr/share/man/man1/mktexfmt.1
/usr/share/man/man1/mktexlsr.1
/usr/share/man/man1/mktexmf.1
/usr/share/man/man1/mktexpk.1
/usr/share/man/man1/mktextfm.1
/usr/share/man/man1/mmafm.1
/usr/share/man/man1/mmpfb.1
/usr/share/man/man1/msxlint.1
/usr/share/man/man1/otfinfo.1
/usr/share/man/man1/otftotfm.1
/usr/share/man/man1/pdfclose.1
/usr/share/man/man1/pdfopen.1
/usr/share/man/man1/pfb2pfa.1
/usr/share/man/man1/pk2bm.1
/usr/share/man/man1/pmxab.1
/usr/share/man/man1/prepmx.1
/usr/share/man/man1/ps2eps.1
/usr/share/man/man1/ps2frag.1
/usr/share/man/man1/ps2pk.1
/usr/share/man/man1/psbook.1
/usr/share/man/man1/psjoin.1
/usr/share/man/man1/pslatex.1
/usr/share/man/man1/psnup.1
/usr/share/man/man1/psresize.1
/usr/share/man/man1/psselect.1
/usr/share/man/man1/pstops.1
/usr/share/man/man1/psutils.1
/usr/share/man/man1/rubibtex.1
/usr/share/man/man1/rumakeindex.1
/usr/share/man/man1/scor2prt.1
/usr/share/man/man1/sjisconv.1
/usr/share/man/man1/t1ascii.1
/usr/share/man/man1/t1asm.1
/usr/share/man/man1/t1binary.1
/usr/share/man/man1/t1disasm.1
/usr/share/man/man1/t1dotlessj.1
/usr/share/man/man1/t1lint.1
/usr/share/man/man1/t1mac.1
/usr/share/man/man1/t1rawafm.1
/usr/share/man/man1/t1reencode.1
/usr/share/man/man1/t1testpage.1
/usr/share/man/man1/t1unmac.1
/usr/share/man/man1/tex2aspc.1
/usr/share/man/man1/texconfig-sys.1
/usr/share/man/man1/texconfig.1
/usr/share/man/man1/texdoctk.1
/usr/share/man/man1/texhash.1
/usr/share/man/man1/texlinks.1
/usr/share/man/man1/tpic2pdftex.1
/usr/share/man/man1/ttf2pk.1
/usr/share/man/man1/ttf2tfm.1
/usr/share/man/man1/ttfdump.1
/usr/share/man/man1/ttftotype42.1
/usr/share/man/man1/updmap-sys.1
/usr/share/man/man1/updmap.1
/usr/share/man/man1/vlna.1
/usr/share/man/man1/xdvipdfmx.1
/usr/share/man/man5/fmtutil.cnf.5
/usr/share/man/man5/updmap.cfg.5
