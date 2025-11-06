# Project 2
# Jonathan Vialpando and Arturo Nunez Gomez
import sys
from PIL import Image

def isVertex(rgb):
    r, g, b = rgb
    return (r > 100) or (g > 100) or (b > 100)

def inBounds(row, column, height, width):
    return 0 <= row < height and 0 <= column < width

def getNeighbors(row, column, height, width):
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        rr = row + dr
        cc = column + dc
        if inBounds(rr, cc, height, width):
            yield rr, cc

def reconstructPath(prev, starting, target):
    if target not in prev:
        return []
    path = [target]
    cur = target
    while cur != starting:
        cur = prev.get(cur)
        if cur is None:
            return []
        path.append(cur)
    path.reverse()
    return path

def colorizeResults(img, visited, path, outPath):
    out = img.copy().convert("RGB")
    pix = out.load()
    green = (0, 255, 0)
    red = (255, 0, 0)

    for (row, column) in visited:
        pix[column, row] = green
    for (row, column) in path: 
        pix[column, row] = red

    out.save(outPath, format="BMP")

def Breadth_First_Search(inputImage, starting, target):
    w, h = inputImage.size
    pix = inputImage.load()

    if not isVertex(pix[starting[1], starting[0]]):
        raise ValueError("Starting pixel is unreachable")
    if not isVertex(pix[target[1], target[0]]):
        raise ValueError("Target pixel is unreachable")

    Q = [starting]
    visited = set([starting])
    prev = {}
    dist = {starting: 0}

    while Q and target not in visited:
        currentPixel = Q.pop(0)
        currentPixelRow, currentPixelColumn = currentPixel
        for visitedRow, visitedColumn in getNeighbors(currentPixelRow, currentPixelColumn, h, w):
            if (visitedRow, visitedColumn) not in visited and isVertex(pix[visitedColumn, visitedRow]):
                visited.add((visitedRow, visitedColumn))
                prev[(visitedRow, visitedColumn)] = currentPixel
                dist[(visitedRow, visitedColumn)] = dist[currentPixel] + 1
                Q.append((visitedRow, visitedColumn))
    if target in visited:
        path = reconstructPath(prev, starting, target)
        return dist[target], visited, path
    else:
        return None, visited, []

if __name__ == '__main__':
    inputImageName = input("Enter input image name: ")
    fileExtension = ".bmp"
    #inputImageName = "demo"
    startingRow = int(input("Enter starting row number: "))
    #startingRow = 2
    startingColumn = int(input("Enter starting column number: "))
    #startingColumn = 2
    targetRow = int(input("Enter target row number: "))
    #targetRow = 35
    targetColumn = int(input("Enter target column number: "))
    #targetColumn = 35
    startingCoordinates = (startingRow, startingColumn)
    TargetCoordinates = (targetRow, targetColumn)

    inputImage = Image.open(inputImageName + fileExtension).convert("RGB")
    width = inputImage.size[0]
    height = inputImage.size[1]

    #run both BFS and ASTAR
    bfsDistance, BFSVisited, BFSpath = Breadth_First_Search(inputImage,startingCoordinates,TargetCoordinates)
    
    if bfsDistance is None:
        print("Not path found for BFS.")
    else:
        print(f"Shortest path found for BFS is: {bfsDistance}") #Ensure Astar is the same distance

    outputBFSResults = input("Enter the file name for BFS output: ")
    #outputBFSResults = "BFSoutput"
    #outputASTAR = input("Enter the file name for A* output: ")
    outputASTAR = "ASTARoutput"

    colorizeResults(inputImage, BFSVisited, BFSpath, outputBFSResults + fileExtension)
    print(f"BFS output saved to {outputBFSResults + fileExtension}")

