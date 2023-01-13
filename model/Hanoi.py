class HanoiConfiguration:
    def __init__(self, nbTower: int, nbDisk: int):
        self.nbTower = nbTower
        self.nbDisk = nbDisk
        self.towers = []

        for i in range(self.nbTower):
            self.towers.append([])

        for i in range(self.nbDisk):
            self.towers[0].append(self.nbDisk - i)

    def __str__(self):
        return str(self.towers)

if __name__ == '__main__':
    config = HanoiConfiguration(3, 4)
    print(config)
