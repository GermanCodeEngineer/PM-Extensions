# Classes Extension

**The classes extension** by [GermanCodeEngineer](https://github.com/GermanCodeEngineer/) provides Python-like **functions, classes, methods, variables** and many other features of Object Orientated Programming.

# Scoped Variables
---
```scratch
set var [NAME] to [VALUE] in current scope::#428af5
```
Creates or updates a variable in the current scope.

---
```scratch
(get var [NAME]::#428af5)
```
Gets the value of a variable visible from the current or outer scopes.

---
```scratch
<var [NAME] exists in [all scopes v]?::#428af5>
<var [NAME] exists in [local scope v]?::#428af5>
<var [NAME] exists in [global scope v]?::#428af5>
```
Checks whether a variable exists in the selected scope range.

---
```scratch
delete var [NAME] in current scope::#428af5
```
Deletes a variable from the current scope.

---
```scratch
(all variables in [all scopes v]::#428af5)
(all variables in [local scope v]::#428af5)
(all variables in [global scope v]::#428af5)
```
Returns all variable names visible in the selected scope range as an array.

---
```scratch
create local variable scope {
  more blocks
}::#428af5
```
Runs the enclosed blocks inside a new local variable scope.

---
```scratch
bind [non-local v] variable [NAME] to current scope::#428af5
bind [global v] variable [NAME] to current scope::#428af5
```
Links a global or non-local variable into the current scope.

<br><br>
# Define Classes

---
```scratch
create class at var [NAME] (class being created::#428af5) {
  more blocks
}::#428af5
```
Creates a new class, stores it in the chosen variable.

---
```scratch
create subclass at var [NAME] with superclass [SUPERCLASS] (class being created::#428af5) {
  more blocks
}::#428af5
```

Creates a subclass with the given superclass, stores it in a variable.

---
```scratch
(create class named [NAME] (class being created::#428af5)::#428af5)
```

Creates and returns a new class with the given name.

---
```scratch
(create subclass named [NAME] with superclass [SUPERCLASS] (class being created::#428af5)::#428af5)
```
Creates and returns a new subclass with the given superclass.

---
```scratch
on class [CLASS] (class being created::#428af5) {
  more blocks
}::#428af5
```

Runs the enclosed blocks as if they were inside the selected class definition. This allows you to e.g. add methods to already defined classes.

---
```scratch
(class being created::#428af5)
```

Returns the class currently being defined.

<br><br>
# Use Classes

---
```scratch
<is [SUBCLASS] a subclass of [SUPERCLASS] ?::#428af5>
```
Checks whether one class inherits from another.

---
```scratch
(get superclass of [CLASS]::#428af5)
```
Returns the superclass of a class, or Nothing if it has none.

<br><br>
# Class Members (use within class)

## Define Instance Methods

---
```scratch
definẹ instance method [NAME] (self::#428af5) {
  more blocks
}::#428af5
```
Defines an instance method on the current class.

---
```scratch
definẹ [init v] instance method (self::#428af5) {
}::#428af5
definẹ [as string v] instance method (self::#428af5) {
}::#428af5
```

Defines a special instance method.

---
```scratch
(self::#428af5)
```
Reports the current instance inside a method.

---
```scratch
(call super method [NAME] with positional args [POSARGS]::#428af5)
```

Calls an instance method from the superclass of the current object.

---
```scratch
(call super init method with positional args [POSARGS]::#428af5)
```

Calls the superclass init method for the current object.

<br><br>
## Define Getters & Setters

---
```scratch
definẹ getter [NAME] (self::#428af5) {
  more blocks
}::#428af5
```

Defines a getter method for an attribute on the current class.

---
```scratch
definẹ setter [NAME] (self::#428af5) (value::#428af5) {
  more blocks
}::#428af5
```

Defines a setter method for an attribute on the current class.

---
```scratch
(value::#428af5)
```

Reports the incoming value inside a setter method.

<br><br>
## Define Operator Methods

---
```scratch
definẹ operator method [left add v] (other value::#428af5) {
}::#428af5
definẹ operator method [right add v] (other value::#428af5) {
}::#428af5
// AND MANY MORE
definẹ operator method [right mod v] (other value::#428af5) {
}::#428af5
definẹ operator method [greater or equal v] (other value::#428af5) {
}::#428af5
// AND MANY MORE
```

Defines custom behavior for an operator on instances of the current class.

---
```scratch
(other value::#428af5)
```

Reports the other operand inside an operator method.

<br><br>
## Define Static Methods & Class Variables

---
```scratch
on [CLASS] set class variable [NAME] to [VALUE]::#428af5
```

Sets a class variable on the selected class.

---
```scratch
(get class variable [NAME] of [CLASS]::#428af5)
```

Gets a class variable from the selected class.

---
```scratch
on [CLASS] delete class variable [NAME]::#428af5
```

Deletes a class variable from the selected class.

---
```scratch
definẹ static method [NAME] {
  more blocks
}::#428af5
```

Defines a static method on the current class.

---
```scratch
([instance method v] names of class [CLASS]::#428af5)
([static method v] names of class [CLASS]::#428af5)
([getter method v] names of class [CLASS]::#428af5)
([setter method v] names of class [CLASS]::#428af5)
([operator method v] names of class [CLASS]::#428af5)
([class variable v] names of class [CLASS]::#428af5)
```

Returns the names of members of the selected type for a class.

<br><br>
## Working with Instances

<br><br>
## Create & Inspect

---
```scratch
(create instance of class [CLASS] with positional args [POSARGS]::#428af5)
```
Creates an instance of a class and passes the given positional arguments to its init method.

---
```scratch
<is [INSTANCE] an instance of [CLASS] ?::#428af5>
```
Checks whether an instance belongs to a class or one of its subclasses.

---
```scratch
(get class of [INSTANCE]::#428af5)
```
Returns the class that created an instance.

<br><br>
## Attributes

---
```scratch
on [INSTANCE] set attribute [NAME] to [VALUE]::#428af5
```
Sets an attribute on an instance or calls its setter if one exists.

---
```scratch
(attribute [NAME] of [INSTANCE]::#428af5)
```
Gets an attribute from an instance or calls its getter if one exists.

---
```scratch
(all attributes of [INSTANCE]::#428af5)
```
Returns all direct instance attributes as an object.

<br><br>
## Call Methods

---
```scratch
(on [INSTANCE] call method [NAME] with positional args [POSARGS]::#428af5)
```
Calls an instance method on an object with positional arguments.

---
```scratch
(on [CLASS] call static method [NAME] with positional args [POSARGS]::#428af5)
```
Calls a static method on a class with positional arguments.

---
```scratch
(get static method [NAME] of [CLASS] as function::#428af5)
```
Returns a static method from a class as a callable function value.

<br><br>
## Functions

<br><br>
## Configure Before Define

---
```scratch
configure next function: argument names [ARGNAMES] defaults [ARGDEFAULTS]::#428af5
```
Configures the argument names and default values used by the next function or method definition.

<br><br>
## Define

---
```scratch
create function at var [NAME] {
  more blocks
}::#428af5
```
Creates a function and stores it in the chosen variable.

---
```scratch
(create function named [NAME]::#428af5)
```

Creates and returns a function with the given name.

<br><br>
## Inside Functions & Methods

---
```scratch
return [VALUE]::#428af5
```
Returns a value from the current function or method and exits it.

---
```scratch
add temporary variables extension::#428af5
```
_button_

Loads the Temporary Variables extension if it is not already available.

<br><br>
## Use Functions

---
```scratch
(call function [FUNC] with positional args [POSARGS]::#428af5)
```
Calls a function value with positional arguments.

<br><br>
## Utilities

---
```scratch
([VALUE] as string::#428af5)
```
Converts a value to its string form, using a class's special as string method when available.

---
```scratch
(typeof [VALUE]::#428af5)
```
Returns a readable type name for a value.

---
```scratch
<[VALUE1] is [VALUE2] ?::#428af5>
```
Checks whether two values are exactly the same value (the same instance).

---
```scratch
(Nothing::#428af5)
```
Returns the special Nothing value.

---
```scratch
execute expression [EXPR]::#428af5
```
Evaluates the input expression without performing any additional action.

<script>
const scratchblocks = require("./scratchblocks.min.js");
scratchblocks.renderMatching('pre.blocks');
</script>
