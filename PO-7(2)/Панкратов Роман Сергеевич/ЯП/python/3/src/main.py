from typing import Optional


class InstanceCountMixin:
    __instance_counts = 0

    def __new__(cls, *args, **kwargs):
        InstanceCountMixin.__instance_counts += 1
        print(f"Create {cls.__name__}")
        return super().__new__(cls)

    @property
    def instance_counts(self) -> int:
        return self.__instance_counts

    def __del__(self):
        print(f"Del {self.__class__.__name__}")
        InstanceCountMixin.__instance_counts -= 1


class ReprMixin:
    def __repr__(self) -> str:
        patched_mro_classes = list(self.__class__.__mro__)
        patched_mro_classes.remove(InstanceCountMixin)
        allowed_classes = set(mro_class.__name__ for mro_class in patched_mro_classes)
        fields_to_print = set(field for field in dir(self) if field.split("__")[0][1:] in allowed_classes)

        return "{}({})".format(
            self.__class__.__name__,
            ", ".join(f"{field.split('__')[-1]}={getattr(self, field)}" for field in fields_to_print)
        )


class PartyMember(InstanceCountMixin, ReprMixin):
    def __init__(self, age: Optional[int] = None, name: Optional[str] = None, party_name: Optional[str] = None):
        self.__age = age
        self.__party_name = party_name
        self.__name = name

    @property
    def age(self) -> Optional[int]:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        self.__age = value

    @property
    def party_name(self) -> Optional[str]:
        return self.__party_name

    @party_name.setter
    def party_name(self, value: str) -> None:
        self.__party_name = value

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value


class SchoolBoy(InstanceCountMixin, ReprMixin):
    def __init__(self, age: Optional[int] = None, name: Optional[str] = None, height: Optional[float] = None):
        self.__age = age
        self.__name = name
        self.__height = height

    @property
    def age(self) -> Optional[int]:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        self.__age = value

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def height(self) -> Optional[int]:
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        self.__height = value


class Person(SchoolBoy):
    def __init__(
        self,
        age: Optional[int] = None,
        name: Optional[str] = None,
        height: Optional[float] = None,
        is_education: bool = False,
        earnings: Optional[float] = None
    ) -> None:
        super().__init__(age, name, height)
        self.__is_education = is_education
        self.__earnings = earnings

    @property
    def is_education(self) -> bool:
        return self.__is_education

    @is_education.setter
    def is_education(self, value: bool) -> None:
        self.__is_education = value

    @property
    def earnings(self) -> Optional[float]:
        return self.__earnings

    @earnings.setter
    def earnings(self, value: float) -> None:
        self.__earnings = value


class Teacher(Person):
    def __init__(
        self,
        age: Optional[int] = None,
        name: Optional[str] = None,
        height: Optional[float] = None,
        earnings: Optional[float] = None,
        focus: Optional[str] = None,
        status: Optional[str] = None
    ) -> None:
        super().__init__(age, name, height, True, earnings)
        self.__focus = focus
        self.__status = status

    @property
    def focus(self) -> Optional[str]:
        return self.__focus

    @focus.setter
    def focus(self, value: str) -> None:
        self.__focus = value

    @property
    def status(self) -> Optional[str]:
        return self.__status

    @status.setter
    def status(self, value: str) -> None:
        self.__status = value


def task_1():
    print("Task 1")
    age = int(input("Enter age: "))
    name = str(input("Enter name: "))
    party_name = str(input("Enter party_name: "))

    party_member = PartyMember()
    party_member.age = age
    party_member.name = name
    party_member.party_name = party_name
    print(party_member)

    party_member_with_constructor = PartyMember(age, name, party_name)
    print(party_member_with_constructor)

    print(f"Instance counts: {party_member_with_constructor.instance_counts}")


def task_2():
    print("Task 2")
    age = int(input("Enter age: "))
    name = str(input("Enter name: "))
    height = float(input("Enter height: "))

    school_boy = SchoolBoy()
    school_boy.age = age
    school_boy.name = name
    school_boy.height = height
    print(school_boy)

    school_boy_2 = SchoolBoy(age, name, height)
    print(school_boy_2)

    is_education = bool(input("Enter is education: "))
    earnings = float(input("Enter earnings: "))

    person = Person()
    person.age = age
    person.name = name
    person.height = height
    person.is_education = is_education
    person.earnings = earnings
    print(person)

    person_2 = Person(age, name, height, is_education, earnings)
    print(person_2)

    focus = str(input("Enter focus: "))
    status = str(input("Enter status: "))

    teacher = Teacher()
    teacher.age = age
    teacher.name = name
    teacher.height = height
    teacher.earnings = earnings
    teacher.focus = focus
    teacher.status = status
    print(teacher)

    teacher_2 = Teacher(age, name, height, earnings, focus, status)
    print(teacher_2)


def main():
    task_1()
    task_2()


if __name__ == "__main__":
    main()
