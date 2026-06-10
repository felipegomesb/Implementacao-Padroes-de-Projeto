class Album:
    def __init__(self, nome):
        self.nome = nome

    def tocar(self):
        print(f"Tocando o álbum: {self.nome}")


class TocarAlbumCommand:
    def __init__(self, album):
        self.album = album
        print("TocarAlbumCommand: Comando criado para tocar o álbum.")

    def execute(self):
        self.album.tocar()
        print("Álbum tocado com sucesso!")


class Player:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command
        print("Comando definido para tocar o álbum.")

    def play(self):
        if self.command:
            self.command.execute()
            print("Player: Comando executado.")
        else:
            print("Nenhum comando definido para tocar o álbum.")


if __name__ == "__main__":

    print("Album")
    album = Album("The Dark Side of the Moon")
    album.tocar()
    print("\n")
    
    
    print("Comando")
    command = TocarAlbumCommand(album)
    command.execute()
    print("\n")
    
    
    print("Player")
    player = Player()
    player.set_command(command)
    player.play()