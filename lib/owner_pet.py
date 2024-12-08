

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns a list of the owner's pets."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Adds a pet to the owner, ensuring the pet is of type Pet."""
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self
        Pet.all.append(pet)

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Validate pet_type
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of: {', '.join(Pet.PET_TYPES)}")

        # Add pet to the global list
        Pet.all.append(self)

        # Assign owner if provided
        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        if owner:
            self.owner = owner

