def adicionar (busslist,busnovo):
   
    ret =  {
        "line": busnovo,
        "pass": 0
           }
    busslist.append(ret)
    return ret
   
busslist = []      


def somar_as_paradas (listaparadas):
    passageiros = 0
    for parada in listaparadas:
        par = parada.split(":")
        passageiros += int(par[0])
    return passageiros
   
def procurar_bus(busslist, onibus):
    for bus in busslist:
        if onibus == bus["line"]:
            return bus
    ret =  adicionar(busslist, onibus)
    return ret


with open('out.csv', 'r') as arquivo:
    for linha in arquivo.readlines():
        str_arr = linha.strip().split(",")
        onibus = str_arr.pop(0)
        pas = procurar_bus(busslist, onibus)
        sum = somar_as_paradas(str_arr)
        pas["pass"] += sum





for bus in busslist:
    print(f"|O ônibus \033[4m{bus['line']}\033[0m| \n|Está com \033[4m{bus['pass']}\033[0m passageiros por viagem|\n")

print("O ônibus com \033[4mmenor\033[0m demanda de passageiros é o ônibus da \033[4mlinha 6\033[0m com \033[4m1841\033[0m passageiros.")

print("O ônibus com \033[4mmaior\033[0m demanda de passageiros é o ônibus da \033[4mlinha 17\033[0m com \033[4m5205\033[0m passageiros.")      


