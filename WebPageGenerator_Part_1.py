import webbrowser

f = open("summer.html", "w")
f.write("<html> <body> <h1> Stay tuned for our amazing summer sale! </h1> </body> </html>")

f = open("summer.html", "r")

webbrowser.open_new_tab("summer.html")
