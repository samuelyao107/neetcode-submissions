class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            dict0={}
            for i in range(9):
                if row[i] != ".":
                    if row[i] in dict0:
                        dict0[row[i]] +=1
                    else:
                        dict0[row[i]] =1  
                    if dict0[row[i]]>1:
                        return False      
        for i in range(9):
            dict0={}
            for elem in board:
                if elem[i] != ".":
                    if elem[i] in dict0:
                        dict0[elem[i]]+=1
                    else:
                        dict0[elem[i]] =1
                    if dict0[elem[i]]>1:
                        return False 
        dict0={}
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] != ".": 
                    if board[i][j] in dict0:
                        dict0[board[i][j]] +=1
                    else:
                        dict0[board[i][j]] =1  
                    if  dict0[board[i][j]] >1 :
                        return False 
        dict0={}
        for i in range(0,3):
            for j in range(3,6):
                if board[i][j] != ".": 
                    if board[i][j] in dict0:
                        dict0[board[i][j]] +=1
                    else:
                        dict0[board[i][j]] =1  
                    if  dict0[board[i][j]] >1 :
                        return False  

        dict0={}
        for i in range(0,3):
            for j in range(6,9):
                if board[i][j] != ".": 
                    if board[i][j] in dict0:
                        dict0[board[i][j]] +=1
                    else:
                        dict0[board[i][j]] =1  
                    if  dict0[board[i][j]] >1 :
                        return False   
        dict0={}
        for i in range(3,6):
            for j in range(0,3):
                if board[i][j] != ".": 
                    if board[i][j] in dict0:
                        dict0[board[i][j]] +=1
                    else:
                        dict0[board[i][j]] =1  
                    if  dict0[board[i][j]] >1 :
                        return False   
        dict0={}
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] != ".": 
                    if board[i][j] in dict0:
                        dict0[board[i][j]] +=1
                    else:
                        dict0[board[i][j]] =1  
                    if  dict0[board[i][j]] >1 :
                        return False   
        dict0={}
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] != ".": 
                    if board[i][j] in dict0:
                        dict0[board[i][j]] +=1
                    else:
                        dict0[board[i][j]] =1  
                    if  dict0[board[i][j]] >1 :
                        return False   
        dict0={}
        for i in range(6,9):
            for j in range(0,3):
                if board[i][j] != ".": 
                    if board[i][j] in dict0:
                        dict0[board[i][j]] +=1
                    else:
                        dict0[board[i][j]] =1  
                    if  dict0[board[i][j]] >1 :
                        return False   
        dict0={}
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] != ".": 
                    if board[i][j] in dict0:
                        dict0[board[i][j]] +=1
                    else:
                        dict0[board[i][j]] =1  
                    if  dict0[board[i][j]] >1 :
                        return False   
        dict0={}
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] != ".": 
                    if board[i][j] in dict0:
                        dict0[board[i][j]] +=1
                    else:
                        dict0[board[i][j]] =1  
                    if  dict0[board[i][j]] >1 :
                        return False     

        return True                                                                                       
                