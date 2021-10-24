echo off

echo EXPORT "DOCS" WIKI TO SINGLE-FILE AND STATIC WIKIS

echo Export to a single-file wiki ...
node ../../TiddlyWiki5/tiddlywiki.js ../docs --rendertiddler $:/core/save/all singlefile.html text/plain
echo ... done

echo Export to a static html file ...
node ../../TiddlyWiki5/tiddlywiki.js ../docs --rendertiddler $:/core/templates/alltiddlers.template.html static.html text/plain
echo ... done

echo Move the exported files to this folder ...
move output\*.* . > NUL
rmdir output
echo ... done

echo DONE

REM  (NOTE) Wait for three seconds before closing this commandline window
timeout /t 3 > NUL
