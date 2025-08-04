for quote in soup.select("div.quote"):
    text = quote.select_one("span.text").text
    author = quote.select_one("small.text").text
    tags = [tag.text for tag in quote.select("div.tags a.tags")]
    print(f"{text} - {author} | Tag :- {",".join(tags)}")