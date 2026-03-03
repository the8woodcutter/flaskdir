## FLASDIR v0.1
### Created/written by The Woodcutter (aka the8woodcutter @ github.com)
#### Created on Monday March 2nd 2026

***

### Purpose of this flask application:

* To create a managed root directory with folders and their subfolders
* Have a nice design, with nice file formmat icons and formatting.
	- Includes distinct file format icons, in *color* and *not monochrome*
	- May involve an open source icon set, and involving their licence/copy rules
* Nesting and animated directories and their contents viewable in the directories
* Mime type handling and viewing of a specific set of file formats/types.
	- Text files in `/public` anywhere should be re-rendered at their following link
	- Files should all have icon, and option, that allows the file shown raw
		- This is to be done in the file tree
	- Markdown files are optionally rendered in html, using a script
	- Python files, and many other programming language files, will be rendered with syntax highlighting
* There could/should be a pastebin feature that integrates with the `/public/{tx,rx}/` directories for uploading from, and downloading to
* We want TwTXT microblog
* Some optional widgets (low priority) such as an XMPP chat, a very simple one, weather, hit counters, download counters, web/blog ring, photo carousel, marquee news ticker, stats tables, icon/emoji appendixes, etcetera
* More clarity and content to come

***

### Dependencies:

* `uwsgi` is the WSGI server this project uses
* `nginx` is used and is *required* otherwise you write and rewrite a lot of code
* `twtxt` which is best installed using `pipx install twtxt` to your `$USER`
* A python virtual environment using `pip install requirements.txt` (inside virtual environment)

***

### Things to take into consideration:

* Do not import non-native, project distinct, modules, libraries or frameworks.
	- No bootstrap, or similar, will be used.  `SASS/SCSS`, if necessary, will be used and written manually
* For the sake of modules and libraries, and nested git repos:
	- No nested repositories if we can avoid it, otherwise a `/vendor` will be required
	- Only the absolute necessity for 3rd party libraries, we are not going to be lazy
	- Modules such as XMPP chat, music player, photo carousel and largely distinct functions themselves should benefit from 3rd party python libraries
* Avoid the use of `os` from python libraries and `bash` or system scripts
* No consideration is given for cross platform for this application
	- *Linux server hosted only*
	- Possibly, if need be, BSD can be tested and we will consider cross platform for BSD
		- It's quite unlikely we get that far ever
* Very seriously use the software the app uses, otherwise if you fork this project you are intending to use parts of this code and not use it as an instance
* Fully open source licence (to be decided, probably GPL)

***

#### For ideas, issues, comments or just to get ahold of the creator please create a ticket
##### XMPP MUC for discussion, and on other python projects, is considered for the future
