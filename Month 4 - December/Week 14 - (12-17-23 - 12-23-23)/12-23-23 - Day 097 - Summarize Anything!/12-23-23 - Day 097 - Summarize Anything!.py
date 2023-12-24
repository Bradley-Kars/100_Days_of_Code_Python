import wikipediaapi
from gensim.summarization import summarize

SUMMARY_RATIO = 0.2

def get_wikipedia_article():
    while True:
        wikipedia_link = input("Enter the Wikipedia link: ")
        if is_valid_wikipedia_link(wikipedia_link):
            return wikipedia_link
        else:
            print("Invalid Wikipedia link. Please enter a valid link.")

def is_valid_wikipedia_link(link):
    return "wikipedia.org/wiki/" in link  # Basic validation, can be improved

def scrape_wikipedia(wikipedia_link):
    try:
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(wikipedia_link)
        if not page_py.exists():
            raise ValueError("Wikipedia page does not exist.")
        return page_py.text
    except wikipediaapi.exceptions.WikipediaException as e:
        print(f"Wikipedia API Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def summarize_with_gensim(text, ratio=SUMMARY_RATIO):
    try:
        summary = summarize(text, ratio=ratio)
        return summary
    except Exception as e:
        print(f"Error summarizing: {e}")
        return None

def print_summary_and_references(summary, article_text):
    print("Summary:")
    print(summary)
    print("\nWikipedia References:")
    print(article_text)

if __name__ == "__main__":
    wikipedia_link = get_wikipedia_article()
    article_text = scrape_wikipedia(wikipedia_link)

    if article_text:
        summary = summarize_with_gensim(article_text)
        if summary:
            print_summary_and_references(summary, article_text)
        else:
            print("Summarization failed.")
    else:
        print("Failed to retrieve Wikipedia article.")