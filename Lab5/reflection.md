# Lab 5 Reflection

Rohan Suresh, PES1UG24CS383, Section G

**1. Which issues were the easiest to fix, and which were the hardest? Why?**

Style issues like names, docstrings and long lines were the easiest. Replacing pickle was the hardest since I had to make sure saving and loading the playlist still worked.

**2. Did the static analysis tools report any false positives? If so, describe one example.**

Yes, Bandit flagged random.choice even though it's just picking a random song, not anything security related.

**3. How would you integrate static analysis tools into your actual software development workflow?**

Run flake8 and pylint before every commit and add all three tools to CI so they run on every push.

**4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**

Titles with apostrophes don't crash the program anymore, the playlist bug is fixed and the code is easier to read. Pylint went from 4.57 to 10.00.
