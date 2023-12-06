# UniProtPeptideToFASTAandPDBDownloader
Overview
The UniProtPeptideToPDBDownloader script is a Python tool designed to streamline the process of fetching peptide sequences from the UniProt database that are associated with structural data in the Protein Data Bank (PDB). It automates the retrieval of FASTA sequences for peptides (specifically, those under 60 amino acids in length and reviewed) from UniProt and downloads corresponding PDB files from the RCSB PDB database.

Features
Automated Querying: Searches UniProt for peptides based on specified criteria (length ≤ 60 amino acids and reviewed status).
UniProt to PDB Mapping: For each UniProt ID, the script finds associated PDB IDs.
Organized Downloads: Downloads FASTA sequences from UniProt and PDB files, saving them in separate directories named after each UniProt ID for easy organization and reference.
Batch Processing: Capable of handling multiple UniProt IDs and corresponding PDB files efficiently.
Prerequisites
Before running the script, ensure you have Python installed on your system along with the requests library. If you do not have the requests library, you can install it using the following command:


pip install requests
Usage
Clone the Repository: Clone this repository to your local machine or download the script file.

Run the Script: Navigate to the script's directory in your terminal and execute it with Python:

Copy code
python UniProtPeptideToPDBDownloader.py
Check the Output: After running, the script will create an output directory where it stores the downloaded FASTA and PDB files, organized into subdirectories named after each UniProt ID.

Customization
You can adjust the script according to your needs:

Modify the max_length parameter in the search_uniprot_for_peptides function to change the maximum peptide length considered.
Change the size parameter to control the number of results to fetch from UniProt.
Contributing
Contributions to enhance the script, extend its functionality, or improve documentation are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

License
This project is released under the MIT License. See the LICENSE file for more details.
