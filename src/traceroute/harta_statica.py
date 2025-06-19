import matplotlib.pyplot as plt #sa creez graficul stil harta
from mpl_toolkits.basemap import Basemap #o extensie sa imi deseneze globul
import requests # cereri http pentru locatia ip-urilor
import re #regex sa iau ip-urile din fisier

def extrage_ipuri_din_fisier(nume_fisier):
    ipuri = []
    pattern = re.compile(r"\d+\.\s+([\d.]+)\s+→")
    with open(nume_fisier, 'r') as f:
        for linie in f:
            linie = linie.strip()
            match = pattern.match(linie)
            if match:
                ip = match.group(1)
                ipuri.append(ip)
    return ipuri

routes = {
    "anu.edu.au": extrage_ipuri_din_fisier("anu_route.txt"),
    "baidu.cn": extrage_ipuri_din_fisier("baidu_route.txt"),
    "gov.za": extrage_ipuri_din_fisier("govza_route.txt")
}

ip_coords = {}
def get_coords(ip):
    if ip in ip_coords:
        return ip_coords[ip]
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if r["status"] == "success":
            coord = (r["lat"], r["lon"])
            ip_coords[ip] = coord
            return coord
    except:
        pass
    return None


fig = plt.figure(figsize=(12, 7))
m = Basemap(projection='robin', lon_0=0)
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightgray', lake_color='lightblue')
m.drawmapboundary(fill_color='lightblue')

colors = {
    "anu.edu.au": 'red',
    "baidu.cn": 'blue',
    "gov.za": 'green'
}

for destinatie, ipuri in routes.items():
    coords_list = []
    for ip in ipuri:
        coord = get_coords(ip)
        if coord:
            x, y = m(coord[1], coord[0])
            coords_list.append((x, y))
    if len(coords_list) >= 1:
        x_vals, y_vals = zip(*coords_list)
        m.plot(x_vals, y_vals, color=colors[destinatie], linewidth=2.5, label=destinatie)

plt.title("Rute Traceroute public")
plt.legend(loc='lower left')
plt.tight_layout()
plt.savefig("harta_traceroute_route.png", dpi=200)
plt.show()
