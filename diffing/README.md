The html files here document the differences between wikis created from the [master-diff branch](https://github.com/nilslindemann/TiddlyWiki5/tree/master-diff) and from the [refined-html-syntax-diff branch](https://github.com/nilslindemann/TiddlyWiki5/tree/refined-html-syntax-diff) (= "featurebranch") in [my fork of TiddlyWiki5](https://github.com/nilslindemann/TiddlyWiki5).

Compare _masterbranch static normalized.html_ and _featurebranch static normalized.html_ using the [diff tool](https://winmerge.org/) of your choice. Or manually compare things in _masterbranch singlefile.html_ and _featurebranch singlefile.html_.

To regenerate the files after changes (Requirements: Windows or the capability to reproduce batch file commands in your environment, a recent Python, the regex module – `pip install regex`):

* In your [Git-Tool](https://desktop.github.com/), activate the [master-DIFF branch](https://github.com/nilslindemann/TiddlyWiki5/tree/master-diff).
* Double-click the _masterbranch export.bat_. This creates/overwrites _masterbranch static.html_ and _masterbranch singlefile.html_.
* Activate the [refined-html-syntax-DIFF branch](https://github.com/nilslindemann/TiddlyWiki5/tree/refined-html-syntax-diff).
* Double-click the _featurebranch export.bat_. This creates/overwrites _featurebranch static.html_ and _featurebranch singlefile.html_.
* Double-click the _normalize for diffing.py_. This creates/overwrites _masterbranch static normalized.html_ and _featurebranch static normalized.html_.
