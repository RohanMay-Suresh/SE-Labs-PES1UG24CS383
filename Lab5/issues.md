# Lab 5 Issues Table

Rohan Suresh, PES1UG24CS383, Section G

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| SQL injection (B608) | Security | 10 | query built with % formatting, a title like "Don't Stop" crashes it | used ? placeholders |
| pickle (B301, B403) | Security | 1, 33 | pickle.loads can run code from untrusted data | used json instead |
| random.choice (B311) | Security | 17 | random is not meant for security | used secrets.choice |
| Mutable default arg (W0102) | Bug | 9 | playlist=[] is shared between calls | default None, new list inside |
| Bare except (W0702, E722) | Bug | 39 | catches every error and hides it | except sqlite3.Error |
| Naming and docstrings (C0103, C0116) | Style | whole file | camelCase names, no docstrings | snake_case names, added docstrings |
| Long lines, l variable (E501, E741) | Style | 6, 10, 21, 47, 49 | lines over 79 chars, unclear name l | split lines, renamed to songs |

Pylint: 4.57 -> 10.00, Bandit: 4 -> 0, Flake8: 7 -> 0
