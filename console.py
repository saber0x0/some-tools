from rich.console import Console,OverflowMethod
from rich import print
from rich.json import JSON

console = Console(width=20)

console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("FOO", style="white on blue")
console.log("Hello, World!")
console.print_json('[false, true, null, "foo"]')
console.log(JSON('["foo", "bar"]'))
console.out("Locals", locals())
console.rule("[bold red]Chapter 2")
supercali = "supercalifragilisticexpialidocious"

overflow_methods: list[OverflowMethod] = ["fold", "crop", "ellipsis"]
for overflow in overflow_methods:
    console.rule(overflow)
    console.print(supercali, overflow=overflow, style="bold blue")
    console.print()





