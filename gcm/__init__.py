#!/usr/bin/env python
import sys

""" GCM implementation in python"""

version = "0.1.4"
version_info = (0, 1, 4, 0)

if sys.version_info < (3, 0):
    import gcm

    GCM = gcm.GCM
else:
    import gcm
    from gcm.gcm import GCM
