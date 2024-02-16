import psycopg2
import json

filename = "yugioh-cards-content.json"

conn = psycopg2.connect("dbname='' user='' host='' password='' port=''")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Cards(
  es_name text,
  es_lore text,
  en_name text,
  en_lore text,
  image text,
  card_type text,
  property text,
  effect_types text,
  ocg text,
  adv text,
  trad text,
  sets text,
  archseries text,
  counter text,
  action text,
  database_id text
)""")
insert_query = "INSERT INTO Cards VALUES"
values = "('{es_name}','{es_lore}','{en_name}','{en_lore}','{image}','{card_type}','{property}','{effect_types}','{ocg}','{adv}','{trad}','a','{archseries}','{counter}','{action}','{database_id}')"
f = open(filename)
cards = json.load(f)
count = 0
query_values = []
for card in cards:
  print(f"Card count: {count}", end='\r')
  query_values.append(values.format(
    es_name=((card.get("es_name") or "").replace("'", "")),
    es_lore=((card.get("es_lore") or "").replace("'", "")),
    en_name=((card.get("en_name") or "").replace("'", "")),
    en_lore=((card.get("en_lore") or "").replace("'", "")),
    image=((card.get("image") or "").replace("'", "")),
    card_type=((card.get("card_type") or "").replace("'", "")),
    property=((card.get("property") or "").replace("'", "")),
    effect_types=((card.get("effect_types") or "").replace("'", "")),
    ocg=((card.get("ocg") or "").replace("'", "")),
    adv=((card.get("adv") or "").replace("'", "")),
    trad=((card.get("trad") or "").replace("'", "")),
    archseries=((card.get("archseries") or "").replace("'", "")),
    counter=((card.get("counter") or "").replace("'", "")),
    action=((card.get("action") or "").replace("'", "")),
    database_id=((card.get("database_id") or "")).replace("'", "")))
  count+=1
insert_query += ','.join(query_values) + ";"
print("Insert query finished")
cur.execute(insert_query)
print("Data inserted in database")
conn.commit()
cur.close()
conn.close()
f.close()