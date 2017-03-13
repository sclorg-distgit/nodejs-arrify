%{?scl:%scl_package nodejs-%{srcname}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# Circular dependency on ava
%global enable_tests 0
%global srcname arrify

%global commit0 4576e944677c722c356480b17a6d709d34d0733c
%global gittag0 v1.0.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           %{?scl_prefix}nodejs-%{srcname}
Version:        1.0.0
Release:        9%{?dist}
Summary:        Convert a value to an array
License:        MIT
URL:            https://www.npmjs.com/package/%{srcname}
Source0:        https://github.com/sindresorhus/%{srcname}/archive/%{commit0}.tar.gz#/%{srcname}-%{shortcommit0}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(ava)
%endif

%description
%{summary}.

%prep
%setup -n %{pkg_name}-%{version} -qn %{srcname}-%{commit0}
rm -rf node_modules/

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr index.js package.json \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
node test.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%doc license
%{nodejs_sitelib}/%{srcname}

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-9
- Clean up

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-8
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-7
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-6
- Invoke find_provides_and_requires macro

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-5
- Enable find provides and requires macro

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-4
- Enable find provides and requires macro

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Enable scl macros

* Sat Oct 17 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.0-1
- Initial package
