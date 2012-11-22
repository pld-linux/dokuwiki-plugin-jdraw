%define		plugin		jdraw
Summary:	DokuWiki jDraw Plugin
Summary(pl.UTF-8):	Wtyczka jDraw dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20120209
Release:	0.1
License:	distributable, non-comercial use
Group:		Applications/WWW
Source0:	http://www.hammurapi.com/products/jdraw/jdraw.zip
# Source0-md5:	cd58b88a64cf5fdaca063961475d45dc
URL:		https://www.dokuwiki.org/plugin:jdraw
Requires:	dokuwiki >= 20110525
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Create and edit diagrams in the browser using a Java Applet. The
plug-in also features off-line diagram editor.

%prep
%setup -q -n %{plugin}
version=$(find . -printf '%%TY%%Tm%%Td\n' | sort | tail -n 1)
if [ "$version" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%doc license.txt
%{plugindir}
