def set_bad_version(bad: int):
    def isBadVersion(n: int):
        return True if n >= bad else False
    return isBadVersion
