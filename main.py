class Internship:
    def __init__(self, title, company, description):
        self.title = title
        self.company = company
        self.description = description

class SearchEngine:
    def __init__(self):
        self.internships = []

    def add_internship(self, internship):
        self.internships.append(internship)

    def search_internships(self, keyword):
        print(f"Search results for keyword '{keyword}':")
        found = False

        for internship in self.internships:
            if keyword.lower() in internship.title.lower() or \
               keyword.lower() in internship.company.lower() or \
               keyword.lower() in internship.description.lower():
                print(f"Title: {internship.title}")
                print(f"Company: {internship.company}")
                print(f"Description: {internship.description}")
                print()
                found = True

        if not found:
            print("No internships found matching the keyword.")

# Main program
search_engine = SearchEngine()

# Add sample internships
internship1 = Internship("Software Development Intern", "Amazon", "Assist in developing web applications.")
internship2 = Internship("Marketing Intern", "Cardevo Inc", "Help create marketing campaigns and analyze data.")
internship3 = Internship("Data Science Intern", "Redvest", "Work on data analysis and machine learning projects.")
internship4 = Internship("Graphic Design Intern", "Creative Designs Co.", "Create visual content for digital and print media.")
internship5 = Internship("Finance Intern", "Capital Investments", "Assist in financial analysis and reporting.")
internship6 = Internship("Human Resources Intern", "Talent Hub", "Support HR processes and employee engagement initiatives.")
internship7 = Internship("Environmental Science Intern", "Green Earth Research", "Contribute to environmental research and conservation efforts.")
internship8 = Internship("Event Planning Intern", "Celebration Events", "Coordinate and execute events from planning to execution.")
internship9 = Internship("Mobile App Development Intern", "Tech Innovators", "Work on developing mobile applications for iOS and Android platforms.")
internship10 = Internship("Public Relations Intern", "Media Connect Agency", "Assist in managing public relations and communication strategies.")

search_engine.add_internship(internship1)
search_engine.add_internship(internship2)
search_engine.add_internship(internship3)
search_engine.add_internship(internship4)
search_engine.add_internship(internship5)
search_engine.add_internship(internship6)
search_engine.add_internship(internship7)
search_engine.add_internship(internship8)
search_engine.add_internship(internship9)
search_engine.add_internship(internship10)

# Search for internships
keyword = input("Enter a keyword to search for internships: ")
search_engine.search_internships(keyword);


