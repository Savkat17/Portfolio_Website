"""
from scorer import score_listing

test_listings = [
    {
        "title": "2010 Mitsubishi Pajero 3.2 DI-D SWB Manual 4x4",
        "description": "Excellent condition diesel Pajero short wheelbase.",
        "year": 2010
    },
    {
        "title": "2010 Mitsubishi Pajero 3.2 DI-D Automatic 4x4",
        "description": "Excellent condition.",
        "year": 2010
    },
    {
        "title": "2011 Mitsubishi Pajero SWB",
        "description": "3.2 diesel manual transmission 4x4.",
        "year": 2011
    },
    {
        "title": "2010 Mitsubishi Pajero Sport Manual",
        "description": "Diesel 4x4.",
        "year": 2010
    }
]

for listing in test_listings:
    score, reasons = score_listing(
        title=listing["title"],
        description=listing["description"],
        year=listing["year"]
    )
    print("\n" + "=" * 60)
    print(listing["title"])
    print(f"Year: {listing['year']}")
    print(f"Score: {score}")
    print("\nReasons:")
    for reason in reasons:
        print(f" - {reason}")

"""

from search import search_google

query = '"Mitsubishi Pajero" "3.2" "manual" SWB'
results = search_google(query)

print("\n")
print("=" * 70)
print("GOOGLE SEARCH RESULTS")
print("=" * 70)

for result in results:
    title = result.get("title", "")
    link = results.get("link", "")
    snippet = results.get("snippet", "")

    print("\nTITLE:")
    print(title)
    print("\nDESCRIPTION:")
    print(snippet)
    print("\nLINK:")
    print(link)
    print("=" * 70)