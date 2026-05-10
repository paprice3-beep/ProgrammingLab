class NumericalCSVFile(CSVFile):
    def get_data(self):
        string_data = super().get_data()
        numerical_data = []

        for row in string_data:
            try:
                new_row = [row[0]]
                for value in row[1:]:
                    new_row.append(float(value))
                numerical_data.append(new_row)
            except (ValueError, TypeError, IndexError) as e:
                print(f"Errore: {e}")
                continue

        return numerical_data

with open("shampoo_sales.csv", "a") as file:
    file.write("01-01-2015,\n")
    file.write("01-02-2015,ciao\n")