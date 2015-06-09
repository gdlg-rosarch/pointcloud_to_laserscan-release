Name:           ros-indigo-pointcloud-to-laserscan
Version:        1.3.0
Release:        0%{?dist}
Summary:        ROS pointcloud_to_laserscan package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/perception_pcl
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-filters
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf2
Requires:       ros-indigo-tf2-ros
Requires:       ros-indigo-tf2-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-ros
BuildRequires:  ros-indigo-tf2-sensor-msgs

%description
Converts a 3D Point Cloud into a 2D laser scan. This is useful for making
devices like the Kinect appear like a laser scanner for 2D-based algorithms
(e.g. laser-based SLAM).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jun 09 2015 Paul Bovbel <paul@bovbel.com> - 1.3.0-0
- Autogenerated by Bloom

