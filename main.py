from js import document

tiles = [1,2,3,4,5,6,7,8,0]

def shuffle():
    random.shuffle(tiles)

def render():
    board = document.getElementById("game-board")
    board.innerHTML = ""

    for i in range(9):
        btn = document.createElement("button")

        if tiles[i] == 0:
            btn.classList.add("tile", "empty")
            btn.disabled = True
        else:
            btn.classList.add("tile")
            btn.innerText = str(tiles[i])
            btn.onclick = make_move(i)

        board.appendChild(btn)

def make_move(i):
    def move(e):
        empty = tiles.index(0)

        possible = [empty-1, empty+1, empty-3, empty+3]

        if i in possible:
            if empty % 3 == 0 and i == empty-1:
                return
            if empty % 3 == 2 and i == empty+1:
                return

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

document.getElementById("reset-btn").addEventListener("click", reset)

shuffle()
render()
