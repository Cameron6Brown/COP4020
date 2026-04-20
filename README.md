# COP4020 QML Transpiler
Programming Language

## EBNF

```
quiz       = "<quiz>", title, question, {question}, "</quiz>" ;
title      = "<title>", TEXT, "</title>" ;
question   = "<question>", text, option, option, {option}, "</question>" ;
text       = "<text>", TEXT, "</text>" ;
option     = "<option", [whitespace, attribute], ">", TEXT, "</option>" ;
attribute  = 'correct="true"' ;
whitespace = " " | "\n" | "\t" | "\r" ;
TEXT       = { character } ;
character  = letter | digit | punctuation | whitespace ;
letter     = "a" | ... | "z" | "A" | ... | "Z" ;
digit      = "0" | ... | "9" ;
punctuation = "." | "," | "?" | "!" | "-" | "'" ;
```