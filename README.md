This is the work folder for my "unified-html-syntax" pull request for [TiddlyWiki](https://github.com/Jermolene/TiddlyWiki5). For the batches to work, make sure you have [my fork of the TiddlyWiki codebase](https://github.com/nilslindemann/TiddlyWiki5) locally available. Do not change the name of the _TiddlyWiki5_ folder, and put this work folder aside of it. Alternatively, edit the relative links in the batches contained here.

The _diffing_ folder has a README explaining how to create static versions of the [tw5.com](https://tiddlywiki.com/) wiki, in order to [diff](https://winmerge.org/) them. I did this to see if unexpected things break, and I am sure that they dont, at least not in the tw5.com wiki. I did not diff all other wikis contained in _TiddlyWiki5/editions_. That will take a long while. When [Jermolene](https://github.com/Jermolene) gives his OK for this pull request, I am willing to do that.

The _doc_ folder contains the source of a wiki documenting this pull request. [Here](https://nilslindemann.github.io/TiddlyWiki5-unified-html-syntax--PR-Work-Folder/singlefile.html) is an online version. The online version is based on the "unified-html-syntax" branch, so you can play around with my syntax changes. I document these changes in the Tiddler [WikiText to HTML Examples](https://nilslindemann.github.io/TiddlyWiki5-unified-html-syntax--PR-Work-Folder/singlefile.html#WikiText%20to%20HTML%20Examples).

You can also run the wiki via Node.js by using the _run wiki via nodejs.batch_ in the _doc_ folder.

The _run all tiddlywiki tests.bat_ runs the tests contained in the _TiddlyWiki5/editions/test_ wiki.
