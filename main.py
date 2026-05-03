import js
import random 
document = js.document

tiles = [1,2,3,4,5,6,7,8,0]

def is_solvable(t):

    flat = [i for i in t if i != 0]
    inv = sum(1 for i in range(len(flat)) for j in range(i+1, len(flat)) if flat[i] > flat[j])
    return inv % 2 == 0

def shuffle():
    random.shuffle(tiles)
    while not is_solvable(tiles): 
        random.shuffle(tiles)

def render():
    board = document.getElementById("game-board")
    board.innerHTML = ""
    for i in range(9):
        btn = document.createElement("button")
        if tiles[i] == 0:
            btn.classList.add("tile", "empty")
        else:
            btn.classList.add("tile")
            btn.innerText = str(tiles[i])
           
            btn.onclick = make_move(i)
        board.appendChild(btn)

def make_move(i):
    def move(e):
        empty = tiles.index(0)
        
      
        r_i, c_i = i // 3, i % 3
        r_e, c_e = empty // 3, empty % 3
        
        
        dist = abs(r_i - r_e) + abs(c_i - c_e)
        
        if dist == 1:
            tiles[empty], tiles[i] = tiles[i], tiles[empty]
            render()
            check_win()
    return move

def check_win():
    if tiles == [1,2,3,4,5,6,7,8,0]:
        document.getElementById("status").innerText = "You solved it!"

def reset(e):
    shuffle()
    document.getElementById("status").innerText = ""
    render()


document.getElementById("reset-btn").onclick = reset
shuffle()
render()
shuffle()
render()
