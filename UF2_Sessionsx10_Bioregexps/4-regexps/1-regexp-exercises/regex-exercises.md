# Regex Exercises

# URL:
- https://regex.sketchengine.co.uk/
- Do them using https://regex101.com/


# Notes
- The first solutions are lists of literal patterns. Good as a first step to find better patterns later.
- The last solution is always the best. Responds to a simplification of the first solutions.
- The solution in exercise 4 works in regex101, not in sketchengine, due to different regex options.
- Get the whole sentence adding '.*' before and after the regexp: (.*[^A-Z][^\w]) ([A-Z].*)


# Exercise 1:
- [^Pe][ iao]t
- (pi|po|pat|p )
- p[aio ]t
- p.t


# Exercise 2:
- (p[ o/\d]|ap[et][^ ])
- (ap |ape|apt|ap\/|ap9|apo)[thr]
- ap.[th]


# Exercise 3:
- [^f ]fg   # ??
- [^ ]fg[ fkh]
- [arb].fg..
- af..[fak ]


# Exercise 4:
- [.!]( W| I|\"| H|'|\))
- [.?!][ ')"]? [WHAIST]

- [^A-Z][.!?)'\"] [A-Z]
- [^A-Z][^\w] [A-Z]
- ([^A-Z][\W]) ([A-Z])

