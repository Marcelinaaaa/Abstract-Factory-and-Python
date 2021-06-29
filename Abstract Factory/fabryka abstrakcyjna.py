class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}!'
        print(msg)

    def interact_with2(self, obstacle):
        act = obstacle.action2()
        msg = f'{self} the Frog encounters {obstacle} and {act}!'
        print(msg)


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class Worm:
    def __str__(self):
        return 'a worm'

    def action2(self):
        return 'eats it right now'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Frog World -------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()

    def make_obstacle2(self):
        return Worm()


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Wizard battles against {obstacle} and {act}!'
        print(msg)

    def interact_with2(self, obstacle):
        act = obstacle.action2()
        msg = f'{self} the Wizard battles against {obstacle} and {act}!'
        print(msg)


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class Devil:
    def __str__(self):
        return 'an evil devil'

    def action2(self):
        return 'kills it now'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()

    def make_obstacle2(self):
        return Devil()


def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you? ')
        age = int(age)
    except ValueError as err:
        print(f"Age {age} is invalid, please try again...")
        return (False, age)
    return (True, age)


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
        self.obstacle2 = factory.make_obstacle2()

    def play(self):
        self.hero.interact_with(self.obstacle)
        self.hero.interact_with2(self.obstacle2)

    def main():
        name = input("Hello. What's your name? ")
        valid_input = False
        while not valid_input:
            valid_input, age = validate_age(name)
        game = FrogWorld if age < 18 else WizardWorld
        environment = GameEnvironment(game(name))
        environment.play()


GameEnvironment.main()
