from repository.conexionMongoDB import conector_cluster

conector_cluster().Rose.Items.delete_many({})

inventario = [["+5 Dexterity Vest", 10, 20],
                  ["Aged brie", 2, 0],
                  ["Elixir of the Mongoose", 5, 7],
                  ["Sulfuras, Hand of Ragnaros", 0, 80],
                  ["Sulfuras, Hand of Ragnaros", -1, 80],
                  ["Backstage passes to a TAFKAL80ETC concert", 15, 20],
                  ["Backstage passes to a TAFKAL80ETC concert", 10, 49],
                  ["Backstage passes to a TAFKAL80ETC concert", 5, 49],
                  ["Conjured Mana Cake", 3, 6]]

inventarioDict = []                  
for item in inventario:
    inventarioDict.append({"name":item[0],"sell_in":item[1],"quality":item[2]})

conector_cluster().Rose.Items.insert_many(inventarioDict)