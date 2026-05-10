class NumericalCSVFile(CSVFile):
    def get_data(self, *args, **kwargs):
        string_data = super().get_data(*args, **kwargs)
        numerical_data = []

        for row in string_data:
            if not row or row[0] == 'Date':
                continue
                
            try:
                new_row = [row[0]]
                for value in row[1:]:
                    new_row.append(float(value))
                numerical_data.append(new_row)
            except (ValueError, TypeError, IndexError) as e:
                print(f"Errore nella conversione della riga {row}: {e}")
                continue

        return numerical_data