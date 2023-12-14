import pandas as pd

import os
from pathlib import Path
from typing import Any

INPUT_PATH = Path(__file__).parent
OUTPUT_PATH = Path(__file__).parent 

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
    
    nb_rows = kwargs.get('nb_rows', 100)
    nb_chunks = kwargs.get('nb_chunks')

    dtypes = kwargs.get('dtypes', {"ean": str, "id_epd": str})

    if filename:
        input_path = input_path / Path(filename)

    if extension == "xlsx":
        df = pd.read_excel(str(input_path), dtype=dtypes)
    else:
        df = pd.read_csv(str(input_path), dtype=dtypes)
    dfs = []

    if nb_chunks is None:
        nb_chunks = (len(df) // nb_rows) + 1 * (len(df) % nb_rows != 0)

    
    total_rows = min(len(df), nb_rows*nb_chunks)

    dfs = [df[i : i + nb_rows] for i in range(0, total_rows, nb_rows)]

    if filename:
        output_path = output_path / Path(filename).stem / Path("chunks")

    else:
        output_path = output_path / Path("chunks")


    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for i, chunk in enumerate(dfs):
        if extension == "xlsx":
            chunk.to_excel(output_path / Path(f"chunk_{i}.xlsx"), index=False)
        else:
            chunk.to_csv(output_path / Path(f"chunk_{i}.csv"), index=False)

    
    return True


if __name__ == "__main__":
    main(INPUT_PATH, OUTPUT_PATH, filename="data.xlsx", nb_rows=100, nb_chunks=2)
