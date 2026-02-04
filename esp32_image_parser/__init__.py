"""ESP32 Image Parser - Tools for parsing and analyzing ESP32 firmware images."""

__version__ = "0.1.0"

from .esp32_firmware_reader import (
    read_partition_table,
    print_verbose,
    PART_TYPES,
    PART_SUBTYPES_APP,
    PART_SUBTYPES_DATA,
)
from .read_nvs import read_nvs_pages
from .cli import main, image2elf

__all__ = [
    "read_partition_table",
    "print_verbose",
    "PART_TYPES",
    "PART_SUBTYPES_APP",
    "PART_SUBTYPES_DATA",
    "read_nvs_pages",
    "main",
    "image2elf",
]
