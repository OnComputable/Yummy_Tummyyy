import graphviz

# Define the flowchart
flowchart = graphviz.Digraph(format='png')
flowchart.attr(rankdir='LR', size='8')

# Nodes
flowchart.node('Start', 'Start')
flowchart.node('Init', 'Initialize Restaurant\n(menu_items={}, book_table=[], customer_orders=[])')
flowchart.node('AddMenu', 'Add Menu Items')
flowchart.node('BookTable', 'Book Tables')
flowchart.node('OrderItems', 'Customer Orders')
flowchart.node('PrintMenu', 'Print Menu Items')
flowchart.node('PrintTables', 'Print Table Reservations')
flowchart.node('PrintOrders', 'Print Customer Orders')
flowchart.node('End', 'End')

# Edges
flowchart.edges([
    ('Start', 'Init'),
    ('Init', 'AddMenu'),
    ('AddMenu', 'BookTable'),
    ('BookTable', 'OrderItems'),
    ('OrderItems', 'PrintMenu'),
    ('PrintMenu', 'PrintTables'),
    ('PrintTables', 'PrintOrders'),
    ('PrintOrders', 'End')
])

# Render flowchart to a file
flowchart.render('restaurant_flowchart', cleanup=True)
