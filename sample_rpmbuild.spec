Name:	SpringMVCLearningSpike	
Version:  1.0
Release:  0
Summary:  SpringMVCLearningSpike	

Group:	Applications/Multimedia
License: GPL	
URL:		http://www.google.co.uk 
Source0:   %{name}-%{version}.tar

#BuildRequires: n/a	
#Requires:      

%description


%prep

%build


%install
rm -rf rm -rf %{buildroot}
mkdir -p  %{buildroot}/usr/local/bin
cp SpringMVCLearningSpike.war %{buildroot}/usr/local/bin


%files
%doc
%attr(0750,root,root)//usr/local/bin/%{name}.war

%changelog

