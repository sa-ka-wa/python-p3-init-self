#!/usr/bin/env python3

class Dog:
    def __init__(self, name,breed="Mutt"):
        self.name = name
        self.breed = breed

fido = Dog("fido")
snoopy = Dog("snoopy")
fido.breed = "Dalmatian"
snoopy.breed = "Beagle"

fido.breed
snoopy.breed

pass