Summary:	Share keyboard and mouse between computers
Name:		quicksynergy
Version:	0.8.1
Release:	1
License:	GPL v2+
Group:		Applications/System
URL:		http://quicksynergy.sourceforge.net
Source0:	http://downloads.sourceforge.net/quicksynergy/%{name}-%{version}.tar.gz
# Source0-md5:	2f8b915dfcce7134eb10444217fb6d8d
Source1:	%{name}.desktop
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gtk+2-devel >= 2:2.10
Requires:	synergy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QuickSynergy is a graphical interface (GUI) for easily configuring
Synergy, an application that allows the user to share his mouse and
keyboard between two or more computers.

%prep
%setup -q

%build
%configure \
	SYNERGYS=%{_bindir}/synergys \
	SYNERGYC=%{_bindir}/synergyc \
	%{nil}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p src/logo/qslogo.png $RPM_BUILD_ROOT%{_pixmapsdir}

desktop-file-install --dir=$RPM_BUILD_ROOT%{_desktopdir} %{SOURCE1}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog COPYING AUTHORS README
%attr(755,root,root) %{_bindir}/%{name}
%{_pixmapsdir}/qslogo.png
%{_desktopdir}/%{name}.desktop
