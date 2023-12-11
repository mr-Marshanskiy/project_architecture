import abc


# region Product
class Pet(abc.ABC):

    @abc.abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        pass

    def drink(self):
        pass


class Dog(Pet):
    def make_sound(self):
        return 'gav'


class Cat(Pet):
    def make_sound(self):
        return 'miau'


class Bird(Pet):
    def make_sound(self):
        return 'chirik-chirik'

# endregion


# region Creator
class PetFeeding(abc.ABC):

    def feed_pet(self):
        pet: Pet = self.create_pet()
        pet.eat()
        pet.drink()
        print(f'*{pet.make_sound()}* Thank you, master!')

    @abc.abstractmethod
    def create_pet(self):
        pass


class DogFeeding(PetFeeding):
    def create_pet(self):
        return Dog()


class CatFeeding(PetFeeding):
    def create_pet(self):
        return Cat()


class BirdFeeding(PetFeeding):
    def create_pet(self):
        return Bird()
# endregion


# region example
if __name__ == '__main__':
    NURSERY = ['cat', 'dog', 'cat', 'bird', 'bird', 'dog']
    feeding_factories = {
        'cat': CatFeeding,
        'dog': DogFeeding,
        'bird': BirdFeeding,
    }

    for pet in NURSERY:
        feeding = feeding_factories.get(pet)()
        feeding.feed_pet()

    '''
    Result:
        *miau* Thank you, master!
        *gav* Thank you, master!
        *miau* Thank you, master!
        *chirik-chirik* Thank you, master!
        *chirik-chirik* Thank you, master!
        *gav* Thank you, master!
    '''
# endregion
