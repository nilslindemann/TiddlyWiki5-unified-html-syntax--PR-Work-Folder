The html files here document the differences between wikis created from the master branch and from the "unified-html-syntax" branch (= "featurebranch").

Compare "masterbranch static normalized.html" and "featurebranch static normalized.html" using the diff tool of your choice. Or manually compare things in "masterbranch singlefile.html" and "featurebranch singlefile.html".

To regenerate the files after changes (Requirements: Windows, a recent Python, the regex module - "pip install regex"):

* Activate the master branch.
* Double-click the "masterbranch export.bat". This creates "masterbranch static.html" and "masterbranch singlefile.html".
* Activate the "unified-html-syntax" branch.
* Double-click the "featurebranch export.bat". This creates "featurebranch static.html" and "featurebranch singlefile.html".
* Double-click the "normalize for diffing.py" (the regex module needs to be installed, "pip install regex"). This creates "masterbranch static normalized.html" and "featurebranch static normalized.html"


