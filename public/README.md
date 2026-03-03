## PLEASE READ THIS CAREFULLY:

* For the actual webroots of the actual files we will *highly likely* be using symbolic links:
	- The original location of the links, and their permissions, required to be 755/644
	- **TODO**: make script for dealing with this

* Example files:
	- PDF/EPUB/DOC/DOCX/ODT
	- Any adobe suite software formats, or other formats for GIMP, or gpick, or graphics
	- FLAC/MP3/OPUS/WAV/AAC
	- FLV/MP4/WEBM
	- JPG/JPEG/WEBP/ICO
	- PNG/GIF/SVG
	- IMG/ISO/QCOW2
	- DEB/APK/RPM
	- TAR/GZ/TAR.GZ/XZ/ZIP/7Z/LZ4/RAR/etcetera
	- BIN/EXE/DLL/MSI/APPIMAGE
	- LOG/BACKUP/BAK/PCAP/PCAPNG/TXT
	- *ETCETERA...*

* For the sake of representation of textual files *from anywhere within `public/`* we require:
	- `/scripts` in project root is where any and all executed text files, outside of flask itself, go
	- Examples of scripts:
		- *!*Markdown to HTML
		- *!* Syntax highlighting for files such as python, html, java, shell, etc
		- RSS feed parser
		- *!* `twtxt.txt` files
		- pastebin function, and put the resulting ascii/utf-8 files into `public/rx` and serve from `public/tx`
			- *TEXTUAL FILES ONLY* 
		- metadata scrapers
		- website scrapers
		- *!* emoji/icon scrapers or initializers
		- *!* SCSS/SASS for dynamic compiling of CSS (maybe, maybe not yet)

* RX and TX are for files to be put when received, and where to serve files from.
	- This can be literally whatever we want essentially
	- **NOTE**: make sure to check `/etc/nginx/mime.types` to be sure your file types are appropriately managed by nginx

* The application base file and any text files that are executable do *NOT* GO HERE
	- **TODO**: add a hook to any static file scripts that require to remove `+x` from any file whatsoever that isn't a directory.  Possibly to `/set-permissions.sh` instead


