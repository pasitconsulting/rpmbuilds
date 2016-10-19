Name:   SpringMVCLearningSpike
Version: 39
Release:  0
Summary:  SpringMVCLearningSpike

Group:  Applications/Multimedia
License: GPL
URL:            http://www.google.co.uk
Source0:   %{name}-%{version}.tar

Requires: java-1.7.0-openjdk
Requires: tomcat
#Requires:      

%description


%prep

%build


%install
rm -rf rm -rf %{buildroot}
mkdir -p  %{buildroot}/usr/local/bin
cp SpringMVCLearningSpike.war %{buildroot}/usr/local/bin
sudo yum-builddep /var/lib/jenkins/rpmbuild/SPECS/SpringMVCLearningSpike.spec

%files
%doc
%attr(0750,root,root)//usr/local/bin/%{name}.war

%changelog
