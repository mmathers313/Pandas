# функция для построения ABC анализа
def abc(df , col, style=True):
    grouped = (df.groupby(col)['sale_usd']
               .sum().reset_index()
               .sort_values(by='sale_usd', ascending=False))

    grouped['percentage'] = grouped['sale_usd'] / grouped['sale_usd'].sum()
    grouped['cumulative_percentage'] = grouped['percentage'].cumsum()

    thresholds = {'A': 0.8, 'B': 0.95}
    grouped['ABC_Class'] = (
        ['A' if cp <= thresholds['A'] else 'B' if cp <= thresholds['B'] else 'C' for cp in grouped['cumulative_percentage']]
    )

    grouped['Class_Rank'] = grouped.groupby('ABC_Class').cumcount() + 1

    grouped.columns = (
        [f'{col}', 'revenue', 'percentage',
         'cum_percentage',	'ABC_Class',	'Class_Rank']
    )

    if style:  # Проверка, применять ли стили
        def color_format(value):
            colors = {'A': '#66BB6A', 'B': '#FFA726', 'C': '#EF5350'}
            return f'background-color: {colors[value]}'

        styled_abc = grouped.style.applymap(color_format, subset=['ABC_Class'])
        return styled_abc
    else:
        return grouped
