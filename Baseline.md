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