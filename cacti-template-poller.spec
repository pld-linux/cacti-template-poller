%define		template	poller
Summary:	Cacti Poller Statistics
Name:		cacti-template-%{template}
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://forums.cacti.net/download/file.php?id=7501#/ss_poller.php.gz
# Source0-md5:	7afa93ad133fcaf3ea073de4f19d8389
Source1:	http://forums.cacti.net/download/file.php?id=7502#/cacti_host_template_local_cacti_polling_host.xml
# Source1-md5:	3f54a6579f06745426163685facac558
Patch0:		config.patch
URL:		http://forums.cacti.net/viewtopic.php?f=12&t=18057
BuildRequires:	rpmbuild(macros) >= 1.554
BuildRequires:	sed >= 4.0
Requires:	cacti >= 0.8.7e-8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
Cacti Poller Statistics.

%prep
%setup -qcT
gzip -dc %{SOURCE0} > ss_poller.php
cp -a %{SOURCE1} .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
cp -a ss_poller.php $RPM_BUILD_ROOT%{scriptsdir}
cp -a *.xml $RPM_BUILD_ROOT%{resourcedir}

%post
%cacti_import_template %{resourcedir}/cacti_host_template_local_cacti_polling_host.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{scriptsdir}/ss_poller.php
%{resourcedir}/*.xml
