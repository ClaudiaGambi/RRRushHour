Baseline 

Laat weten dat rode auto naar voren moet 
- als auto in pad staat van rode auto moet die eerst bewegen 
- als de auto in de weg niet kan bewegen moet die weer verder kijken
- uiteindelijk beweegt de auto die wel kan 
- als laatst de pad weer terug de autos bewegen 

wat is een goeie set?
- hoeveel mogelijke zetten kunnen er in de volgende zet gezet worden
- de startsituatie is niet meer mogelijk!! 

- breath first
- best first 

* maak car object 
* dictionary alleen coordinates 

if self.orientation == 'H':
            for i, coordinate in enumerate(self.coordinates_list):
                updated_x = coordinate[0] + direction
                updated_coordinate = (updated_x, coordinate[1])
                self.updated_coordinates[i] = updated_coordinate

        if self.orientation== 'V':
            for i, coordinate in enumerate(self.coordinates_list):
                updated_y = coordinate[1] + direction
                updated_coordinate = (coordinate[0], updated_y)
                self.updated_coordinates[i] = updated_coordinate


heuristieken:
- pak de 'beste' move (grootste/ meeste stappen)



"""
Randomize + Heuristics:

1. Randomize
        Algorithm that randomly generates moves and eventually finds a solution.

2. Randomize + Cutting


Breadth First + Heuristics:

1. Breadth First
        Algorithm that explores all possible options, per generation.

2. Breadth First + NearExit
        Breadth First algorithm that prioritizes board states where the red car is more near the exit.

3. Breadth First + LoosenBoard
        Breadth First algorithm that prioritizes board states that have more potential children board states.

4. Breadth First + Blocking
        Breadth First algorithm that prioritizes board states that have a smaller number of cars between the red car and the exit.

Notes:
- With sorting the queue generation of the board state is not taken into account.
- Generation is also not taken into account with pruning (Breadth First).

To do:
- Make graphics summerizing findings
- Make script OCD proof
- Make script more efficient
- Processing time ook printen? (Maar zonder generation time prints)

"""