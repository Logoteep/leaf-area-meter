[app]
title = Leaf Area Meter
package.name = leafareameter
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3==3.11.11, hostpython3==3.11.11, kivy==2.3.0, camera4kivy, gestalt, pillow, pyjnius

orientation = portrait
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.api = 34
android.minapi = 24
android.ndk = 25c
android.features = android.hardware.camera, android.hardware.camera.autofocus

p4a.branch = develop
p4a.hook = camerax_provider/gradle_options.py
