echo off

echo EXPORT "DOCS" WIKI TO SINGLE FILE

REM  (NOTE) The online Wiki is generated with this batch and the refined-html-syntax-DIFF branch active.
REM  (NOTE) Also, I temporarily remove
REM  (NOTE) 
REM  (NOTE) 	"tiddlywiki/tiddlyweb",
REM  (NOTE) 	"tiddlywiki/filesystem",
REM  (NOTE) 
REM  (NOTE) from the tiddlywiki.info contained here, before running this batch.

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
