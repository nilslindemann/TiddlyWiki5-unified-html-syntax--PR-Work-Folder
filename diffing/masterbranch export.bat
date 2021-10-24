echo off

echo EXPORT TW5.COM WIKI TO SINGLE FILE AND SINGLE STATIC HTML FILE

echo ********************************************
echo Please make sure the MASTER BRANCH is active
echo ********************************************

echo Export the "tw5.com" wiki to a single-file wiki (takes a few seconds) ...
node ../../TiddlyWiki5/tiddlywiki.js ../../TiddlyWiki5/editions/tw5.com --rendertiddler $:/core/save/all "masterbranch singlefile.html" text/plain
echo ... done

echo Also export it to a static html file (takes a few more seconds) ...
node ../../TiddlyWiki5/tiddlywiki.js ../../TiddlyWiki5/editions/tw5.com --rendertiddler $:/core/templates/alltiddlers.template.html "masterbranch static.html" text/plain
echo ... done

echo Move the exported files to this folder ...
move ..\..\TiddlyWiki5\editions\tw5.com\output\*.* . > NUL
rmdir ..\..\TiddlyWiki5\editions\tw5.com\output
echo ... done

echo DONE

REM  (NOTE) Wait for three seconds before closing this commandline window
timeout /t 3 > NUL
