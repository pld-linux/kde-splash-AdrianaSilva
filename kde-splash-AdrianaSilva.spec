
%define		_splash		AdrianaSilva

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	01
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://www.kde-look.org/content/files/20476-AdrianaSilva.tar.gz	
# Source0-md5:	2765b751fd99712aad4614e70eceb9fc
URL:		http://www.kde-look.org/content/show.php?content=20476
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"AdrianaSilva" is a splash screen and contains a nice photo of Adriana Silva

%description -l pl
Ekran startowy KDE "AdrianaSilva" zawiera ca³kiem mi³y obrazek Adriany Silvy

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

install %{_splash}/*.png $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install %{_splash}/Theme.rc $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
