Summary:	yconsole - monitors & controls the Y sound server
Summary(pl.UTF-8):	yconsole - monitorowanie i sterowanie serwerem dźwięku Y
Name:		yconsole
Version:	3.4.6
Release:	2
License:	GPL-like
Group:		Applications/Sound
Source0:	http://wolfsinger.com/~wolfpack/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	923ddfedd38efa41a408d93ee6bd78ac
URL:		http://freecode.com/projects/yconsole
BuildRequires:	gtk+-devel >= 1.2.10
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	yiff-devel >= 2.14
Requires:	gtk+ >= 1.2.10
Requires:	yiff-lib >= 2.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YConsole monitors the status of the Y sound server and allows
modification of its Audio and Mixer values. It also features yplayer
which allows you to play sound objects and audio CDs.

%description -l pl.UTF-8
YConsole monitoruje stan serwera dźwięku Y i pozwala na modyfikowanie
jego wartości dźwięku i miksera. Ma także yplayer, który pozwala
odtwarzać obiekty dźwiękowe i płyty CD-Audio.

%prep
%setup -q

%build
%{__make} -C yconsole \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall `imlib-config --cflags` -DHAVE_IMLIB `gtk-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C yconsole install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	ICONS_DIR=$RPM_BUILD_ROOT%{_pixmapsdir}

# conflicts with yplayer, but may be useful for some desktop in future...
%{__rm} $RPM_BUILD_ROOT%{_pixmapsdir}/yplayer.xpm

bzip2 -d $RPM_BUILD_ROOT%{_mandir}/man1/*.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/yconsole
%{_datadir}/yconsole
%{_pixmapsdir}/yconsole.xpm
%{_pixmapsdir}/ymidi.xpm
%{_pixmapsdir}/ymixer.xpm
%{_mandir}/man1/yconsole.1*
