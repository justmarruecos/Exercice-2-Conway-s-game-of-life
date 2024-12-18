def compute_number_neighbors(paded_frame, index_line, index_column):
    
    voisins = paded_frame[index_line-1:index_line+2, index_column-1:index_column+2]
    number_neighbors = voisins.sum() - paded_frame[index_line, index_column]
    return number_neighbors