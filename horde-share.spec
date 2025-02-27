%define prj     Horde_Share

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:		horde-share
Version:	0.0.3
Release:	5
Summary:	Horde Browser package
License:	LGPL
Group:		Networking/Mail
Url:		https://pear.horde.org/index.php?package=%{prj}
Source0:	%{prj}-%{version}.tgz
BuildArch:	noarch
Requires(pre):  php-pear
Requires:	horde-framework
Requires:	horde-util
Requires:	php-pear-channel-horde
BuildRequires:	php-pear
BuildRequires:	php-pear-channel-horde


%description
The Horde_Browser:: class provides an API for getting information about
the current user's browser and its capabilities.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde
%{peardir}/Horde/Share.php




%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-4mdv2011.0
+ Revision: 564100
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-3mdv2010.1
+ Revision: 524854
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased rel ver to 2

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-2mdv2010.1
+ Revision: 509385
- line Requires(pre) added missing %%{_bindir}/pear
- increase rel version

* Tue Feb 16 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-1mdv2010.1
+ Revision: 506425
- import horde-share


