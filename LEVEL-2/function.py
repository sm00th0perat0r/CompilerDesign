from symboltable import SymbolTable
class Function:
	def __init__(self, returnType, name):
		self.returnType = returnType
		self.name       = name
		self.statementsAstList = []
		self.localSymbolTable = SymbolTable()
	def setStatementsAstList(self, sastList):
		self.statementsAstList = sastList
	def getStatementsAstList(self):
		return self.statementsAstList
	def setLocalSymbolTable(self,localList):
		self.localSymbolTable = localList
	def getLocalSymbolTable(self):
		return self.localSymbolTable
	def print(self):
		print("Program:")
		print(f"\tProcedure: {self.name},Return Type: {self.returnType}")
		print("Statements:")
		for statement in self.statementsAstList:
			if statement is not None:
				statement.print()
		# 	else:
		# 		print("Error: None statement detected")
		# 		# for stmt in self.statementsAstList:
		# 			# print(stmt)
		# print("Local Symbol Table:")
		# self.localSymbolTable.printSymbolTable()