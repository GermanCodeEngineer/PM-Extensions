# OOP Extension

**The OOP extension** by [GermanCodeEngineer](https://github.com/GermanCodeEngineer/) provides Python-like object-oriented programming features in PenguinMod blocks.
> Highlights: **scoped variables**, **functions with defaults**, **classes and inheritance**, **getters/setters**, **operator methods**, **static methods**, **introspection**, and the special **`Nothing`** value.

Contents:
- [Feature List](#features)
- [Block List](#blocks)

Thanks to [jwklong](https://github.com/jwklong), [DogeisCut](https://github.com/dogeiscut), [Sharkpool](https://github.com/SharkPool-SP) and especially [**VeryGoodScratcher42**](https://github.com/Lego7set) for inspiration.

# Features

The OOP extension brings structured **object-oriented programming** and **scope-aware functions** into block-based projects.

## Quick Notes
- **Flexible inputs:** When a block expects a **class**, **instance**, or **function**, you can usually give either the value itself or the **name of a variable** that stores it.
- **Scope behavior:** Variables are resolved at **runtime** and only within the current **PM Script**. If you want to modify or delete an outer variable from inside a nested scope, **bind it first**.
- **Default arguments:** Default values automatically fill the **last positional arguments** when those trailing inputs are left out.
- **Class variables:** These are specially supported with blocks to **set**, **get**, **delete**, and **list** them.
- **`as string`:** This converts a value to readable text. For class instances, it calls the special **`as string`** method when one is defined.

## Block and Input Shapes
In this extension, the shapes of reporters indicate the **type of value**, they return. Input shapes indicate in the same way which type of value, they expect. Here are some examples for the existing shapes:
### Class
![Class Example](images/create_class_named.png)
### Class Instance
![Class Instance Example](images/create_instance_of.png)
### Function
![Function Example](images/create_function_named.png)
### Nothing
![Nothing Example](images/Nothing.png)
### Array (extension by jwklong)
![Array Example](images/all_variables_in.png)
### Object (extension by dogeiscut)
![Object Example](images/all_attributes_of.png)
### Any value (Normal round reporter)
![Anything Example](images/attribute_of.png)

## Scoped Variables and Scope Control
- Create, read, update, and delete variables in the **current scope**.
- Check whether a variable exists in **local**, **global**, or **all visible** scopes.
- Create temporary **local variable scopes** for safer nested logic.
- **Bind global or non-local variables** into the current scope so changes stay linked instead of copied.
- Variable context is limited to the current **PenguinMod Script**(e.g.a green flag block and the blocks below it), and outer names are resolved **at runtime**.
- Handle shadowing naturally: when the same name exists in multiple scopes, the **innermost** one is used first.

## Functions and Closures
- Create functions either **to store them in a variable** or **in a reporter block**.
- Configure the **next function's argument names and default values** before defining it.
- Default values fill the **last positional arguments** automatically when those trailing inputs are omitted.
- Call functions with positional arguments.
- Functions and methods can **capture outer variables** from where they were defined.
- Use `return` to exit a function or method cleanly with a result.

## Classes and Inheritance
- Create classes and subclasses either **in a variable** or **in a reporter block**.
- All class-related inputs accept either the **class value itself** or the **name of a variable** holding that class.
- Re-open an existing class with **`on class`** to add more members later.
- Access **`class being created`** while inside a class-definition context.
- Check subclass relationships and retrieve a class's **superclass**.

## Methods, Accessors, and Custom Behavior
- Define **instance methods**, **special methods** like `init` and `as string`, and **static methods**.
- Define **getters** and **setters** to control attribute reads and writes.
- Define **operator methods** to customize how instances behave with operators.
- Use helper values like **`self`**, **`value`**, and **`other value`** inside the appropriate method contexts.
- Call parent-class behavior with **`call super method`** and **`call super init method`**.

## Instances, Attributes, and Introspection
- Create instances with positional arguments passed to `init`.
- Inputs that expect an **instance** can use either the instance itself or the **name of a variable** holding it.
- Read and write attributes directly, or route access through getters and setters.
- Get **all attributes** of an instance for quick inspection.
- Check whether a value **is an instance of** a class, get its class, compare identity, and inspect its type.
- List class members by category, including **instance methods**, **static methods**, **getters**, **setters**, **operator methods**, and **class variables**.
- **Class variables are specially supported** with dedicated set/get/delete/list blocks for class-level metadata.

## Special Values and Utilities
- Use **`Nothing`** as a stable no-value similar to Python's `None`.
- Convert values to readable text with **`as string`**. On class instances that define it, this calls the special **`as string`** method.
- Use **`execute expression`** to evaluate reporter blocks inside scripts.
- Use the debugging helper to inspect the current **thread stacks and scopes** when needed.

# Blocks

## Scoped Variables
---
```scratch
set var [myVar] to [my value] in current scope::#428af5
```
- Creates or updates a variable in the current scope.

---
```scratch
(get var [myVar]::#428af5)
```
- Gets the value of a variable visible from the current or outer scopes.

---
```scratch
<var [myVar] exists in [all scopes v]?::#428af5>
<var [myVar] exists in [local scope v]?::#428af5>
<var [myVar] exists in [global scope v]?::#428af5>
```
- Checks whether a variable exists in the selected scope range.

---
```scratch
delete var [myVar] in current scope::#428af5
```
- Deletes a variable from the current scope.

---
```scratch
(all variables in [all scopes v]::#428af5)
(all variables in [local scope v]::#428af5)
(all variables in [global scope v]::#428af5)
```
- Returns all variable names visible in the selected scope range as an array.

---
```scratch
create local variable scope {
}::#428af5
```
- Runs the enclosed blocks inside a new local variable scope.

---
```scratch
bind [non-local v] variable [myVar] to current scope::#428af5
bind [global v] variable [myVar] to current scope::#428af5
```
- Links a global or non-local variable into the current scope. Because scope resolution happens at runtime, bind outer variables first if you want to modify or delete them from an inner scope.

<br><br>
## Define Classes

---
```scratch
create class at var [MyClass] (class being created::#428af5) {
}::#428af5
```
- Creates a new class, stores it in the chosen variable.

---
```scratch
create subclass at var [MySubclass] with superclass [MyClass] (class being created::#428af5) {
}::#428af5
```
- Creates a subclass with the given superclass, stores it in a variable.

---
```scratch
create class named [MyClass] (class being created::#428af5) {

}::#428af5
```
- *Note: This block is really a reporter with a branch, but it can not be rendered accurately here.*
- Creates and returns a new class with the given name.

---
```scratch
create subclass named [MySubclass] with superclass [MyClass] (class being created::#428af5) {
}::#428af5
```
- *Note: This block is really a reporter with a branch, but it can not be rendered accurately here.*
- Creates and returns a new subclass with the given superclass.

---
```scratch
on class [MyClass] (class being created::#428af5) {
}::#428af5
```
- Runs the enclosed blocks as if they were inside the selected class definition. This allows you to e.g. add methods to already defined classes.

---
```scratch
(class being created::#428af5)
```
- Returns the class currently being defined.

<br><br>
## Use Classes

---
```scratch
<is [MySubclass] a subclass of [MyClass] ?::#428af5>
```
- Checks whether one class inherits from another.

---
```scratch
(get superclass of [MySubclass]::#428af5)
```
- Returns the superclass of a class, or Nothing if it has none.

<br><br>
## Class Members

### Define Instance Methods

---
```scratch
definẹ instance method [myMethod] (self::#428af5) {
}::#428af5
```
- Defines an instance method on the current class.

---
```scratch
definẹ [init v] instance method (self::#428af5) {
}::#428af5
definẹ [as string v] instance method (self::#428af5) {
}::#428af5
```
- Defines a special instance method.

---
```scratch
(self::#428af5)
```
- Reports the current instance inside a method.

---
```scratch
(call super method [myMethod] with positional args (parse [\["argument1", "argument2"\]] as an array::#ff513d)::#428af5)
```
- Calls an instance method from the superclass of the current object.

---
```scratch
(call super init method with positional args (parse [\["argument1", "argument2"\]] as an array::#ff513d)::#428af5)
```
- Calls the superclass init method for the current object.

<br><br>
### Define Getters & Setters

---
```scratch
definẹ getter [myAttr] (self::#428af5) {
}::#428af5
```
- Defines a getter method for an attribute on the current class.

---
```scratch
definẹ setter [myAttr] (self::#428af5) (value::#428af5) {
}::#428af5
```
- Defines a setter method for an attribute on the current class.

---
```scratch
(value::#428af5)
```
- Reports the incoming value inside a setter method.

<br><br>
### Define Operator Methods

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
- Defines custom behavior for an operator on instances of the current class.

---
```scratch
(other value::#428af5)
```
- Reports the other operand inside an operator method.

<br><br>
### Define Static Methods & Class Variables

---
```scratch
on [MyClass] set class variable [myVariable] to [my value]::#428af5
```
- Sets a class variable on the selected class.

---
```scratch
(get class variable [myVariable] of [MyClass]::#428af5)
```
- Gets a class variable from the selected class.

---
```scratch
on [MyClass] delete class variable [myVariable]::#428af5
```
- Deletes a class variable from the selected class.

---
```scratch
definẹ static method [myMethod] {
}::#428af5
```
- Defines a static method on the current class.

---
```scratch
([instance method v] names of class [MyClass]::#428af5)
([static method v] names of class [MyClass]::#428af5)
([getter method v] names of class [MyClass]::#428af5)
([setter method v] names of class [MyClass]::#428af5)
([operator method v] names of class [MyClass]::#428af5)
([class variable v] names of class [MyClass]::#428af5)
```
- Returns the names of members of the selected type for a class.

<br><br>
## Working with Instances

<br><br>
### Create & Inspect

---
```scratch
(create instance of class [MyClass] with positional args (parse [\["argument1", "argument2"\]] as an array::#ff513d)::#428af5)
```
- Creates an instance of a class and passes the given positional arguments to its `init` method. The class input can be either a class value or the name of a variable holding one.

---
```scratch
<is [my instance] an instance of [MyClass] ?::#428af5>
```
- Checks whether an instance belongs to a class or one of its subclasses.

---
```scratch
(get class of [my instance]::#428af5)
```
- Returns the class that created an instance.

<br><br>
### Attributes

---
```scratch
on [my instance] set attribute [myAttr] to [my value]::#428af5
```
- Sets an attribute on an instance or calls its setter if one exists.

---
```scratch
(attribute [myAttr] of [my instance]::#428af5)
```
- Gets an attribute from an instance or calls its getter if one exists.

---
```scratch
(all attributes of [my instances]::#428af5)
```
- Returns all direct instance attributes as an object.

<br><br>
### Call Methods

---
```scratch
(on [my instance] call method [myMethod] with positional args (parse [\["argument1", "argument2"\]] as an array::#ff513d)::#428af5)
```
- Calls an instance method on an object with positional arguments. The instance input can be either the instance itself or the name of a variable holding it.

---
```scratch
(on [MyClass] call static method [myMethod] with positional args (parse [\["argument1", "argument2"\]] as an array::#ff513d)::#428af5)
```
- Calls a static method on a class with positional arguments. The class input can be either the class itself or the name of a variable holding it.

---
```scratch
(get static method [myMethod] of [MyClass] as function::#428af5)
```
- Returns a static method from a class as a callable function value.

<br><br>
## Functions

<br><br>
### Configure Before Define

---
```scratch
configure next function: argument names (parse [\["person", "message"\]] as an array::#ff513d) defaults (parse [\["Hello World!"\]] as an array::#ff513d)::#428af5
```
- Configures the argument names and default values used by the next function or method definition. Default values fill the last positional arguments when those trailing inputs are omitted.

<br><br>
### Define

---
```scratch
create function at var [myFunction] {
}::#428af5
```
- Creates a function and stores it in the chosen variable.

---
```scratch
create function named [myFunction] {
}::#428af5
```
- *Note: This block is really a reporter with a branch, but it can not be rendered accurately here.*
- Creates and returns a function with the given name.

<br><br>
### Inside Functions & Methods

---
```scratch
return [my value]::#428af5 cap
```
- Returns a value from the current function or method and exits it.

---
```scratch
(call function [myFunction] with positional args (parse [\["Bob", "Goodbye."\]] as an array::#ff513d)::#428af5)
```
- Calls a function value with positional arguments. The function input can be either the function itself or the name of a variable holding it.

<br><br>
### Utilities

---
```scratch
([my instance] as string::#428af5)
```
- Converts a value to its string form. On class instances that implement it, this calls the special `as string` method automatically.

---
```scratch
(typeof <true::operators>::#428af5)
(typeof (blank array::#ff513d)::#428af5)
(typeof (blank object::#f9bb58)::#428af5)
(typeof [my instance]::#428af5)
// And many more
```
- Returns a readable type name for a value.
- Possible return texts are:
	- `Function`
	- `Method`
	- `Getter Method`
	- `Setter Method`
	- `Operator Method`
	- `Class`
	- `Class Instance`
	- `Nothing`
	- `Boolean`
	- `Number`
	- `String`
	- `Array`
	- `Object`
	- `Date`
	- `Set`
	- `Lambda`
	- `Color`
	- `Unlimited Number`
	- `Target`
	- `XML`
	- `JavaScript Undefined`
	- `JavaScript Null`
	- `JavaScript BigInt`
	- `JavaScript Symbol`
	- `JavaScript Function`
	- `JavaScript Object`
	- `Unknown` *(shouldn't happen in practice; unrecognized values will usually return `JavaScript Object` instead)*

---
```scratch
<[my instance] is [other instance] ?::#428af5>
```
- Checks whether two values are exactly the same value (the same instance).

---
```scratch
(Nothing::#428af5)
```
- Returns the cool Nothing value like None in python.

---
```scratch
execute expression (call function [myFunction] with positional args (parse [\["Bob", "Goodbye."\]] as an array::#ff513d)::#428af5)::#428af5
```
- Evaluates the input expression without performing any additional action. This allows you to e.g. use the function call block (a reporter) in a script.
