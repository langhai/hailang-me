Writing Posts Using reStructuredText Directives
###############################################

:date: 17-01-2013
:tags: rst, pelican
:category: Code!
:slug: write-rest-post
:author: Hai Lang
:status: published

.. highlights:: 1234

There is no 

.. pull-quote:: POWAH!

.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.

.. table:: Truth table for "not"

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

Links
--------------
You can easily create a hyper link by adding a '_' after a word.

.. code-block:: rest

    This is a link_

In order for a hyperlink to work, you'll have to define it's destination as well. 
The link destination can be defined anywhere in the document, putting all hyperlink definitions at the end of your document seems to be a nice idea.

.. code-block:: rest

    Click here_ for google

    .. _here: http://google.com

..

Here's how it looks like, now 'here' is a hyperlink to google.com
Click here_ for google

Code
--------------
You can include code snippets in your document by using code or code-block directives.

.. code-block:: rest

    .. code-block:: identifier
    <blank line>
    <indent>#include <stdio.h>
    <indent>
    <indent>void take_out_garbage() {
    <indent>    printf("Yes, ma'am!\n");
    <indent>    sleep(5000);
    <indent>}
    <blank line>

And this will look like

.. code-block:: cpp

    #include <stdio.h>

    void take_out_garbage() {
        printf("Yes, ma'am!\n");
        sleep(5000);
    }

Replace the identifier with a lexer. Lexer tells pygments what kind of programming language you are writing. Here's a list of available lexers_


.. _here: http://google.com
.. _lexers: http://pygments.org/docs/lexers/
