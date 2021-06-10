#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :Propósito:     Manejador de Bunch
    :Autor:         David Schoonover
    :web:           https://github.com/dsc/bunch
    :Adaptación:    Tony Diana
    :Versión:       21.06.10

    ---------------------------------------------------------------------------
"""

from .kernel import _Bunch as Bunch

# --- Evitar flake8 F401
aux = Bunch
aux = None
del aux
