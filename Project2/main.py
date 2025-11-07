# Project 2
# Jonathan Vialpando and Arturo Nunez Gomez
import sys
from PIL import Image
import heapq

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

def heuristic (u,t):
    p1, p2 = u
    t1, t2 = t
    return abs(p1 - t1) + abs(p2 - t2)

def Best_First_Search(inputImage, starting, target):
    w, h = inputImage.size
    pix = inputImage.load()

    if not isVertex(pix[starting[1], starting[0]]):
        raise ValueError("Starting pixel is unreachable")
    if not isVertex(pix[target[1], target[0]]):
        raise ValueError("Target pixel is unreachable")

    Q = [(heuristic(starting, target),starting)]

    visited = set()
    d = {starting:0}
    prev = {}


    while Q:
        priority, u = heapq.heappop(Q)
        if u in visited:
            continue
        visited.add(u)
        if u == target:
            break
        uRow, uCol = u

        for vRow, vCol in getNeighbors(uRow, uCol, h, w):
            v = (vRow, vCol)
            if not isVertex(pix[vCol, vRow]):
                continue
            if v not in visited:
                d[v] = d[u] + 1
                prev[v] = u
                f = d[v] + heuristic(v,target)
                heapq.heappush(Q,(f,v))
    if target in d:
        path = reconstructPath(prev,starting,target)
        return d[target], visited, path
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
        print(f"Nodes visited by BFS: {len(BFSVisited)}")

    astarDistance, ASTARVisited, ASTARpath = Best_First_Search(inputImage, startingCoordinates,TargetCoordinates)
    if astarDistance is None:
        print("No path found for A*")
    else:
        print(f"Shortest path found for A*: {astarDistance}")
        print(f"Nodes visited by A*: {len(ASTARVisited)}")

    outputBFSResults = input("Enter the file name for BFS output: ")
    #outputBFSResults = "BFSoutput"
    outputASTAResults = input("Enter the file name for A* output: ")
    #outputASTAR = "ASTARoutput"

    colorizeResults(inputImage, BFSVisited, BFSpath, outputBFSResults + fileExtension)
    print(f"BFS output saved to {outputBFSResults + fileExtension}")
    print(f"A* output saved to {outputASTAResults + fileExtension}")

