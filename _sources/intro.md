# Toki - Data Expression API

**last update: 2020-06-24**

`Expression` is the base class used to create any kind of expressions inside `toki`.

A `toki` expression is based on `metadsl` expression and, in general, it would create
expressions for `types`, `datatypes` and `operations`.

```{note}
Currently there is no way to change `__init__` or `__new__` methods of an expression class.
Each time an expression is instantiated, `metadsl` clones that expression, so the
`__new__` method is called again and receives some parameters used by the `metadsl` expression.
```

For now, we can define a method `expr` that will create a new expression for that class:

```python
e = Literal.expr(1, type='int64')
```

```{note}
Every function, method or class should use typing.
```

Initially, Toki core has the following main modules:

* api
* datatypes
* operations
* rules
* types

The main expression classes should use `Expr` suffix, facilitating the identification of which classes
are the base classes, for example: `Expr`, `DataTypeExpr` `TypeExpr` and `OperationExpr`.
Generally, these classes are not used directly, they can be used for typing or as base or metaclass classes.

## API

`toki.api` is responsable for preparing `toki` API, creating expression for each combination of
operations and types and datatypes.

## Data Types

`toki.datatypes` is responsible for defining all the data type expressions. Its main class
is `DataTypeExpr`. All the other data type classes shouldn't use the suffix `Expr`.

The initial `toki` plan is to add support for numeric, text, boolean and date/time data types.

Data type expressions can be created using `expression constructor functions`.
Generally, these constructors could be used with 1 positional parameter or a keyword `value`:

* for `Int64`: `int64(1)` or `int64(value=1)`
* for `Float64`: `float64(1.0)` or `float64(value=1.0)`
* for `Date`: `date('2020-02-02')` or `date('2020-02-02')`

Some expression constructors could have extra parameters, for example: `Decimal('1.1234', precision=4)`

```{note}
Internally, this module is commonly abbreviated as `dts`.
```

## Operations

`toki.operations` is responsible for defining all the expressions for operations, such as
`Add`, `Subtract`, etc. Its main class is `OperationExpr`. All the other operation classes
shouldn't use the suffix `Expr`. If it is a base operation used for other classes, the
suffix `Op` should be used (e.g. `BinaryOp`).

`toki` operations should have a `result_type` object that will be used to create a result expression.

This is a 2-step expression: 1) it creates an instance of an operation expression and it
is used as a parameter for 2) an instance of a `datatype`, `type` or another `operation` expression,
according to the `result_type`. It would look similar to:

```
n1 = int64(1)
n2 = int64(2)

(n1 + n2) -> Add(left=n1, right=n2) -> IntegerScalar(parent=Add(left=n1, right=n2))
```

For the second step we could use the keyword `source` or `parent` or `value`. For now,
`parent` will be used because the expressions are nodes in a graph. But it is open for discussion.


```{note}
Internally, this module is commonly abbreviated as `ops`.
```

## Rules

`toki.rules` is responsible for defining all the expression types.

```{note}
Internally, this module is commonly abbreviated as `rls`.
```

## Types

`toki.types` is responsible for defining all the expression types. For example the main `toki`
expression class is `Expr`


```{note}
Internally, this module is commonly abbreviated as `tps`.
```

## Backends subpackage

`toki` aims to supply, initially, some base backends, such as `String Standard SQL` and `SQLAlchemy`,
so new backends could just inherit that.

## General notes

* `toki` supports `python` >= 3.8.
