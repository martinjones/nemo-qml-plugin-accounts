# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       nemo-qml-plugin-accounts-qt5

# >> macros
# << macros

Summary:    Accounts plugin for Nemo Mobile
Version:    0.0.0
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugin-accounts
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-qml-plugin-accounts-qt5.yaml
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(accounts-qt5)

%description
%{summary}.

%package tests
Summary:    QML accounts plugin tests
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/org/nemomobile/accounts/libnemoaccounts.so
%{_libdir}/qt5/qml/org/nemomobile/accounts/qmldir
# >> files
# << files

%files tests
%defattr(-,root,root,-)
/opt/tests/nemo-qml-plugins-qt5/accounts/*
%{_datadir}/accounts/providers/test-provider.provider
%{_datadir}/accounts/services/test-service2.service
%{_datadir}/accounts/service_types/test-service-type2.service-type
# >> files tests
# << files tests
