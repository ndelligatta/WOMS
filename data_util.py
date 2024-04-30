import os
import pandas as pd
import pickle

class DataUtility:
    # TODO: Return False or Error (Add error handling)
    # TODO: Get used to working with Lambda
    #       (change file opening code)
    def serialize_object(object, file_name, path=None):
        if path is None:
            path = os.path.dirname(__file__)
        print(f"Path is {path}")
        file_path = os.path.join(path, file_name)
        print(f"file path is {file_path}")
        with open(file_path, "wb") as f:
            pickle.dump(object, f)
        return True
    
    def deserialize_object(file_path):
        with open(file_path, "rb") as f:
            result = pickle.load(f)
        return result

    def get_dataframe(table):
        header_row = None
        data = []

        for cell in table.cells:
            # Extract row index, column index, and content of each cell
            row_index = cell.row_index
            column_index = cell.column_index
            content = cell.content
            if "\n" in content:
                content = content.replace("\n", "")
            if content.isdigit():
            # Convert the string to dollars and cents and format it as currency
                dollars_cents = int(content)
                dollars = dollars_cents // 100  # Get the dollars part
                cents = dollars_cents % 100  # Get the cents part
                formatted_currency = "${}.{:02d}".format(dollars, cents)
                content = formatted_currency

            # Check if it's the first row to extract header names
            if row_index == 0:
                if header_row is None:
                    header_row = []
                header_row.append(content)
            else:
                # Ensure the row list is initialized
                if len(data) <= row_index:
                    data.extend([[]] * (row_index - len(data) + 1))

                # Ensure the column list within the row is initialized
                if len(data[row_index]) <= column_index:
                    data[row_index].extend([None] * (column_index - len(data[row_index]) + 1))

                # Set the content in the corresponding cell of the DataFrame
                data[row_index][column_index] = content

        # Create DataFrame with header names
        df = pd.DataFrame(data[1:], columns=header_row)
        return df
    # TODO: Use for converting .pdf and .excel to .obj
    def get_object_name(self):
        pass