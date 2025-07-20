# Structure of the app:
- ## `main.py` will have logic to start the app
- ## Other files will have only structure and functions defined, no calling them, this is because, suppose we  a change needs to be made in some function, or i want to make a new function to handle everything everywhere, it will be much better if we do that in separate files. 
- ## `CSES_app.py` will do all handling, i.e. calling all functions, just that's it. If i need to call some other functions, they will be put in a `logic.py`.
- ## Now all what remains is formatting the things well, making classes properly and looking at it twice or thrice.