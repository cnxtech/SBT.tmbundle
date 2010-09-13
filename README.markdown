SBT.tmbundle: a [TextMate](http://macromates.com/) bundle for the [Simple Build Tool](http://code.google.com/p/simple-build-tool/).
==========================

This is a minimal bundle for the TextMate editor to call the Simple Build Tool.  It currently only adds one command, Build cmd-B, that calls `sbt compile`.  It then parses the SBT output and makes any file references hyperlinks to the appropriate location in the file.

If you're interested in SBT and Textmate, you may also be interested in this [SBT Console Textmate plugin](http://github.com/mads379/SBT-Console-Textmate-Plugin).  It is much more heavyweight, but probably also much better supported :).

Installation
------------

This bundle requires a way to run SBT without ANSI colour control sequences in the output.  I use a similar technique to the Console plugin above: you must make a second SBT startup script to start SBT in this mode.  I use the following script in `/usr/local/bin/sbt_nocolours`:

    #! /bin/sh
    
    # see http://code.google.com/p/simple-build-tool/
    
    java -Xmx512M -XX:+CMSClassUnloadingEnabled -Dsbt.log.noformat=true -XX:MaxPermSize=256m -jar /usr/local/lib/sbt-launch.jar "$@"

You'd need to modify that to include your path to `sbt-launch.jar`.  I also assume that /usr/local/bin is in your Textmate path.

Use
---

There is one command at present, although the support tools are there to make more fairly easily.  That command is 'Build - cmd-B'.  When executed from a Textmate project window, it:

* saves all files in the project,
* searches upwards from the project window until it finds a directory with both a `src` subdirectory and a `project/build.properties` file, and assumes that is the SBT project directory,
* calls `sbt_nocolours compile` in that SBT project directory,
* displays the output and makes any paths that appear in the output into hyperlinks.

Making other Textmate commands that execute other SBT commands would be trivial.  However, the parsing and display out output currently occurs when the sbt command completes, which makes the incremental commands less useful.

License
-------

The code in `htmlize_sbt.py` is based on the TextMate java bundle, and so shouldn't be used unless you have a TextMate license.

Any code not covered by another license is released under the BSD simplified license:

Copyright 2010 William Uther. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the authors and should not be interpreted as representing official policies, either expressed or implied, of anyone else.
