#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'vendor/lib/hw/camera.sdm660.so': blob_fixup()
        .add_needed('libcamera_sdm660_shim.so'),
    'vendor/lib/libMiWatermark.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'tulip',
    'xiaomi',
    blob_fixups=blob_fixups,
    check_elf=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sdm660-common', module.vendor
    )
    utils.run()
