import numpy

frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])


def compute_number_neighbors(paded_frame, index_line, index_column):
    
    the_neighbors = paded_frame[index_line-1:index_line+2, index_column-1:index_column+2]
    number_neighbors = the_neighbors.sum() - paded_frame[index_line, index_column] #enlever la valeur de la cellule elle meme pour laisser que les voisins
    return number_neighbors



def compute_next_frame(frame):
    paded_frame = numpy.pad(frame, 1, mode="constant") #zéro padding
    
    for index_line in range(1, len(paded_frame)-1):
        for index_column in range(1, len(paded_frame[index_line])-1):
            the_neighbors = compute_number_neighbors(paded_frame, index_line, index_column)


    return frame 

while True:
    print(frame)
    frame = compute_next_frame(frame)