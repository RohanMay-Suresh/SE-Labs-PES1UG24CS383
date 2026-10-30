# Lab 5 Reflection

Rohan Suresh, PES1UG24CS383, Section G

**1. Which issues were the easiest to fix, and which were the hardest? Why?**

The style issues were the easiest, like renaming functions to snake_case, adding docstrings and splitting long lines. They don't change how the code works. The hardest one was replacing pickle because I had to make sure saving and loading the playlist still worked after the change. json worked since the playlist is only a list of strings. The mutable default argument also took a bit of time to understand.

**2. Did the static analysis tools report any false positives? If so, describe one example.**

Yes, Bandit flagged random.choice (B311) even though it is only used to pick a random song, which has nothing to do with security. I still changed it to secrets.choice since we had to handle all the Bandit issues, but normally I would just leave it.

**3. How would you integrate static analysis tools into your actual software development workflow?**

I would run flake8 and pylint before every commit, either from the editor or with a pre-commit hook. In a team project they can also be added to CI (like GitHub Actions) so the checks run on every push and the build fails if there are serious Bandit issues. Fixing a few warnings each time is easier than fixing everything at the end.

**4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**

The program doesn't crash anymore when a song title has an apostrophe, and loading a playlist can't run random code now. The mutable default bug where old songs were showing up in new playlists is also fixed. The code is easier to read with proper names and docstrings. Pylint went from 4.57 to 10.00 and Bandit and Flake8 don't show any issues.
