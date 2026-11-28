"""Practice #51: dataclasses (attempt 2)."""

from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    age: int
    name: str = field(compare=False)


if __name__ == "__main__":
    people = [Person(age, name) for name, age in [('Dev', 35), ('Chen', 58), ('Ben', 62), ('Dev', 67)]]
    for p in sorted(people):
        print(p)
    oldest = max(people)
    assert oldest.age == max(age for _, age in [('Dev', 35), ('Chen', 58), ('Ben', 62), ('Dev', 67)])
