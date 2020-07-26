class Upsert:
    def __init__(self, table):
        self.table = table

    def upsert_rows(self, rows: list, primary_keys: list):
        """
        Assumes all rows have the same set of keys (columns).
        """

        if rows is None:
            return False

        keys_text = self._get_primary_keys_text(primary_keys)
        columns_list = self._get_column_list(rows)
        columns_text = self._get_column_text(columns_list)
        values_text = self._get_values_text(rows, columns_list)
        on_conflict_query = self._get_conflict_update_query(columns_list, primary_keys)

        query = f'INSERT INTO {self.table.name} ' \
                f'({columns_text}) ' \
                f'VALUES {values_text} ' \
                f'ON CONFLICT ({keys_text}) DO UPDATE {on_conflict_query};'
        return self.table.run_query(query)

    def _get_primary_keys_text(self, primary_keys: list):
        keys_text = ''
        for primary_key in primary_keys:
            keys_text += primary_key
            keys_text += ','
        keys_text = keys_text.strip(',')
        return keys_text

    def _get_column_list(self, rows):
        columns_list = []
        for (column, value) in rows[0].items():
            columns_list.append(column)
        return columns_list

    def _get_column_text(self, columns_list):
        columns_text = ''
        for column in columns_list:
            columns_text += f'{column},'
        columns_text = columns_text.strip(',')
        return columns_text

    def _get_values_text(self, rows, columns_list):
        values = ''
        for row in rows:
            values += '('
            for column in columns_list:
                value = row[column]
                if value is None:
                    values += 'NULL,'
                else:
                    escaped_value = self._escape_chars(value)
                    values += f"'{escaped_value}',"
            values = values.strip(',')
            values += '),'
        values = values.strip(',')
        return values

    def _get_conflict_update_query(self, columns: list, primary_keys: list):
        query = f'SET '
        for column in columns:
            if column in primary_keys:
                continue
            query += f'{column} = EXCLUDED.{column},'
        query = query.strip(',')
        query += f' WHERE'
        for primary_key in primary_keys:
            query += f' {self.table.name}.{primary_key} = EXCLUDED.{primary_key} AND'
        query = query.strip(' AND')
        return query

    def _escape_chars(self, value):
        if value is not None and isinstance(value, str):
            return value.replace("'", "''")
        return value
