# Lab 5 Issues Table

Rohan Suresh, PES1UG24CS383, Section G

Line numbers are from the original file.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| SQL injection (B608) | Security - Bandit, Medium | 10 | the insert query was made with % formatting so title and artist go straight into the sql. a title like "Don't Stop" crashes the program | used ? placeholders and passed the values as a tuple |
| pickle.loads (B301) | Security - Bandit, Medium | 33 | pickle can run code when loading data from an untrusted source | used json.dumps / json.loads instead since the playlist is just a list of strings |
| Mutable default arg (W0102) | Bug - Pylint | 9 | playlist=[] is shared between calls so old songs show up in new playlists | changed default to None and made a new list inside the function |
| Bare except (W0702, E722) | Bug - Pylint/Flake8 | 39 | catches every exception and hides actual errors | changed it to except sqlite3.Error |
| import pickle (B403) | Security - Bandit, Low | 1 | importing pickle is flagged | removed it with the json change |
| random.choice (B311) | Security - Bandit, Low | 17 | random is not meant for anything security related | changed to secrets.choice |
| Function names (C0103) | Style - Pylint | 9, 15, 28, 32, 36 | function names were camelCase | renamed to snake_case (add_song, shuffle_pick etc) |
| Missing docstrings (C0114, C0116) | Style - Pylint | whole file | no module or function docstrings | added docstrings |
| else after return (R1705) | Style - Pylint | 22-25 | else is not needed after a return | removed the else |
| Multiple statements on one line (C0321, E701) | Style - Pylint/Flake8 | 48 | if and print on the same line | put the print on its own line |
| Line too long (E501) | Style - Flake8 | 6, 10, 21, 49 | lines longer than 79 characters | split the lines |
| Ambiguous variable name (E741) | Style - Flake8 | 47 | variable called l | renamed it to songs |

Pylint: 4.57 -> 10.00  
Bandit: 4 issues -> 0  
Flake8: 7 issues -> 0
