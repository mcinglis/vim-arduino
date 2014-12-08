
This provides basic Arduino support for Vim, adding syntax highlighting and filetype detection. The syntax highlighting is derived from the keywords of Arduino 1.0.6 (i.e. `lib/keywords.txt`), but you should be able to regenerate it if you need to, by:

``` sh
$ syntax/generate.py $PATH_TO_ARDUINO_ROOT > syntax/arduino.vim
```

The `generate.py` script requires at least Python 3.4.

Every version tag will be signed with [my GPG key](http://pool.sks-keyservers.net/pks/lookup?op=vindex&search=0xD020F814) (fingerprint: `0xD020F814`). The project is available at [Gitorious](https://gitorious.org/mcinglis/vim-arduino), [Bitbucket](https://bitbucket.org/mcinglis/vim-arduino), and [GitHub](https://github.com/mcinglis/vim-arduino).

Installation as per usual for your package manager of choice.

Enjoy!

