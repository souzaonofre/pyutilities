# -*- coding: utf-8 -*-
#
import sys
import string
import re
import unicodedata
import types

GOOD_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)
#
REXPTYPE = re.compile(r'')
#
BAD_CHARS_REXP = re.compile(r'[^A-Za-z0-9_. ]+|^\.|\.$|^ | $|^$')
BAD_NAMES_REXP = re.compile(r'(aux|com[1-9]|con|lpt[1-9]|prn)(\.|$)')
#
# decimal character reference
DECIMAL_REXP = re.compile('&#(\d+);')
#
# hexadecimal character reference
HEX_REXP = re.compile('&#x([\da-fA-F]+);')
#
#

def _unicode_normalize(filename):
	# text to unicode
	if type(filename) != types.UnicodeType:
		filename = unicode(filename, 'utf-8', 'ignore')
	#----------------------------
	return unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore')

#
def _clean_fname_by_good_chars(fname):
	return ''.join(c for c in fname if c in GOOD_CHARS)

#
def _clean_fname_by_rexp(fname, rexp, repl=''):
	if type(rexp) != REXPTYPE:
		return fname
	elif rm_by_rexp == re.compile(rexp):
		return rm_by_rexp.sub(repl,fname)
	else:
		return fname
#
def _clean_fname_by_dup_char(fname, char=''):
	dchar = "%s%s" % char,char
	while  dchar in fname:
		fname = fname.sub(dchar,char)
	return fname

#
def make_new_fname(fname):
	new_fname = _unicode_normalize(fname)
	new_fname = _clean_fname_by_good_chars(new_fname)
	return new_fname

#
#
if __name__ == '__main__':

	if not sys.argv[1]:
		print >>sys.stderr, USAGE
		sys.exit(1)
	#----------------------------
	old_fname = sys.argv[1]
	new_fname = make_new_fname(old_fname)
	print repr(new_fname)

