%global commit 0fcf944ab5b8903249d888230ef2e68e83286256
%global commit_date 20211110

Name:	        qdl
Version:        %{commit_date}
Release:        2%{?dist}
Summary:        Tool to communicate with USB devices of id 05c6:9008 to upload a flash loader and use this to flash images
License:        BSD-3-Clause
URL:            https://github.com/andersson/qdl
Source0:        https://github.com/andersson/qdl/archive/%{commit}/qdl-%{commit}.tar.gz
BuildRequires:  gcc
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml-2.0)

%description
This tool communicates with USB devices of id 05c6:9008 to upload a flash
loader and use this to flash images

%prep
%autosetup -n qdl-%{commit}

%build
%make_build

%install
%make_install prefix="%{_prefix}"

%files
%license LICENSE
%doc README
%{_bindir}/%{name}

%changelog
* Sat Mar 19 2022 Mustafa Çalışkan <muscaln@protonmail.com> - 20211110-2
- Initial package


