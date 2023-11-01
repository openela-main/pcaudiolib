Name:           pcaudiolib
Version:        1.1
Release:        9%{?dist}
Summary:        Portable C Audio Library

# pcaudiolib bundles TPCircularBuffer with Cube license, which is only used
# by coreaudio support, which we do not build. The rest is GPLv3+.
License:        GPLv3+
URL:            https://github.com/rhdunn/pcaudiolib
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  gcc make autoconf automake libtool pkgconfig
BuildRequires:  alsa-lib-devel pulseaudio-libs-devel

%description
The Portable C Audio Library (pcaudiolib) provides a C API to different
audio devices.

%package devel
Summary: Development files for pcaudiolib
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the Portable C Audio Library.

%prep
%autosetup
rm -rf src/TPCircularBuffer

%build
./autogen.sh
%configure --without-coreaudio
%make_build

%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%doc AUTHORS
%doc CHANGELOG.md
%{_libdir}/libpcaudio.so.*

%files devel
%{_libdir}/libpcaudio.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/audio.h

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.1-9
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.1-8
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Ondřej Lysoněk <olysonek@redhat.com> - 1.1-2
- Clarify licensing, make sure we don't build TPCircularBuffer

* Sat Mar 24 2018 Ondřej Lysoněk <olysonek@redhat.com> - 1.1-1
- New version
- Resolves: rhbz#1549559

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Ondřej Lysoněk <olysonek@redhat.com> - 1.0-3
- Made the pcaudiolib-devel Requires arch-specific

* Thu Sep 22 2016 Ondřej Lysoněk <olysonek@redhat.com> - 1.0-2
- Own the /usr/include/pcaudiolib directory

* Fri Sep 16 2016 Ondřej Lysoněk <olysonek@redhat.com> 1.0-1
- Initial package
