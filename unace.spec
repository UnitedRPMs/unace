%define debug_package %{nil}

Summary:        A tool to extract ace archives
Name:           unace
Version:        2.5
Release:        1%{?dist}
License:        Redistributable, no modification permitted
Group:          Applications/Archiving
URL:            http://www.winace.com/
Source0:        http://ftp.debian.org/debian/pool/non-free/u/unace-nonfree/unace-nonfree_%{version}.orig.tar.gz
Patch0:		01-makefiles.patch
Patch1:		04-64bit.patch
BuildRequires:	ncurses-devel

%description
unace is a command line utility to extract, view, and test the
contents of an ACE archive.


%prep
%setup -n %{name}-%{version}
patch -p1 < %{_sourcedir}/01-makefiles.patch

%ifarch x86_64
%patch1 -p1 
%endif

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
install -m 0755 %{name} $RPM_BUILD_ROOT/%{_bindir}/
install -D -m644 licence $RPM_BUILD_ROOT/%{_datadir}/licenses/unace/license


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_datadir}/licenses/unace/license
%{_bindir}/%{name}


%changelog

* Wed Feb 15 2017 david va <davidva AT tutanota DOT com> 2.5-1
- Initial build.
