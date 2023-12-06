import requests
import os

def search_uniprot_for_peptides(max_length=60):
    """
    Search UniProt for peptides with length less than max_length.
    :param max_length: Maximum length of peptides.
    :return: List of UniProt IDs.
    """
    query = f"length:[1 TO {max_length}] AND reviewed:true"
    url = "https://rest.uniprot.org/uniprotkb/search"
    params = {
        "query": query,
        "format": "list",
        "size": 50  # Adjust as needed
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Failed to retrieve data from UniProt: {response.status_code} - {response.text}")
        return []

    return response.text.strip().split('\n')

def get_pdb_ids_from_uniprot(uniprot_id):
    """
    Get PDB IDs associated with a given UniProt ID.
    :param uniprot_id: UniProt ID.
    :return: List of PDB IDs.
    """
    url = f"https://www.ebi.ac.uk/pdbe/api/mappings/best_structures/{uniprot_id}"
    response = requests.get(url)
    pdb_ids = []

    if response.status_code == 200:
        data = response.json()
        if uniprot_id in data:
            for entry in data[uniprot_id]:
                pdb_id = entry.get('pdb_id')
                if pdb_id:
                    pdb_ids.append(pdb_id)
    elif response.status_code == 404:
        print(f"No PDB entries found for UniProt ID {uniprot_id}")
    else:
        print(f"Failed to retrieve PDB IDs for UniProt ID {uniprot_id}: {response.status_code} - {response.text}")

    return pdb_ids

def download_files(uniprot_ids, output_directory="output"):
    """
    Download FASTA sequences and PDB files for UniProt IDs with associated PDB IDs.
    Each UniProt ID will have its own directory.
    :param uniprot_ids: List of UniProt IDs.
    :param output_directory: Directory where sub-folders will be created.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for uniprot_id in uniprot_ids:
        uniprot_dir = os.path.join(output_directory, uniprot_id)
        if not os.path.exists(uniprot_dir):
            os.makedirs(uniprot_dir)

        pdb_ids = get_pdb_ids_from_uniprot(uniprot_id)

        if pdb_ids:
            # Download FASTA file from UniProt
            fasta_url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
            fasta_response = requests.get(fasta_url)
            if fasta_response.status_code == 200:
                fasta_file_path = os.path.join(uniprot_dir, f"{uniprot_id}.fasta")
                with open(fasta_file_path, 'w') as file:
                    file.write(fasta_response.text)
                print(f"Downloaded FASTA for {uniprot_id}")

            # Download PDB files
            for pdb_id in pdb_ids:
                pdb_url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
                pdb_response = requests.get(pdb_url)
                if pdb_response.status_code == 200:
                    pdb_file_path = os.path.join(uniprot_dir, f"{pdb_id}.pdb")
                    with open(pdb_file_path, 'w') as file:
                        file.write(pdb_response.text)
                    print(f"Downloaded PDB file {pdb_id} for UniProt ID {uniprot_id}")
        else:
            print(f"Skipped UniProt ID {uniprot_id} as no PDB entries were found.")

def main():
    uniprot_ids = search_uniprot_for_peptides()
    print(f"Found {len(uniprot_ids)} UniProt IDs")
    download_files(uniprot_ids)

if __name__ == "__main__":
    main()

