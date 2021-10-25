echo off

echo EXPORT "DOCS" WIKI TO SINGLE FILE

echo ***********************************************************
echo Please make sure the "UNIFIED-HTML-SYNTAX" branch is active
echo ***********************************************************

echo Export to a single-file wiki ...
node ../../TiddlyWiki5/tiddlywiki.js --rendertiddler $:/core/save/all singlefile.html text/plain
echo ... done

REM  (NOTE) ~ echo Export to a static html file ...
REM  (NOTE) ~ node ../../TiddlyWiki5/tiddlywiki.js --rendertiddler $:/core/templates/alltiddlers.template.html static.html text/plain
REM  (NOTE) ~ echo ... done

echo Move the exported file to this folder ...
move output\*.* . > NUL
rmdir output
echo ... done

echo DONE

REM  (NOTE) Wait for three seconds before closing this commandline window
timeout /t 3 > NUL
