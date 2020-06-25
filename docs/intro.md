# Toki - Data Expression API

**last update: 2020-06-24**

`Expression` is the base class used to create any kind of expression inside `toki`.

A `toki` expression is based on `metadsl` expression and, in general, it would create
expression for `types`, `datatypes` and `operations`.

```{note}
Note: Currently there is no way to change `__init__` or `__new__` methods of an expression class.
Each time an expression is instantiated, `metadsl` clones that expression, so the
`__new__` method is called again and receive some parameters used by the `metadsl` expression.
```

For now, we can define a method `expr` that will create a new expression for that class:

```python
e = Literal.expr(1, type='int64')
```

```{note}
Note: Every function, method or class should use typing.
```

Initially, Toki core has the follow main modules:

* api
* datatypes
* operations
* rules
* types

The main expression classes should use `Expr` suffix, so it would be easy to identify what classes
are the base classes, for example: `Expr`, `DataTypeExpr` `TypeExpr` and `OperationExpr`.
Generally, these classes are not used directly, it can be used for typing or as base or metaclass classes.

## API

`toki.api` is responsable to prepare `toki` API, create expression for each combination of
operations and types and datatypes.

## Data Types

`toki.datatypes` is responsible for defining all the data types expressions. Its main class
is `DataTypeExpr`. All the other data type classes shouldn't use the suffix `Expr`.

The initial `toki` plan is adding support for numeric, text, boolean and date/time data types.

Data types expressions can be created using `expression constructor functions`.
Generally, this constructors could be used with 1 positional parameter or a keyword `value`:

* for `Int64`: `int64(1)` or `int64(value=1)`
* for `Float64`: `float64(1.0)` or `float64(value=1.0)`
* for `Date`: `date('2020-02-02')` or `date('2020-02-02')`

Some expression constructors could have extra parameter, for example: `Decimal('1.1234', precision=4)`

```{note}
Note: Internally, this module is commonly abbreviated as `dts`.
```

## Operations

`toki.operations` is responsible for defining all the expression for operations, such as
`Add`, `Subtract`, etc. Its main class is `OperationExpr`. All the other operation classes
shouldn't use the suffix `Expr`. If it is a base operations used for other classes, the
suffix `Op` should be used (e.g. `BinaryOp`).

`toki` operations should have a `result_type` object that will be used to create a result expression.

This is a 2-steps expression: 1) it creates an instance of a operation expression and it
is used as parameter for 2) a instance of a `datatype`, `type` or another `operation` expression,
according to the `output_result`. It would looks similar to:

```
n1 = int64(1)
n2 = int64(2)

(n1 + n2) -> Add(left=n1, right=n2) -> IntegerScalar(parent=Add(left=n1, right=n2))
```

For the second step we could use the keyword `source` or `parent` or `value`. For now,
`parent` will be used because the expressions are nodes in a graph. But it is opened for discussion.


```{note}
Note: Internally, this module is commonly abbreviated as `ops`.
```

## Rules

`toki.rules` is responsible for defining all the expression types.

```{note}
Note: Internally, this module is commonly abbreviated as `rls`.
```

## Types

`toki.types` is responsible for defining all the expression types. For example the main `toki`
expression class is `Expr`


```{note}
Note: Internally, this module is commonly abbreviated as `tps`.
```

## Backends subpackage

`toki` aims to supply, initially, some base backends, such as `String Standard SQL` and `SQLAlchemy`,
so new backends could just inherit from one of these backends.

## General notes

* `toki` supports `python` >= 3.8.
