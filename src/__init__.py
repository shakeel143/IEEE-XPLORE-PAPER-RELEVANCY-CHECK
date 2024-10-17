import pandas as pd


def find_relevant_papers(csv_file, keywords):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Convert keywords into a list, removing any extra spaces
    keywords = [kw.strip().lower() for kw in keywords.split(",")]

    # Define lists to store relevant and not relevant papers
    relevant_papers = []
    not_relevant_papers = []

    # Iterate through the rows of the DataFrame
    for index, row in df.iterrows():
        # Combine relevant columns into a single text for keyword matching
        text = f"{row['Abstract']} {row['Author Keywords']}".lower()

        # Check if any of the keywords are in the text
        if any(keyword in text for keyword in keywords):
            relevant_papers.append(row['Document Title'])
        else:
            not_relevant_papers.append(row['Document Title'])

    # Get counts of relevant and not relevant papers
    num_relevant = len(relevant_papers)
    num_not_relevant = len(not_relevant_papers)

    # Print the results
    print(f"Number of relevant papers: {num_relevant}")
    print(f"Number of not relevant papers: {num_not_relevant}")
    print("\nList of relevant papers:")
    for paper in relevant_papers:
        print(paper)
    print("\nList of not relevant papers:")
    for paper in not_relevant_papers:
        print(paper)


# Example usage
csv_file = 'export2024.10.17-03.01.51.csv'
keywords = 'political campaigns'
find_relevant_papers(csv_file, keywords)
