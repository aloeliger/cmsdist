### RPM external OpenBLAS 0.2.19
Source: https://github.com/xianyi/OpenBLAS/archive/v%{realversion}.tar.gz

%prep
%setup -n %{n}-%{realversion}

%build

make %{makeprocesses} FC=gfortran BINARY=64 

%install
make install PREFIX=%i
