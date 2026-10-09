pr = ""
def print_header():
    pr = (
        f"{'Index':<20}"
        f"{'Amount':<20}"
        f"{'Category':<20}"
        f"{'Description':<20}"
    )


def print_header_line():
    le = len(pr)
    print("=" * le)

