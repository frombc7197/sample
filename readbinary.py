#!/usr/bin/python
# -*- coding: cp949 -*-

import sys


# ���ϸ��� �������� ������ ���� ����ϰ� ����
if len(sys.argv) is 1:
  print >> sys.stderr, '���� ���ϸ��� �Է��� �ּ���'
  exit(1)




# ����� �ɼ����� ������ ���ϸ� ���
fname = sys.argv[1]



# ���� ������, �� ����Ʈ�� �о ȭ�鿡 16������ ����ϱ�
try:
  FH = open(fname, 'rb')  # ���� ����

  while True:
    s = FH.read(1)
    if s == '': break
    print("%02X", int(ord(s)))  # 1����Ʈ�� ���


  FH.close()  # ���� �ݱ�
except IOError:
  print >> sys.stderr, '������ �� �� �����ϴ�.'
