import json
class CSVergeB:

	header = []
	metaMergeFileName = ''
	

	def writeCVSMergeFile(self, files, resultFile, metaMergeFile='metaMergeFile.meta'):
		self.makeMetaMergeFile(files, metaMergeFile)		
		with open(self.makeMetaMergeFileName()) as dataFile:
			jsonObjec = json.load(dataFile)
		finalFile = open(resultFile,'w')
		#Headers
		finalFile.write(self.clearLine(jsonObjec['head']))

			


	def clearLine(self, Line):
			lLine = ''
			for line in Line:
				lLine += line + ' '	
			print(lLine)
			return lLine


	#Crea un JSON del resultado del merge
	def makeMetaMergeFile(self, files, metaMergeFileName='metaMergeFile.meta'):
		finalJSON = {}
		self.setMetaMergeFileName(metaMergeFileName)
		metaMergeFile = open(self.makeMetaMergeFileName(),'w')
		mergeResult = self.getCVSMapAttasked(files)
		finalJSON['head'] = self.getHeader()
		finalJSON['body'] = {}
		for item in mergeResult:
			finalJSON['body'][item] = mergeResult[item]
		#Cierra el map
		with open(metaMergeFileName, 'w') as outfile:
			json.dump(finalJSON, outfile)


	def getCVSMapAttasked(self, files):
		maps = []
		headers = []
		mergeMap = {}
		for file in files:
			fileObject = open(file, 'r')
			self.addHeader(fileObject.readline().split(','))#Separados por comas
			fileMap = self.getMapFromFile(fileObject)
			mergeMap = self.mergeMapCollection(mergeMap, fileMap)
		return mergeMap

	def mergeMapCollection(self,mergeMap, fileMap):
		localMergeMap={}
		if not bool(mergeMap):
			 localMergeMap = fileMap
		else:
			for item in mergeMap:
				try:
					if fileMap[item] and mergeMap[item]:
						localMergeMap[item]=mergeMap[item] + fileMap[item]
				except KeyError:
					continue
		return localMergeMap

	#Este metodo ignora la primera linea del archivo
	#La estructura queda por ejemplo: 
	# {contxid:[response,user_type]}
	def getMapFromFile(self, fileObject):
		fileMap = {}
		firstLine = fileObject.readline() 
		passFirstLine = False
		for line in fileObject:
			if line is not firstLine or passFirstLine:
				lineSplited = line.split(',')
				fileMap[lineSplited[0]] = lineSplited[1:]
			else:
				passFirstLine = True
		return fileMap
		
	def getHeader(self):
		return self.header

	def addHeader(self, newList):
		for item in newList:
			if item  not in self.getHeader():
				self.header.append(item)
		
	def makeMetaMergeFileName(self):
		return self.metaMergeFileName
	def setMetaMergeFileName(self, fileName):
		if self.metaMergeFileName is not fileName:
			self.metaMergeFileName =  fileName

cvsObj = CSVergeB()
file1 = 'prueba-formularios.csv'
file2 = 'prueba-redirecciones.csv'
file3 = 'prueba-resultados.csv'
files = [file1,file2, file3]
#mapFile =  cvsObj.getMapFromFile(open(file1))
#print(mapFile)
#cvsObj.getCVSMapFromFile(file1)
#atasked = cvsObj.getCVSMapAttasked([file1, file2, file3])
#print(cvsObj.getHeader())
#cvsObj.makeMetaMergeFile(files,'metaMergeFile.meta')
cvsObj.writeCVSMergeFile(files, 'result.csv')