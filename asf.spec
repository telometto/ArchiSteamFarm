Name:           ArchiSteamFarm
Version:        0.1.1

# Release start
Release:        1%{?dist}
# Release end

Summary:        "C# application with primary purpose of farming Steam cards from multiple accounts simultaneously."
Group:          Applications/System
License:        "Apache-2.0"
URL:            https://github.com/JustArchiNET/ArchiSteamFarm/archive/refs/heads
Source0:        main.zip
BuildRequires:  ca-certificates glibc libgcc libicu krb5-libs openssl-libs libstdc++ zlib git

%description
%{summary}

%prep
# Nothing to do.

%build
# Nothing to do.

%install
cd $HOME
git clone https://github.com/JustArchiNET/ArchiSteamFarm.git
cd ArchiSteamFarm
chmod +x ArchiSteamFarm

%clean
# Nothing to do.

%files
%{_bindir}/%{name}

%changelog
* Sat May 7 2022 telometto - 0.1.1
- First version: 0.1.1.
