# (OPEN) :Transcludes\: 6
# (GOTO) :lib:file\:///C\:/run/code/Transcluder/lib.py

import time
from contextlib import contextmanager
from pathlib import Path
from traceback import format_exc

# (OPEN) :Path
# Imports the often used pathlib.Path
# (CLOSE)
# (OPEN) :contents
def contents(path, *args, encoding='utf-8', **kwargs):
	with path.open('r', *args, encoding=encoding, **kwargs) as f:
		return f.read()
# (CLOSE)
# (OPEN) :realpath
def realpath(path_string):
	return Path (path_string).resolve(strict=True)
# (CLOSE)
# (OPEN) :set_contents
def set_contents(path, string, *args, encoding='utf-8', **kwargs):
	with path.open('w', *args, encoding=encoding, **kwargs) as f:
		f.write(string)
# (CLOSE)
# (OPEN) :sleep
def sleep(secs):
	time.sleep(secs)
# (CLOSE)
# (OPEN) :stay_open, stay_open_on_error
def init():
	stays_open = False

	# (OPEN) :stay_open()
	def stay_open():
	
		'''
		Like stay_open_on_error, but manually tells the commandline window to stay
		open.
		'''
	
		nonlocal stays_open
		stays_open = True
	# (CLOSE)
	# (OPEN) :stay_open_on_error()
	@contextmanager
	def stay_open_on_error():
	
		'''
		usage:
	
			with stay_open_on_error():
				# do stuff. If it raises the commandline window will stay open.
	
		This is useful for scripts which are called via clicking the script in the
		explorer or via executing it by pressing an assigned button or keyboard
		shortcut.
	
		Syntax errors are unfortunately not catched.
		'''
	
		nonlocal stays_open
	
		try:
			yield
	
		except SystemExit:
			print('System Exit')
			stays_open = True
	
		except: # noqa
			print(format_exc())
			stays_open = True
	
		if stays_open:
			input('Press key to close')
	# (CLOSE)

	return stay_open, stay_open_on_error

stay_open, stay_open_on_error = init()
# (CLOSE)
# (CLOSE)

# (NOTE) This script normalizes a static wiki for diffing. The idea is to have
# (NOTE) the diff view only show the differences we want to catch and ignore
# (NOTE) irrelevant differences. I use it to compare static wikis generated
# (NOTE) from different branches. This file was created with a modified version
# (NOTE) of the Code Browser, https://github.com/heronils/Code_Browser_49

with stay_open_on_error ():

# (NOTE) 	https://pypi.org/project/regex/, 'pip install regex'
	import regex

	master_static = 'masterbranch static.html'
	feature_static = 'featurebranch static.html'

# (NOTE) 	My PR removes so many of these invalid p's that the diff
# (NOTE) 	becomes unreadable. So i remove them from the masterbranch
# (NOTE) 	static export. Set to true to see these changes. BTW, the
# (NOTE) 	normalized featurebranch static export is nearly HTML 5
# (NOTE) 	conform, with some things to do left, which are subject
# (NOTE) 	of other PR's (for example a's wrapping elements which
# (NOTE) 	contain other a's, a div containing styles inside of the
# (NOTE) 	head)
	show_invalid_ps_in_master = False

# (NOTE) 	Currently, `True` will result in both files having the same
# (NOTE) 	amount of lines, and they can then be compared using the
# (NOTE) 	`log differences.py`
	line_by_line_comparable = False

	def norm(path):
		print(f'Normalizing {path} ...')

		is_feature = 'featurebranch' in path

		text = contents (realpath (path))

		# (OPEN) :def _regex_sub_verbose()
		def _regex_sub_verbose(pattern, replacement, flags=0):
			nonlocal text
			flags = flags | regex.VERBOSE
			text = regex.sub(pattern, replacement, text, flags=flags)
		# (CLOSE)
		# (OPEN) :def replace()
		def replace(description, pattern, replacement, flags=0):
			print(f"  {description}")
			_regex_sub_verbose(pattern, replacement, flags)
		# (CLOSE)
		# (OPEN) :def remove()
		def remove(description, pattern, flags=0):
			replace(f'Remove {description}', pattern, '', flags)
		# (CLOSE)

		# (OPEN) :Big elements
		remove('<style>...</style>',
			r'<style \s .+? </style>', regex.DOTALL
		)
		
		remove('<script>...</script>',
			r'<script \s .+? </script>', regex.DOTALL
		)
		
		remove('<svg>...</svg>',
			r'<svg \s .+? </svg>' , regex.DOTALL
		)
		# (CLOSE)
		# (OPEN) :Attributes
		remove('"..." attributes',
			r'''
			\s+ [$a-zA-Z] (?: -? [a-zA-Z0-9]+ )* (*PRUNE)
			\s* = \s* (*PRUNE)
			" [^"]* " (*PRUNE)
			'''
		)
		# (CLOSE)
		# (OPEN) :Attributes (escaped html)
		remove('"..." attributes from escaped html',
			r'''
				\s+ [$a-zA-Z] (?: -? [a-zA-Z0-9]+ )*	(*PRUNE)
				\s* = \s*	(*PRUNE)
				&quot; (?!&quot;) .*? (?<!&quot;) &quot; (?!&quot;)	(*PRUNE)
			''',regex.DOTALL
		)
		
		remove('"" attributes from escaped html',
			r'''
				\s+ [$a-zA-Z] (?: -? [a-zA-Z0-9]+ )*	(*PRUNE)
				\s* = \s*	(*PRUNE)
				&quot; \s* &quot; (?!&quot;)	(*PRUNE)
			''', regex.DOTALL
		)
		
		# (CLOSE)
		# (OPEN) :Linebreak escapers
		if is_feature:
			remove('linebreak escapers from escaped html (only featurebranch)',
				r'(?<=&gt;)\\(?=\n)'
			)
		# (CLOSE)
		# (OPEN) :Remove empty p´s
		# (NOTE) Those get eg. created by the navigator widget in the Tiddler
		# (NOTE) 'Creating SubStories'.
		
		if line_by_line_comparable or not is_feature:
			only_masterbranch = '' if line_by_line_comparable else ' (only masterbranch)'
			remove(f'empty p´s{only_masterbranch}',
				r'<p> \s* </p>'
			)
		# (CLOSE)
		# (OPEN) :Remove invalid p´s wrapping blockelements from the masterbranch wiki
		if not line_by_line_comparable and not show_invalid_ps_in_master and not is_feature:
		
		# (NOTE) 	We can not do this using regexes because eg it will not catch (but
		# (NOTE) 	should) ...
		# (NOTE) 		<p>
		# (NOTE) 		<a ...></a>
		# (NOTE) 		<div></div>
		# (NOTE) 		</p>
		# (NOTE) 	... so instead we use a mini parser.
		
			print('  Remove p´s we dont want from masterbranch wiki')
		
			blockelems = (
				'(?:div|ul|ol|dl|table|tr|td|h[1-6]|p|pre|style|blockquote)'
			)
			cleaned = ['']
			p_locations = [0]
			# (OPEN) :pat
			pat = regex.compile(r'''
			
				(<\s*!\s*doctype\s+html\s*>)	# doctype – doctype tag
				|
				(<''' + blockelems + r'''>)	# O - blockelement opener
				|
				(</''' + blockelems + r'''>)	# C - blockelement closer
				|
				(<''' + blockelems + r'''\s*/>)	# S - self closing blockelement
				|
				(<img>)	# v - void element,
				|
				(<[^<>\s]+>)	# o - inline element opener
				|
				(</[^<>\s]+>)	# c - inline element closer
				|
				(<[^<>\s]+\s*/>)	# s - self closing inline element
				|
				([^<>]+)	# other - not a tag
				|
				([<>])	# error - this should not happen
			''', regex.VERBOSE)
			# (CLOSE)
			# (OPEN) :handler
			def handler(match):
				nonlocal cleaned, p_locations
			
				# See description in the pattern definition
				doctype, O, C, S, v, o, c, s, other, error = match.groups()
			
				if O is not None:
					cleaned.append(O)
					cleaned[p_locations[-1]] = ''
					if O == '<p>':
						p_locations.append(len(cleaned)-1)
			
				elif C is not None:
					if C == '</p>':
						if cleaned[p_locations[-1]]:
							cleaned.append(C)
						p_locations.pop()
					else:
						cleaned.append(C)
			
				elif S is not None:
					cleaned[p_locations[-1]] = ''
					cleaned.append(S)
			
				elif v is not None: cleaned.append(v)
			
				elif error is not None:
					raise Exception(error)
			
				elif doctype is not None: cleaned.append(doctype)
				elif o is not None: cleaned.append(o)
				elif c is not None: cleaned.append(c)
				elif s is not None: cleaned.append(s)
				elif other is not None: cleaned.append(other)
			
				return match[0]
			# (CLOSE)
			pat.sub(handler, text)
			text = ''.join(cleaned)
		# (CLOSE)
		# (OPEN) :Remove image-picker Macro changes
		# (NOTE) The html In the Tiddler "image-picker Macro (Example 1)" has changed,
		# (NOTE) the images are not wrapped in ps (which is ok, as the images are
		# (NOTE) represented inline). I remove this change from the diff, because
		# (NOTE) there are quite a lot of such, which disturbs the diffing.
		
		if not line_by_line_comparable:
			replace("Remove wrapping p's from images in 'image-picker Macro' Tiddler",
				r'<a>\s*<p>\s*<img>\s*</p>\s*</a>',
				'<a><img></a>'
			)
		
		# (CLOSE)
		# (OPEN) :Normalize whitespaces
		replace('Compress all whitespace to " "', r'\s+', ' ')
		replace("Let each tag start in a new line", r'\s* (?=<)', '\n')
		replace("Let each tag have a newline after it", r'(?<=>) \s*', '\n')
		replace("Compress multiple newlines to one", r'\s* \n \s*', '\n')
		remove("whitespace after <p>", r'(?<=<p>) \s*')
		remove("whitespace before </p>", r'\s* (?=</p>)')
		# (CLOSE)
		text = text.strip()

		normalized = Path (path.replace('.html', ' normalized.html'))
		set_contents (normalized, text)

		print('...done\n')

	norm(master_static)
	norm(feature_static)

	print('ALL DONE')
	sleep (2)
