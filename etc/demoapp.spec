Summary: Demo App
Name: @@PACKAGE_NAME@@
Version: @@VERSION@@
Release: @@BUILD@@
License: Copyright by Ladislav Prskavec
Group: System Environment/Internet
BuildRoot: @@BUILDROOT@@

#topdir
%define _topdir @@TOPDIR@@
%define _target_os Linux

%description
Barcamp 2010 demo app

%install
mkdir -p $RPM_BUILD_ROOT/srv/www/demoApp/@@CURRENT@@
cp -r ${FILENAME}-${VERSION}/* $RPM_BUILD_ROOT/srv/www/demoApp/@@CURRENT@@/

%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}


%files 
/srv/www/demoApp/@@CURRENT@@

%defattr(755,root,root)
%dir /srv/
%dir /srv/www
%dir /srv/www/demoApp/
%dir /srv/www/demoApp/@@CURRENT@@/

%post
echo "run: ln -nfs /srv/www/demoApp/@@CURRENT@@/ /srv/www/demoApp/current"
