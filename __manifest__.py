{
    'name': 'Vista unificada de facturas',

    'summary': """
        Menús "Todas las Facturas" (facturas y rectificativas) para clientes y proveedores.
        """,

    'description': """
Listado unificado de facturas
=============================

Este módulo añade a Contabilidad/Facturación un listado único de facturas
que incluye, en la misma vista, tanto las facturas como las facturas
rectificativas (abonos), de forma que no sea necesario consultarlas por separado.

Funcionalidades
---------------
* **Clientes** (Facturación > Clientes > Todas las Facturas):
  muestra facturas emitidas y rectificativas de cliente
  (``out_invoice`` y ``out_refund``).
* **Proveedores** (Facturación > Proveedores > Todas las Facturas):
  muestra facturas recibidas y rectificativas de proveedor
  (``in_invoice`` y ``in_refund``).
* Vistas lista, kanban y formulario, reutilizando las vistas y filtros
  estándar de Odoo.
* Agrupación por defecto por diario y año de la fecha de factura.
* Límite de 1000 registros por página.
* Acceso restringido a los grupos de facturación y de contabilidad
  (solo lectura).

Notas técnicas
--------------
* No añade modelos ni campos: únicamente acciones de ventana y menús sobre
  ``account.move``.
* Depende del módulo ``account``.
""",

    'author': "motsoft",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing Management',
    'version': '15.0.0.1',

    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': [
        'account',
    ],

    # always loaded
    'data': [
        'views/account_move_menus.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
