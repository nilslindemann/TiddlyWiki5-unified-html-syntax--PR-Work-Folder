echo off

echo EXPORT TESTWIKI

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
timeout /t 3 > NUL
