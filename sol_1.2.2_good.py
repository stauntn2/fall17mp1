#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib as url

a = "I come in peace."
b = "Prepare to be destroyed!"
decision = url.quote("""
                                      9qۆ�F�s^h.����ֽ_�~�M&
�V��˂6��'���Q�qE�����|'N��r\\�}g�"�J��q>�n�A��=~��\ٻ�TiY�s�_�\�q4�p��8�K�(|	�k�l@�.\�X""")
result = ord(decision[119])
if result % 2 == 1:
    print(a)
else:
    print(b)