import re
import unicodedata


def normalize_name(name):
    if not isinstance(name, str):
        return ""

    # Convert accented characters to normal characters
    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ascii", "ignore").decode("ascii")

    # Convert to lowercase
    name = name.lower()

    # Remove website prefix/suffix
    name = re.sub(r"https?://", "", name)
    name = re.sub(r"www\.", "", name)
    name = re.sub(r"\.(com|net|org)\b", "", name)

    # Replace punctuation with spaces
    name = re.sub(r"[^a-z0-9]+", " ", name)

    # Remove common business suffixes
    name = re.sub(
        r"\b(incorporated|inc|llc|ltd|limited|corp|corporation|company|co)\b",
        "",
        name
    )

    # Remove extra spaces
    name = re.sub(r"\s+", " ", name).strip()

    return name


def normalize_address(address):
    if not isinstance(address, str):
        return ""

    # Convert accented characters
    address = unicodedata.normalize("NFKD", address)
    address = address.encode("ascii", "ignore").decode("ascii")

    # Lowercase
    address = address.lower()

    # Standardize common address words
    replacements = {
        "avenue": "ave",
        "street": "st",
        "road": "rd",
        "drive": "dr",
        "boulevard": "blvd",
        "highway": "hwy",
        "lane": "ln",
        "parkway": "pkwy",
        "township": "twp",
        "apartment": "apt",
    }

    for old, new in replacements.items():
        address = re.sub(r"\b" + old + r"\b", new, address)

    # Replace punctuation with spaces
    address = re.sub(r"[^a-z0-9]+", " ", address)

    # Remove extra spaces
    address = re.sub(r"\s+", " ", address).strip()

    return address


if __name__ == "__main__":
    names = [
        "Maure Williams Colombier Inc",
        "Maure Wilblims Colombier Inc",
        "maurewilliamscolombier.com",
        "Dréxkor"
    ]

    print("NAME NORMALIZATION:")
    for name in names:
        print(name, "->", normalize_name(name))

    addresses = [
        "85 Wayne Avenue, Ticonderoga, NY",
        "85 Wanye Avenue, Ticonderoga Townshiip, New York",
        "Wayne Ave, Ticonderoga Townshiip, New York"
    ]

    print("\nADDRESS NORMALIZATION:")
    for address in addresses:
        print(address, "->", normalize_address(address))