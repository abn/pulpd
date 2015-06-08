%define debug_package %{nil}
%define pulpd_home /var/lib/pulpd
%define pulpd_data %{pulpd_home}/data

Name:       pulpd	
Version:	0.1
Release:	1%{?dist}
Summary:	Pulp'd - Pulp in a box

License:	GPLv2
URL:		https://github.com/abn/pulpd
Source0:    pulpd
Source1:    pulpd.conf

Requires:	bash, docker, util-linux, coreutils

%description
Pulp'd aims to provide an easier way to deploy multi-container pulp. This extends on the great work done by the pulp maintainers working on Pulp Docker Packaging.

%install
install -d %{buildroot}/%{_bindir}
install %{SOURCE0} %{buildroot}/%{_bindir}

install -d %{buildroot}/%{_sysconfdir}
install %{SOURCE1} %{buildroot}/%{_sysconfdir}

%pre
install -d -m 750 -o root -g root %{pulpd_data}
chcon -Rt svirt_sandbox_file_t %{pulpd_data}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/pulpd
%attr(755, root, root) %{_sysconfdir}/pulpd.conf

%doc

%changelog
* Mon Jun 08 2015 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.1-1
- Initial release

