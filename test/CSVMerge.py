import csv

class CSVMerge:
	

	#Este método usa el la primer colección ingresada como guía
	#busca el contenido de la llave en las demás colecciones, 
	#la idea es regresar una sola collecciòn mergeada
	#def mergeCollections(self, collectionsList):
	#	resultMap = {}
	#	mainCollection =  collectionsList[0] #Se agrega el archivo principal al inicio de la lista
	#	for register in  mainCollection:
	#		for i in range(1,len(collectionsList)):
	#			if collectionsList[counter][register.key()]:
	#				register.update(collectionsList[counter][register.key()])
	#			continue
	#	return mainCollection
			


	#Se ingresa una lista de archivos, regresa una lista
	#de colecciones, cada colección usa contxid cómo llave		

	def getCollectionFromCVSFiles(self, files):
		collections = []
		for file in files: 
			csvMap	= 	self.getCollectionFromCSVFile(file)
			collections.append(csvMap)
		return collections



	#Usa la librería csv para leer archivos
	#una vez creado el objeto se crea tambien el mapa
	#ya que el archivo se cierra
	def getCollectionFromCSVFile(self, file):
		with open(file, newline='') as csvfile:
			collectionFile = csv.reader(csvfile, delimiter=' ', quotechar='|')
			csvMap= self.makeFileMaps(collectionFile)
			return csvMap

	
	#Crea un mapa usando los valores de la primer columna como llaves 
	def makeFileMaps(self, csvObject):
		resmap = {}
		for item in csvObject:
			resmap[item[0]] = item[1:]
		return resmap


#DictReader not works	

csvobj = CSVMerge()
files = ['prueba-formularios.csv', 'prueba-redirecciones.csv', 'prueba-resultados.csv']

print(csvobj.getCollectionFromCSVFile('prueba-formularios.csv'))
#print(csvobj.getCollectionFromCVSFiles(files))

#for col in csvobj.getCollectionFromCVSFiles(files):
#	print(str(col) + '\n')
