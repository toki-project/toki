from typing import List
from uuid import uuid4

import graphviz as gv

from toki import types as tt
from toki.types import Expr


def _get_entity_class_html(expr):
    expr_template = '''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="1">
      {}
      {}
    </TABLE>>'''

    expr_schema_template = '''
    <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1">
      {}
    </TABLE>
    '''

    expr_name_template = (
        '<TR><TD><BR ALIGN="LEFT" />  <I>{}</I> <BR ALIGN="LEFT" /></TD></TR>'
    )

    row_template = '<TR><TD>{}</TD></TR>'
    row_key_value_template = '<TR><TD><b>{}</b>: {} ({})</TD></TR>'

    schema_content = ''

    entity_title = expr_name_template.format(
        '<b>{}</b>: {}'.format(expr._display_name, type(expr).__name__)
    )

    entity_attrs = []

    if hasattr(expr, 'schema') and expr.schema:
        for k, v in expr.schema.structure.items():
            entity_attrs.append(
                row_key_value_template.format(
                    k,
                    v['type'],
                    'nullable' if v['nullable'] else 'non-nullable',
                )
            )
        schema_content = row_template.format(
            expr_schema_template.format('\n'.join(entity_attrs))
        )

    output = expr_template.format(entity_title, schema_content)
    return output


def visualize(expr: Expr) -> gv.Digraph:
    """
    Visualize a graph representation of an expression.

    Parameters
    ----------
    expr : Expr

    Returns
    -------
    gv.Digraph
    """
    g = gv.Digraph(comment='Graph')
    g.attr('node', shape='none', rankdir='BT')

    edges: List = []

    nodes: List = [expr]
    parent = None
    while len(nodes):
        node = nodes.pop(0)
        node_id = uuid4().hex
        g.node(node_id, _get_entity_class_html(node))
        if parent:
            edges.append((parent[0], node_id))
        parent = (node_id, node)
        if isinstance(node.args[0], tt.Expr):
            nodes.append(node.args[0])

    g.edges(edges)
    return g
