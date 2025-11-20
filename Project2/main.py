# Project 2
# Jonathan Vialpando and Arturo Nunez Gomez
import sys
from PIL import Image
import heapq
from collections import  deque

# isVertex will determine if a pixel's color is a vertex in the graph
def isVertex(rgb):
    r, g, b = rgb
    return (r > 100) or (g > 100) or (b > 100)

# inBounds makes sure that the row and column are in the boundaries of the image given
def inBounds(row, column, height, width):
    return 0 <= row < height and 0 <= column < width

# getNeighbors will get the coordinates of the adjacent pixels
def getNeighbors(row, column, height, width):
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        rr = row + dr
        cc = column + dc
        if inBounds(rr, cc, height, width):
            yield rr, cc

# reconstructPath will reconstruct the shortest path from target to starting
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

# colorizeResults will create our output image
# the visited nodes will be colored green
# the nodes on the shortest path are colored red
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

# Breadth_First_Search will find the shortest path in an unweighted graph.
# We will use a standard queue (deque for optimization) for exploration
def Breadth_First_Search(inputImage, starting, target):
    w, h = inputImage.size
    pix = inputImage.load()

    if not isVertex(pix[starting[1], starting[0]]):
        raise ValueError("Starting pixel is unreachable")
    if not isVertex(pix[target[1], target[0]]):
        raise ValueError("Target pixel is unreachable")

    Q = deque([starting])
    visited = set([starting])
    prev = {}
    dist = {starting: 0}

    while Q and target not in visited:
        currentPixel = Q.popleft()
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

# heuristic will estimate the shortest distance from u to goal t if there are no obstacles
def heuristic (u,t):
    p1, p2 = u
    t1, t2 = t
    return abs(p1 - t1) + abs(p2 - t2)

# implemented the Best_First_Search algorithm.
# we will use a priority queue (heapq) that is based on f(v) = d[v] + h[v]
def Best_First_Search(inputImage, starting, target):
    w, h = inputImage.size
    pix = inputImage.load()
    s = starting
    t = target

    if not isVertex(pix[s[1], s[0]]):
        raise ValueError("Starting pixel is unreachable")
    if not isVertex(pix[t[1], t[0]]):
        raise ValueError("Target pixel is unreachable")

    d = {(r, c): float('inf') for r in range(h) for c in range(w)}

    prev = {}
    visited = set()
    Q = []
    d[s] = 0
    heapq.heappush(Q, (d[s] + heuristic(s, t), s))

    while Q and t not in visited:
        priority, u = heapq.heappop(Q)
        if u in visited:
            continue
        visited.add(u)
        uRow, uCol = u
        for vRow, vCol in getNeighbors(uRow, uCol, h, w):
            v = (vRow, vCol)
            if isVertex(pix[vCol, vRow]) and v not in visited:
                new_dist = d[u] + 1
                if new_dist < d[v]:
                    d[v] = new_dist
                    prev[v] = u
                    f = d[v] + heuristic(v, t)
                    heapq.heappush(Q, (f, v))

    if t in visited:
        path = reconstructPath(prev, s, t)
        return d[t], visited, path
    else:
        return None, visited, []

if __name__ == '__main__':
    # user input for filename, starting and target coordinates
    inputImageName = input("Enter input image name: ")
    fileExtension = ".bmp"
    if not inputImageName.lower().endswith(fileExtension):
        inputImageName = inputImageName + fileExtension
    startingRow = int(input("Enter starting row number: "))
    startingColumn = int(input("Enter starting column number: "))
    targetRow = int(input("Enter target row number: "))
    targetColumn = int(input("Enter target column number: "))
    startingCoordinates = (startingRow, startingColumn)
    TargetCoordinates = (targetRow, targetColumn)

    # loading our image and getting the width and height
    inputImage = Image.open(inputImageName).convert("RGB")
    width = inputImage.size[0]
    height = inputImage.size[1]

    # run both BFS and ASTAR
    bfsDistance, BFSVisited, BFSpath = Breadth_First_Search(inputImage,startingCoordinates,TargetCoordinates)
    if bfsDistance is None:
        print("Not path found for BFS.")
    else:
        print(f"Shortest path found for BFS is: {bfsDistance}")

    astarDistance, ASTARVisited, ASTARpath = Best_First_Search(inputImage, startingCoordinates,TargetCoordinates)
    if astarDistance is None:
        print("No path found for A*")
    else:
        print(f"Shortest path found for A*: {astarDistance}")

    # input for getting output file name, and outputing the results
    outputBFSResults = input("Enter the file name for BFS output: ")
    outputASTAResults = input("Enter the file name for A* output: ")
    colorizeResults(inputImage, BFSVisited, BFSpath, outputBFSResults + fileExtension)
    colorizeResults(inputImage, ASTARVisited, ASTARpath, outputASTAResults + fileExtension)

    print(f"BFS output saved to {outputBFSResults + fileExtension}")
    print(f"A* output saved to {outputASTAResults + fileExtension}")
