" Vim syntax file
" Language: SolidCAM .gpp postprocessor
" Maintainer: Dmitry Ponyatov <dponyatov@gmail.com>

"if exists("b:current_syntax")
"    finish
"endif

syntax match Comment "\v;.*$"
syntax match Function "\v\@\w+"
syntax keyword Function endp
syntax keyword Keyword global if else endif call
syntax keyword Type logical string integer numeric true false TRUE FALSE
syntax match String "'.*'"
syntax match Constant "\<[0-9]*\>"

let b:current_syntax = "gpp"

