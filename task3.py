# Код реализует 
# SELECT event.id, event.name, asset.id, asset.name FROM events as event 
# LEFT JOIN assets as asset ON event.asset_id = asset.id 
# ORDER BY event.id 
# LIMIT 100
#
events = [[4, '2024-03-28', 'Event4', 1],
          [1, '2024-03-26', 'Event1', 1],
          [6, '2024-03-29', 'Event6', 3],
          [3, '2024-03-28', 'Event3', 2],
          [5, '2024-03-29', 'Event5', None],
          [2, '2024-03-27', 'Event2', None],]

assets = [[4, 'Asset4'],
          [1, 'Asset1'],
          [3, 'Asset3'],
          [2, 'Asset2'],]

def query(events: list, assets: list) -> list:
    # Создание словарей для Assets и Events
    assets_dict = {asset[0]: asset[1] for asset in assets}
    events_dict = {event[0]: [event[0], event[2], event[-1]] for event in events}

    result = []
    
    # Объединяем таблицы по asset_id
    for event_id in events_dict:
        for asset in assets_dict:
            if asset in events_dict[event_id][2:]:
                result += [events_dict[event_id] + [assets_dict[asset]]]
            elif events_dict[event_id][2:][0] not in assets_dict and events_dict[event_id][:2][0] not in list(map(lambda x: x[0], result)):
                result += [events_dict[event_id] + [None]]
    result.sort(key=lambda x: x[0]) # Сортировка по 1 элементу event_id
    
    return result[:100]

result = query(events, assets)
for row in result:
    print(row)

