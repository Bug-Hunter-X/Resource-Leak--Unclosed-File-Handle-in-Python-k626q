# Resource Leak: Unclosed File Handle in Python

This repository demonstrates a common, yet subtle, bug in Python: forgetting to close a file handle after opening it. This can lead to resource leaks, potentially causing performance issues or even crashes in long-running applications.

The `bug.py` file contains the buggy code. The `bugSolution.py` file shows the corrected version using the `with` statement, which automatically handles file closure.

**Why this is important:**

* **Resource exhaustion:**  Unclosed files tie up system resources (file descriptors). In a program opening many files, this can lead to resource exhaustion.
* **Data corruption:**  In some cases, data might not be fully written or flushed to disk if the file isn't closed properly.
* **Security implications:** In rare cases, leaving file handles open could create a potential security vulnerability.

**Solution:**
Always use the `with` statement when working with files in Python to guarantee they are automatically closed, even if exceptions occur.