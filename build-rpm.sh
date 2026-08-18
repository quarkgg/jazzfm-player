#!/bin/sh
# Build the jazzfm-player RPM: stages a versioned source tarball, then rpmbuild.
set -e
cd "$(dirname "$0")"

name=jazzfm-player
version=0.1.0
topdir=${RPMBUILD_TOPDIR:-$HOME/rpmbuild}

mkdir -p "$topdir/SOURCES"
stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT
mkdir "$stage/$name-$version"
cp -r jazzfm_player logo.png "$name" "$name.desktop" "$stage/$name-$version/"
find "$stage" -type d -name __pycache__ -prune -exec rm -rf {} +
tar -C "$stage" -cf "$topdir/SOURCES/$name-$version.tar" "$name-$version"

rpmbuild -bb --define "_topdir $topdir" "$name.spec"
echo "Built: $topdir/RPMS/noarch/$name-$version-*.noarch.rpm"
