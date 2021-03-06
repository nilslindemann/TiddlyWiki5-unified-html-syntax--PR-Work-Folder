# (OPEN) :Transcludes\: 3
# (GOTO) :lib:file\:///C\:/run/code/Transcluder/lib.py

from pathlib import Path

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
# (CLOSE)

# (NOTE) Quick and dirty script which counts and logs the differences between
# (NOTE) `featurebranch static normalized loggable.html` and
# (NOTE) `masterbranch static normalized loggable.html`. For this to work, the files
# (NOTE) have to be normalized, so that identical lines have the same line number.
# (NOTE) Currently this will be the case if you set `line_by_line_comparable` to True in
# (NOTE) `normalize for diffing.py` (afterwards, append " loggable" to the file names of
# (NOTE) the exported files).

f = contents (realpath ('featurebranch static normalized loggable.html'), encoding="mbcs").splitlines()
m = contents (realpath ('masterbranch static normalized loggable.html'), encoding="mbcs").splitlines()

len_f = len(f)
len_m = len(m)

if len_f == len_m:

	print(f'Both files have {len_f} lines')

	differences = {}
	for linenum, f_line in enumerate(f):
		m_line = m[linenum]
		if m_line != f_line:
			diff = m_line, f_line
			if diff not in differences:
				differences[diff] = 0
			differences[diff] += 1

	totalchanges = sum(differences.values())
	print(f'On average, every {round(len_f / totalchanges)}th line changes')
	
	print('Differences:')
	for diff, changes in sorted(differences.items(), key=lambda x:x[1], reverse=True):
		m_line, f_line = diff
		plural = 's' if changes > 1 else ''
		print(f'  {changes} time{plural}: "{m_line}" becomes "{f_line}"')

else:
	print('the files have a different amount of lines, so this script will probably only output nonsense')
