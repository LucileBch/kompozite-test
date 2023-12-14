import pandas as pd

import os
from pathlib import Path
from typing import Any

# defining input and output path
INPUT_PATH = Path(__file__).parent
OUTPUT_PATH = Path(__file__).parent 

#            MAIN FUNCTION - should call 2 new modules to be shorter (explained further in comments)
def main(
        input_path:str,
        output_path:Path,
        *,
        extension = "xlsx",
        filename=None,
        **kwargs: Any
        )->bool:
    
    """
    Main function of the script. It takes a file as input and splits it into chunks of a given size.

    Attributes:
    -------------------------
    input_path: Path
        Path to the folder or input file.
    output_path: Path
        Path to the output folder.
    extension: str
        Extension of the input file. Possible values "csv" and "xlsx". Default: "xlsx"
    filename: str
        Name of the input file. Warning: Needs to be specified if the name is not included in input_path. Default: None
    kwargs: dict
        Optional arguments. Possible values:
        - nb_rows: int
            Number of rows per chunk. Default: 100
        - nb_chunks: int
            Number of chunks. Computed from nb_rows if None. Default: None
        - dtypes: dict
            Dictionary of column names and their type. Default: {"ean": str, "id_epd": str}
    
    """
    # if nb_rows exist, get it, if not return 100   
    nb_rows = kwargs.get('nb_rows', 100)
    # get value from nb_chunks, otherwise return None
    nb_chunks = kwargs.get('nb_chunks')
    
    # get nb_chukns in kwargs dict. otherwise return default type
    dtypes = kwargs.get('dtypes', {"ean": str, "id_epd": str})

#             SHOULD BE ONE MODULE WITH TWO FUNCTION : one to Read and Transform the file
# lecture du fichier d'entrée
# if the filename is given => adding it to the path
    if filename:
        input_path = input_path / Path(filename)
# if extension is xlsx => use read excel, if extension is csv => use read csv
    if extension == "xlsx":
        df = pd.read_excel(str(input_path), dtype=dtypes)
    else:
        df = pd.read_csv(str(input_path), dtype=dtypes)
    dfs = []

# if nb_chunks unspecified
    # dividing lenght of dataframe by nb of line
    # adding 1 by security to include all lines
    if nb_chunks is None:
        nb_chunks = (len(df) // nb_rows) + 1 * (len(df) % nb_rows != 0)


    total_rows = min(len(df), nb_rows*nb_chunks)

# dividing data frame according to number of rows
    dfs = [df[i : i + nb_rows] for i in range(0, total_rows, nb_rows)]


#                       SHOULD BE ONE MODULE ==> LOADING CHUNKS IN NEW FILE
# configuration output
# if filename is present adding it to output path + chunks, otherwise define it as chunks only
    if filename:
        output_path = output_path / Path(filename).stem / Path("chunks")

    else:
        output_path = output_path / Path("chunks")

# if directory doesn't exist, create one
    if not os.path.exists(output_path):
        os.makedirs(output_path)


# for each chunk, load it in file xlsx or csv according to the file extension
    for i, chunk in enumerate(dfs):
        if extension == "xlsx":
            chunk.to_excel(output_path / Path(f"chunk_{i}.xlsx"), index=False)
        else:
            chunk.to_csv(output_path / Path(f"chunk_{i}.csv"), index=False)

    # to confirm success
    return True

#                       MAIN SCRIPT EXECUTION (stays in this module main.py)
if __name__ == "__main__":
    main(INPUT_PATH, OUTPUT_PATH, filename="data.xlsx", nb_rows=100, nb_chunks=2)
