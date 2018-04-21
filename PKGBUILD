# Script generated with Bloom
pkgdesc="ROS - Converts a 3D Point Cloud into a 2D laser scan. This is useful for making devices like the Kinect appear like a laser scanner for 2D-based algorithms (e.g. laser-based SLAM)."
url='http://ros.org/wiki/perception_pcl'

pkgname='ros-lunar-pointcloud-to-laserscan'
pkgver='1.4.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-message-filters'
'ros-lunar-nodelet'
'ros-lunar-roscpp'
'ros-lunar-roslint'
'ros-lunar-sensor-msgs'
'ros-lunar-tf2'
'ros-lunar-tf2-ros'
'ros-lunar-tf2-sensor-msgs'
)

depends=('ros-lunar-message-filters'
'ros-lunar-nodelet'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
'ros-lunar-tf2'
'ros-lunar-tf2-ros'
'ros-lunar-tf2-sensor-msgs'
)

conflicts=()
replaces=()

_dir=pointcloud_to_laserscan
source=()
md5sums=()

prepare() {
    cp -R $startdir/pointcloud_to_laserscan $srcdir/pointcloud_to_laserscan
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

