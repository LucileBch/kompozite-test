"""This module contains the unit tests for the widget."""

import os
from pathlib import Path

import pandas as pd

from main import main

DTYPES = {"ean": str, "id_epd": str}

class TestCases:
    nb_rows = 500
    state = {}

    def test_initial_cleanup(self)->None:
        """Cleanup the environment to make sure that the tests are testing the right thing."""

        if os.path.exists("data/chunks"):
            files = os.listdir("data/chunks")
            for file in files:
                os.remove(f"data/chunks/{file}")

            os.rmdir("data/chunks")



    def test_main(self)->None:
        """Test that the main function runs without error."""

        main(Path("data.xlsx"), Path("data"), nb_rows=self.nb_rows)
        # Asserts
        df = pd.read_excel("data/chunks/chunk_0.xlsx", engine="openpyxl", dtype=DTYPES)
        self.state["df"] = df
        assert not df.empty
    

    def test_type_coercition(self)->None:
        """Checks that the process did not corrupt the data."""
       
        df = self.state["df"]
        # Check that ean and id_epd are strings
        assert df["ean"].dtype == "object", f"ean should be a string. Got {df['ean'].dtype} instead"
        assert df["id_epd"].dtype == "object", f"id_epd should be a string. Got {df['id_epd'].dtype} instead"


    def test_chunk_size(self)->None:
        """Checks that the process produced the right chunk size."""

        df = self.state["df"]
        assert len(df) == 500, f"Expected 500 rows. Got {len(df)} instead."

    
    def test_nb_chunks(self)->None:
        """Checks that the tests produced the right number of chunks."""

        
        files = os.listdir("data/chunks")
        assert len(files) == 14, f"Expected 14 chunk. Got {len(files)} instead."



    def test_final_cleanup(self)->None:
        """Cleanup the environment to make sure that the tests are stateless."""

        if os.path.exists("data/chunks"):
            files = os.listdir("data/chunks")
            for file in files:
                os.remove(f"data/chunks/{file}")

            os.rmdir("data/chunks")

    


if __name__ == "__main__":
    test_cases = TestCases()
    test_cases.test_initial_cleanup()
    test_cases.test_main()
    test_cases.test_type_coercition()
    test_cases.test_chunk_size()
    test_cases.test_nb_chunks()
    test_cases.test_final_cleanup()
