class Entity:
    def __init__(self, name1, strength1):
        if type(name1) == str:
            self._name = name1
        else:
            print('type ERROR')
        if not isinstance(strength1, float) and not isinstance(strength1, int):
            print('type ERROR')
        elif strength1 < 0:
            self._strength = 0
        elif strength1 > 5:
            self._strength = 5
        else:
            self._strength = strength1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            print('type ERROR')

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, new_strength):
        if not isinstance(new_strength, float) and not isinstance(new_strength, int):
            print('type ERROR')
        elif new_strength < 0:
            self._strength = 0
        elif new_strength > 5:
            self._strength = 5
        else:
            self._strength = new_strength

    def __gt__(self, other):
        if isinstance(self, Orc) and isinstance(other, Orc):
            if self.weapon and not other.weapon:
                return True
            elif not self.weapon and other.weapon:
                return False
            elif self._strength > other.strength:
                return True
            elif self._strength < other.strength:
                return False
        elif not isinstance(self, Orc) and isinstance(other, Orc):
            if not other.weapon:
                return True
            elif self._strength > other.strength:
                return True
            elif self._strength < other.strength:
                return False
        elif isinstance(self, Orc) and not isinstance(other, Orc):
            if not self.weapon:
                return False
            elif self._strength > other.strength:
                return True
            elif self._strength < other.strength:
                return False

    def __eq__(self, other):
        if self._strength == other.strength:
            return True

    def fight(self, other):
        if isinstance(self, Human) and isinstance(other, Human):
            print('Fight Error')
        elif self > other:
            if self._strength + 1 <= 5:
                self._strength += 1
            else:
                self._strength = 5
            print(self)
        elif other > self:
            if other.strength + 1 <= 5:
                other.strength += 1
            else:
                other.strength = 5
            print(other)
        elif other == self:
            if other.strength - 0.5 >= 0:
                other.strength -= 0.5
            else:
                other.strength = 0
            if self._strength - 0.5 >= 0:
                self._strength -= 0.5
            else:
                self._strength = 0
            print(self)
            print(other)


class Orc(Entity):
    def __init__(self, name1, strength1, weapon1):
        super().__init__(name1, strength1)
        if type(weapon1) != bool:
            print('type ERROR')
        else:
            self._weapon = weapon1

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, new_weapon):
        if type(new_weapon) != bool:
            print('type ERROR')
        else:
            self._weapon = new_weapon

    def __str__(self):
        return '%s %s %s' % (self.name, self.strength, self._weapon)


class Human(Entity):
    def __init__(self, name1, strength1, kingdom1):
        super().__init__(name1, strength1)
        if type(kingdom1) == str:
            self._kingdom = kingdom1
        else:
            print('type ERROR')

    @property
    def kingdom(self):
        return self._kingdom

    @kingdom.setter
    def kingdom(self, new_kingdom):
        if type(new_kingdom) == str:
            self._kingdom = new_kingdom
        else:
            print('type ERROR')


class Archer(Human):
    def __init__(self, name1, strength1, kingdom1):
        super().__init__(name1, strength1, kingdom1)

    def __str__(self):
        return '%s %s %s' % (self.name, self.strength, self.kingdom)


class Knight(Human):
    def __init__(self, name1, strength1, kingdom1, archers1):
        super().__init__(name1, strength1, kingdom1)
        self._archers = []
        if not isinstance(archers1, list):
            archers1 = list(archers1)
        for i in archers1:
            if not isinstance(i, Archer):
                print('Type Error')
            elif i.kingdom != self._kingdom:
                continue
            else:
                self._archers.append(i)

    @property
    def archers(self):
        return self._archers

    @archers.setter
    def archers(self, archers1):
        if not isinstance(archers1, list):
            archers1 = list(archers1)
        for i in archers1:
            if not isinstance(i, Archer):
                print('Type Error')
            elif i.kingdom != self.kingdom:
                continue
            else:
                self._archers.append(i)

    def __str__(self):
        archerlist = '['
        for i in self._archers:
            archerlist += str(i) + ', '
        archerlist = archerlist[:-2]
        archerlist += ']'
        return '%s %s %s %s' % (self.name, self.strength, self.kingdom, archerlist)
