pr = ""
def print_header():
    global pr
    pr = (
        f"{'Index':<20}"
        f"{'Amount':<20}"
        f"{'Category':<20}"
        f"{'Description':<20}"
    )
    return pr


def print_header_line():
    le = len(pr)
    return ("=" * le)

