def prep_subplot(total_plots, max_cols, **kwargs):
    """
    Helper for basic subplots
    """
    from plotly.subplots import make_subplots
    import math

    def row_cols(max_cols):
        iterator = 0
        while 1:
            row = iterator // max_cols + 1
            col = iterator % max_cols + 1


            iterator += 1
            yield row, col

    yeeterator = row_cols(max_cols)
    rows = math.ceil(total_plots/max_cols)
    fig = make_subplots(rows=rows, cols=max_cols, **kwargs)


    return fig, yeeterator
