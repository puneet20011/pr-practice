"""Practice #21: dataclasses (attempt 1)."""

from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    age: int
    name: str = field(compare=False)


if __name__ == "__main__":
    people = [Person(age, name) for name, age in [('Fay', 61), ('Gus', 67), ('Ben', 34), ('Fay', 58)]]
    for p in sorted(people):
        print(p)
    oldest = max(people)
    assert oldest.age == max(age for _, age in [('Fay', 61), ('Gus', 67), ('Ben', 34), ('Fay', 58)])
