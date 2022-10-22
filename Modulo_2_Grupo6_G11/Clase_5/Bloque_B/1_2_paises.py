paises = {
'Juan': {'Chile', 'Argentina'},
'Pedro': {'Francia', 'Suiza', 'Chile'},
'Diego': {'Chile', 'Italia', 'Francia', 'Peru'},
}


def cuantos_en_comun(a, b):
  return len(paises[a] & paises[b])

print("Hay", cuantos_en_comun("Diego","Pedro"), " en comun")