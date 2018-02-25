leader = clan.cat_set.filter(position='LD')[0]
deputy = clan.cat_set.filter(position='DY')[0]
warriors = clan.cat_set.filter(position='WR')

dot = Digraph(name='clan_graph')
dot.format = 'png'
dot.node('L', leader.name)
dot.node('D', deputy.name)
for x in warriors:
    dot.node('W' + str(x.id), x.name)
    
    
dot.edge('L', 'D')
for x in warriors:
    dot.edge('D', 'W' + str(x.id))

dot.render(view=True)
