The html files here document the differences between wikis created from the [master branch](https://github.com/nilslindemann/TiddlyWiki5/tree/master) and from the [refined-html-syntax branch](https://github.com/nilslindemann/TiddlyWiki5/tree/refined-html-syntax) (= "featurebranch") in [my fork of TiddlyWiki5](https://github.com/nilslindemann/TiddlyWiki5).

Compare _masterbranch static normalized.html_ and _featurebranch static normalized.html_ using the [diff tool](https://winmerge.org/) of your choice. Or manually compare things in _masterbranch singlefile.html_ and _featurebranch singlefile.html_.

To regenerate the files after changes (Requirements: Windows, a recent Python, the regex module – `pip install regex`):

* Activate the [master branch](https://github.com/nilslindemann/TiddlyWiki5/tree/master).
* Double-click the _masterbranch export.bat_. This creates _masterbranch static.html_ and _masterbranch singlefile.html_.
* Activate the [refined-html-syntax branch](https://github.com/nilslindemann/TiddlyWiki5/tree/refined-html-syntax).
* Double-click the _featurebranch export.bat_. This creates _featurebranch static.html_ and _featurebranch singlefile.html_.
* Double-click the _normalize for diffing.py_. This creates _masterbranch static normalized.html_ and _featurebranch static normalized.html_.
