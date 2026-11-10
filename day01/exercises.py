"""
Day 1 exercises: variables, types, maths operators and f-strings.

Theme: you're writing small helpers for a security monitoring tool.

How to check your answers (run in the VS Code terminal, from the python-mastery folder):
    python -m pytest day01

Each function currently returns None, so every test fails (red) at the start.
Replace `return None` with your own code. Stuck after 20 minutes? Ask for Hint 1.
"""


# ---------------------------------------------------------------------------
# Exercise 1: Log file sizes (about 10 min)
# ---------------------------------------------------------------------------
# Log files are measured in bytes, but people read sizes in megabytes (MB).
# Here, 1 MB = 1024 * 1024 bytes (1,048,576 bytes).
#
# Convert num_bytes to megabytes, rounded to 2 decimal places.
#
# Examples:
#   bytes_to_megabytes(1048576)  -> 1.0
#   bytes_to_megabytes(5242880)  -> 5.0
#   bytes_to_megabytes(1500000)  -> 1.43
def bytes_to_megabytes(num_bytes):
    # YOUR CODE HERE
    return None


# ---------------------------------------------------------------------------
# Exercise 2: Network traffic total (about 15 min)
# ---------------------------------------------------------------------------
# A firewall report gives you bytes sent and bytes received as TEXT (strings),
# because it was read from a file. Return the total traffic as an int,
# and build an alert message with an f-string.
#
# Return TWO things, separated by a comma, like this:  return total, message
# The message must look EXACTLY like this:
#   "Host 10.0.0.5 transferred 1500 bytes"
#
# Examples:
#   traffic_report("10.0.0.5", "1000", "500") -> (1500, "Host 10.0.0.5 transferred 1500 bytes")
#   traffic_report("8.8.8.8", "0", "64")      -> (64, "Host 8.8.8.8 transferred 64 bytes")
def traffic_report(host, sent_text, received_text):
    # YOUR CODE HERE
    return None


# ---------------------------------------------------------------------------
# Exercise 3: Session duration (about 25 min, the hardest one)
# ---------------------------------------------------------------------------
# A login session lasted total_seconds. Return it as a string "HH:MM:SS",
# with each part 2 digits wide (padded with a leading zero if needed).
#
# Examples:
#   session_duration(0)     -> "00:00:00"
#   session_duration(65)    -> "00:01:05"
#   session_duration(3661)  -> "01:01:01"
#   session_duration(86399) -> "23:59:59"
#
# Tools you'll need: //, % and f-string formatting like {value:02d}
def session_duration(total_seconds):
    # YOUR CODE HERE
    return None


# ---------------------------------------------------------------------------
# Playground: run this file directly (python day01\exercises.py) to try
# your functions by hand. pytest ignores this part.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print(bytes_to_megabytes(1500000))
    print(traffic_report("10.0.0.5", "1000", "500"))
    print(session_duration(3661))
