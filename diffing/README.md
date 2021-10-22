The html files here document the differences between wikis created from the master branch and from the "unified-html-syntax" branch ("feature branch").

Compare "masterbranch static normalized.html" and "featurebranch static normalized.html" using the diff tool of your choice.

Or manually compare things in "masterbranch singlefile.html" and "featurebranch singlefile.html".

To regenerate the files after changes (Requirements: Windows, a recent Python installed, 'pip install regex' run in a console):

* Activate the master branch.
* Doubleclick the "masterbranch export.bat".  
  This creates "masterbranch static.html" and "masterbranch singlefile.html"
* Activate the "unified-html-syntax" branch
* Doubleclick the "featurebranch export.bat".  
  This creates "featurebranch static.html" and "featurebranch singlefile.html"
* Doubleclick the "normalize for diffing.py" (the regex module needs to be installed, "pip install regex")  
  This creates "masterbranch static normalized.html" and "featurebranch static normalized.html"


