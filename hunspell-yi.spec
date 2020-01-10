Name: hunspell-yi
Summary: Yiddish hunspell dictionaries
Version: 1.1
Release: 6%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/e-files/3975/1/%{name}-%{version}.oxt
URL: http://extensions.services.openoffice.org/en/project/dict-yi
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+ or GPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Yiddish hunspell dictionaries.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/yi.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/yi_US.aff
cp -p dictionaries/yi.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/yi_US.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc gpl-2.0.txt MPL-1.1.txt README_yi.txt LICENSES-en.txt HACKING lgpl-2.1.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 13 2010 Caolán McNamara <caolanm@redhat.com> - 1.1-2
- Resolves: rhbz#624045 Change URL to point to static project info url

* Sat May 01 2010 Caolán McNamara <caolanm@redhat.com> - 1.1-1
- initial version
