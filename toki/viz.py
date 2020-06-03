from typing import List

import graphviz as gv

from toki.type import Expr


def _get_entity_class_html(expr):
    class_template = '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="1" CELLPADDING="1">
      <TR>
        <TD>{}</TD>
      </TR>
      <TR>
        <TD>
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1">
          {}
          </TABLE>
        </TD>
      </TR>
    </TABLE>>'''

    class_name_template = '<BR ALIGN="LEFT" />  <I>{}</I> <BR ALIGN="LEFT" />'

    entity_title = class_name_template.format(
        '{} ({})'.format(expr.args[0], type(expr).__name__)
    )
    entity_attrs = []
    row_key_value_template = '{}{}{}'

    for k, v in expr.args[1].args[0].items():
        entity_attrs.append(
            row_key_value_template.format(
                k, v['type'], 'nullable' if v['nullable'] else 'non-nullable'
            )
        )

    return class_template.format(entity_title, '\n'.join(entity_attrs),)


def show_expr(expr: Expr):
    g = gv.Digraph(comment='Graph')
    g.attr('node', shape='none', rankdir='BT')

    edges: List = []
    g.node(str(type(expr)), _get_entity_class_html(expr))

    # edges.append((_get_fullname(b), _get_fullname(c)))

    g.edges(edges)
    return g
