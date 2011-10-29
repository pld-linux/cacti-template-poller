%define		template	poller
Summary:	Cacti Poller Statistics
Name:		cacti-template-%{template}
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/usertemplate:host:cacti:poller_stats3.tgz
# Source0-md5:	8d994fa7c8bfc9e1e8b7e9d11788b8e9
URL:		http://docs.cacti.net/usertemplate:host:cacti:poller
BuildRequires:	rpmbuild(macros) >= 1.554
BuildRequires:	sed >= 4.0
Requires:	cacti >= 0.8.7g
Obsoletes:	cacti-addons-Cacti_Poller_Statistics
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
Variety of Graphs for Cacti Poller/Boost Performance.

%prep
%setup -qc

# sane filename, we use it in post
mv cacti{087g,}_host_template_cacti_polling_host.xml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
install -p ss_poller.php $RPM_BUILD_ROOT%{scriptsdir}
cp -p *.xml $RPM_BUILD_ROOT%{resourcedir}

%post
%cacti_import_template %{resourcedir}/cacti_host_template_cacti_polling_host.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{scriptsdir}/ss_poller.php
%{resourcedir}/*.xml
