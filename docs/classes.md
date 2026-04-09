# Classes

This is a starter README generated from the extension metadata. It currently lists each block and its tooltip.

## Scoped Variables

```scratch
set var [NAME] to [VALUE] in current scope
```
Creates or updates a variable in the current scope.

```scratch
(get var [NAME])
```
Gets the value of a variable visible from the current or outer scopes.

```scratch
<var [NAME] exists in [KIND v]?>
```
Checks whether a variable exists in the selected scope range.

```scratch
delete var [NAME] in current scope
```
Deletes a variable from the current scope.

```scratch
(all variables in [KIND v])
```
Returns all variable names visible in the selected scope range as an array.

```scratch
create local variable scope {
  more blocks
}
```
Runs the enclosed blocks inside a new local variable scope.

```scratch
bind [KIND v] variable [NAME] to current scope
```
Links a global or non-local variable into the current scope.

## Define Classes

```scratch
create class at var [NAME] (class being created) {
  more blocks
}
```
Creates a new class, stores it in the chosen variable.

```scratch
create subclass at var [NAME] with superclass [SUPERCLASS] (class being created) {
  more blocks
}
```

Creates a subclass with the given superclass, stores it in a variable.

```scratch
(create class named [NAME] (class being created))
```

Creates and returns a new class with the given name.

```scratch
(create subclass named [NAME] with superclass [SUPERCLASS] (class being created))
```
Creates and returns a new subclass with the given superclass.

```scratch
on class [CLASS] (class being created) {
  more blocks
}
```

Runs the enclosed blocks as if they were inside the selected class definition. This allows you to e.g. add methods to already defined classes.

```scratch
(class being created)
```

Returns the class currently being defined.

## Use Classes

```scratch
<is [SUBCLASS] a subclass of [SUPERCLASS] ?>
```
Checks whether one class inherits from another.

```scratch
(get superclass of [CLASS])
```
Returns the superclass of a class, or Nothing if it has none.

## Class Members (use within class)

## Define Instance Methods

```scratch
define instance method [NAME] (self) {
  more blocks
}
```
Defines an instance method on the current class.

```scratch
define [SPECIAL_METHOD v] instance method (self) {
  more blocks
}
```

Defines a special instance method.

```scratch
(self)
```
Reports the current instance inside a method.

```scratch
(call super method [NAME] with positional args [POSARGS])
```

Calls an instance method from the superclass of the current object.

```scratch
(call super init method with positional args [POSARGS])
```

Calls the superclass init method for the current object.

## Define Getters & Setters

```scratch
define getter [NAME] (self) {
  more blocks
}
```

Defines a getter method for an attribute on the current class.

```scratch
define setter [NAME] (self) (value) {
  more blocks
}
```

Defines a setter method for an attribute on the current class.

```scratch
(value)
```

Reports the incoming value inside a setter method.

## Define Operator Methods

```scratch
define operator method [OPERATOR_KIND v] (other value) {
  more blocks
}
```

Defines custom behavior for an operator on instances of the current class.

```scratch
(other value)
```

Reports the other operand inside an operator method.

## Define Static Methods & Class Variables

```scratch
on [CLASS] set class variable [NAME] to [VALUE]
```

Sets a class variable on the selected class.

```scratch
(get class variable [NAME] of [CLASS])
```

Gets a class variable from the selected class.

```scratch
on [CLASS] delete class variable [NAME]
```

Deletes a class variable from the selected class.

```scratch
define static method [NAME] {
  more blocks
}
```

Defines a static method on the current class.

```scratch
([PROPERTY v] names of class [CLASS])
```

Returns the names of members of the selected type for a class.

## Working with Instances

## Create & Inspect

```scratch
(create instance of class [CLASS] with positional args [POSARGS])
```
Creates an instance of a class and passes the given positional arguments to its init method.

```scratch
<is [INSTANCE] an instance of [CLASS] ?>
```
Checks whether an instance belongs to a class or one of its subclasses.

```scratch
(get class of [INSTANCE])
```
Returns the class that created an instance.

## Attributes

```scratch
on [INSTANCE] set attribute [NAME] to [VALUE]
```
Sets an attribute on an instance or calls its setter if one exists.

```scratch
(attribute [NAME] of [INSTANCE])
```
Gets an attribute from an instance or calls its getter if one exists.

```scratch
(all attributes of [INSTANCE])
```
Returns all direct instance attributes as an object.

## Call Methods

```scratch
(on [INSTANCE] call method [NAME] with positional args [POSARGS])
```
Calls an instance method on an object with positional arguments.

```scratch
(on [CLASS] call static method [NAME] with positional args [POSARGS])
```
Calls a static method on a class with positional arguments.

```scratch
(get static method [NAME] of [CLASS] as function)
```
Returns a static method from a class as a callable function value.

## Functions

## Configure Before Define

```scratch
configure next function: argument names [ARGNAMES] defaults [ARGDEFAULTS]
```
Configures the argument names and default values used by the next function or method definition.

## Define

```scratch
create function at var [NAME] {
  more blocks
}
```
Creates a function and stores it in the chosen variable.

```scratch
(create function named [NAME])
```

Creates and returns a function with the given name.

## Inside Functions & Methods

```scratch
return [VALUE]
```
Returns a value from the current function or method and exits it.

```scratch
add temporary variables extension
```
_button_

Loads the Temporary Variables extension if it is not already available.

## Use Functions

```scratch
(call function [FUNC] with positional args [POSARGS])
```
Calls a function value with positional arguments.

## Utilities

```scratch
([VALUE] as string)
```
Converts a value to its string form, using a class's special as string method when available.

```scratch
(typeof [VALUE])
```
Returns a readable type name for a value.

```scratch
<[VALUE1] is [VALUE2] ?>
```
Checks whether two values are exactly the same value (the same instance).

```scratch
(Nothing)
```
Returns the special Nothing value.

```scratch
execute expression [EXPR]
```
Evaluates the input expression without performing any additional action.

<script>
const scratchblocks = require("./scratchblocks.min.js");
scratchblocks.renderMatching('pre.blocks');
</script>
