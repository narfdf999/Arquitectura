import os



directory= '/Users/pedroguillermarnanzcoll/Documents/AI/Arquitectura/csv/1260_pruebas'
for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
    	print(os.path.join(directory, filename))
    	with open(filename,"wb") as file:
    		x,y,z
    		csv_out = csv.writer(file, delimiter=",")
            for index, row in enumerate(csv_out):
	        	if index == 0:
	        		coordenadas = row[0].split(",") 
	        		x= coordenadas[0]
	        		y=coordenadas[1]
	        		z=coordenadas[2]
	        	print(x,y,z)
        continue
    else:
        continue