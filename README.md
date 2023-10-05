# Internship Search Engine

Welcome to the Internship Search Engine repository! This project allows users to add and search for internships based on keywords.

# Internship Class

The Internship class represents an internship opportunity and has the following attributes:

- Title: The title of the internship.
- Company: The company offering the internship.
- Description: A brief description of the internship.

# SearchEngine Class

The SearchEngine class manages a list of internships and provides methods to add internships and search for them based on keywords.

# Usage

1. Create an instance of SearchEngine:

    search_engine = SearchEngine()
  

2. Add internships using the "add_internship" method:

    internship = Internship("Software Development Intern", "Amazon", "Assist in developing web applications.")
    search_engine.add_internship(internship)
    

3. Search for internships using the "search_internships" method:

    keyword = input("Enter a keyword to search for internships: ")
    search_engine.search_internships(keyword)

# Example

# Example program
search_engine = SearchEngine()

# Add sample internships (similar to the ones you provided)

# Search for internships
keyword = input("Enter a keyword to search for internships: ")
search_engine.search_internships(keyword)
