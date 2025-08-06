from string import ascii_letters, ascii_uppercase


def is_yelling(hey_bob):
    s = [c in ascii_uppercase for c in hey_bob if c in ascii_letters]
    if not s:
        return False
    else:
        return all(s)


def response(hey_bob):
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.endswith("?") and is_yelling(hey_bob):
        return "Calm down, I know what I'm doing!"
    if hey_bob.endswith("?"):
        return "Sure."
    elif is_yelling(hey_bob):
        return "Whoa, chill out!"
    else:
        return "Whatever."
