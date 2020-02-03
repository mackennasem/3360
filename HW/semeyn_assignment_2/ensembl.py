# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 2 - Ensembl
# ensembl.py

import ftplib
import io
import sys
import requests
import os
import time
import gzip
import urllib.request
import urllib.error


def get_sequence():
    # constant for requests made per second
    reqs_per_second = 15
    server = "https://rest.ensembl.org"
    input_id = sys.argv[1]

    # if a ref-seq ID is entered
    if not input_id.isnumeric():
        ensembl_id = convert_id()

        # Case 1: Returned list is empty (error in convert_id())
        if len(ensembl_id) == 0:
            return
        # Case 2: Search ENSEMBL for each ID in the list
        else:
            # set filename in format of [user input].fasta
            filename = sys.argv[2] + ".fasta"
            try:
                # create file with input name, throws error if file already exists
                fin = open(filename, "x")
                # closes file
                fin.close()
            except FileExistsError:
                print("ERROR: File name already exists")
                return
            # opens file again but in 'append' mode for loop
            fin = open(filename, "a")
            req_count = 0
            # for loop through each sequence in the list
            for iid in ensembl_id:
                ext = "/sequence/id/" + iid + "?"
                r = requests.get(server + ext, headers={"Content-Type": "text/x-fasta"})
                if not r.ok:
                    r.raise_for_status()
                    sys.exit()
                # make sure to not exceed rate limit
                req_count += 1
                if req_count % reqs_per_second == 0:
                    time.sleep(0.50)
                fin.write(r.text)

            # close file when finished writing to it
            fin.close()
            file_stats = os.stat(filename)
            print("TRUE")
            print(f'File size: {round(file_stats.st_size / (1024 * 1024), 2)} MB')
    else:
        # get accession from ensembl
        server2 = "https://rest.ensembl.org"
        ext2 = "/info/genomes/taxonomy/" + input_id
        # request for accession information
        t = requests.get(server2 + ext2, headers={"Content-Type": "application/json"})
        # if request is bad
        if not t.ok:
            print("ERROR: " + t.status_code)
            return

        # parse json object to get proper accession information
        json_obj = t.json()
        assembly_accession = json_obj[0]["assembly_accession"]
        assembly_name = json_obj[0]["assembly_name"]
        division = json_obj[0]["division"]
        url_name = json_obj[0]["url_name"]
        server3 = "ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/"

        # set extension based on classification from ENSEMBL divisions and results
        if "Vertebrate" in division:
            ext3 = "vertebrate_mammalian/" + url_name + "/latest_assembly_versions/" + assembly_accession \
                   + "_" + assembly_name + "/"
        elif "Fungi" in division:
            ext3 = "fungi/" + url_name + "/latest_assembly_versions/" + assembly_accession \
                   + "_" + assembly_name + "/"
        elif "Metazoa" in division:
            ext3 = "protozoa/" + url_name + "/latest_assembly_versions/" + assembly_accession \
                   + "_" + assembly_name + "/"
        elif "Plants" in division:
            ext3 = "plant/" + url_name + "/latest_assembly_versions/" + assembly_accession \
                   + "_" + assembly_name + "/"
        elif "Bacteria" in division:
            ext3 = "bacteria/" + url_name + "/latest_assembly_versions/" + assembly_accession \
                   + "_" + assembly_name + "/"
        else:
            print("ERROR: Invalid domain specified")
            return

        # set filename in format of [user input].fasta
        filename = sys.argv[2] + ".fasta"
        try:
            # create file with input name, throws error if file already exists
            fin = open(filename, "x")
            # closes file
            fin.close()
        except FileExistsError:
            print("ERROR: File name already exists")
            return
        # set information and try to download file from ftp server
        url = server3 + ext3
        file = assembly_accession + "_" + assembly_name + "_genomic.fna.gz"
        # try to fetch file specified and unzip into regular fasta file
        try:
            response = urllib.request.urlopen(url + file)
            compressedfile = io.BytesIO(response.read())
            decompressedfile = gzip.GzipFile(fileobj=compressedfile)
            with open(filename, 'wb') as out:
                out.write(decompressedfile.read())
            # close file when finished
            out.close()
            # calculate and print stats on file
            file_stats = os.stat(filename)
            print("TRUE")
            print(f'File size: {round(file_stats.st_size / (1024 * 1024), 2)} MB')
        # except errors because of url issues
        except requests.exceptions.InvalidSchema:
            print("ERROR: No connection adapters found for " + url)
        except (ftplib.error_perm, urllib.error.URLError):
            print("ERROR: No such file or directory")


def convert_id():
    # establish server url
    server = "https://biodbnet-abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi.json?"
    # get ID from the user
    input_id = sys.argv[1]
    # declare empty list for IDs
    ensembl_id_list = []

    # get prefix of Ref-Seq ID
    prefix = input_id[:2]
    invalid_id = False
    ext = ""
    # Case 1: Genomic Accession
    if prefix == "AC" or prefix == "NC" or prefix == "NG" or prefix == "NT" or prefix == "NW" or prefix == "NS" \
            or prefix == "NZ":
        # get rid of trailing numbers after decimal - API does not return a value
        iid = input_id.split(".")
        # add refseq genomic accession to extension
        ext = "method=db2db&input=refseqgenomicaccession&inputValues=" + iid[0] + \
              "&outputs=ensemblgeneid&format=row"
    # Case 2: mRNA Accession
    elif prefix == "NM" or prefix == "NR" or prefix == "XM" or prefix == "XR":
        # get rid of trailing numbers after decimal - API does not return a value
        iid = input_id.split(".")
        # add refseq mRNA accession to extension
        ext = "method=db2db&input=refseqmrnaaccession&inputValues=" + iid[0] + \
              "&outputs=ensemblgeneid&taxonId=&format=row"
    # Case 3: Protein Accession
    elif prefix == "AP" or prefix == "NP" or prefix == "YP" or prefix == "XP" or prefix == "ZP":
        # get rid of trailing numbers after decimal - API does not return a value
        iid = input_id.split(".")
        # add refseq protein accession to extension
        ext = "method=db2db&input=refseqproteinaccession&inputValues=" + iid[0] + \
              "&outputs=ensemblgeneid&taxonId=&format=row"
    # Case 4: Invalid prefix for accession
    else:
        # bool for invalid input
        invalid_id = True

    # Case 1: No valid input to request
    if invalid_id:
        print("ERROR: Unable to convert Ref-Seq ID to ENSEMBL ID (Improper Prefix)")
    # Case 2: Valid input to request
    else:
        # request for ENSEMBL ID from Ref-Seq ID
        g = requests.get(server + ext)
        # format request output into a JSON object
        json_obj = g.json()
        # take JSON object and place results for ENSEMBL gene ID into a list
        ensembl_id_list = json_obj[0]["Ensembl Gene ID"].split("//")

    # return ENSEMBL ID(s) as a list
    return ensembl_id_list
