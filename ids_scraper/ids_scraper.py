from urllib.request import urlopen
import json

missing_subjects = {
    "Bilinguismo": {
        "id": 15419,
        "filterId": 116
    },
    "Cidadania Digital": {
        "id": 13556,
        "filterId": 117
    },
    "Democracia Plena, Responsabilidade e Estado de Direito": {
        "id": 0,
        "filterId": 118
    },
    "Direito Laboral": {
        "id": 0,
        "filterId": 119
    },
    "Educação e Cidadania Global Criativa": {
        "id": 14126,
        "filterId": 1110
    },
    "Educação, Cidadania e Direitos Humanos": {
        "id": 11773,
        "filterId": 11773
    },
    "Inglês Académico": {
        "id": 11738,
        "filterId": 1112
    },
    "Introdução à Língua e Cultura Russa": {
        "id": 15417,
        "filterId": 1113
    },
    "Literacia Fotográfica da Física à Mensagem": {
        "id": 15410,
        "filterId": 1114
    },
    "Matemática das Coisas": {
        "id": 10892,
        "filterId": 1115
    },
    "Princípios de Gestão de Inventários": {
        "id": 10986,
        "filterId": 1116
    },
    "Substâncias que Mudaram o Mundo": {
        "id": 12365,
        "filterId": 1117
    },
    "Sustentabilidade Ambiental, Social e Económica": {
        "id": 13403,
        "filterId": 1118
    },
    "Temas de Direito da Igualdade e Não Discriminação": {
        "id": 0,
        "filterId": 1119
    },
    "Tópicos de Astronomia e Cosmologia": {
        "id": 10886,
        "filterId": 1120
    }
}

def rename_dict_keys(dict: dict[str, any], original_name: str, new_name: str):
    print(f"\t{original_name} -> {new_name}")

    dict[new_name] = dict[original_name]
    del dict[original_name]

print("\nGetting Subject ids from manual scrape file made by CeSIUM.")

shifts_file = urlopen("https://raw.githubusercontent.com/cesium/calendarium/96169aac3d6771e3eb27c1f782a204fe85ba682c/data/shifts.json")
shifts = json.load(shifts_file)

ids = {}

for shift in shifts:
    if not shift["title"] in ids.keys():
        ids[shift["title"]] = {
            "id": shift["id"],
            "filterId": shift["filterId"]
        }

print("\nDoing little corrections (read more about on docs):")

rename_dict_keys(ids, "Cálculo para a Engenharia", "Cálculo para Engenharia")
rename_dict_keys(ids, "Álgebra Linear para a Engenharia", "Álgebra Linear para Engenharia")
rename_dict_keys(ids, "Análise Inteligente em Sistemas de 'Big Data'", "Análise Inteligente em Sistemas de \"Big Data\"")
rename_dict_keys(ids, "Métodos Numéricos e Otimização Não Linear", "Métodos Numéricos e Otimização não Linear")

print("\n\tAdding missing subjects - Opções Uminho (read more about on docs)")
ids = ids | missing_subjects

print("\nOrdering ids by filterId")
# Ordering by filterId -> subject keys will be ordered but year and semester number not; ex. 324 < 1212
ids = dict(sorted(ids.items(), key=lambda item: item[1]["filterId"]))
# Ordering by first two digits from filterId -> will order by year and semester number
ids = dict(sorted(ids.items(), key=lambda item: int(str(item[1]["filterId"])[:2])))

with open("ids.json", "w") as outfile:
    json.dump(ids, outfile, indent=2, ensure_ascii=False)

print(f"\nDone. Scraped {len(ids)} ids from the 'shifts.json' from CeSIUM!")
print(f"Check them at 'ids.json'\n")
