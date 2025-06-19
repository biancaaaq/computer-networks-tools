# Raport Traceroute 
# Domenii testate sunt:
- Australia - anu.edu.au :site-ul oficial al Universitatii Nationale din Australia
- China - baidu.cn :motor de cautare din China ~ Google-ul lor
- Africa de Sud - gov.za :site-ul guvernului Africii de Sud


# Rulări din locații diferite:
Am rulat din :
-VPS AWS (Frankfurt, Germania ) , iar rezultatele sunt in fiserele  cu _route.txt
-wifi-ul din Facultate :facultate.txt
-acasa: wifi digi   home.txt
-retea publica: wifi-ul din cafeneaua Tucano de langa facultate:_public.txt

#Hartă Traceroute – Rute colorate
Fiecare destinație are propria culoare:
- `anu.edu.au` → roșu
- `baidu.cn` → albastru
- `gov.za` → verde

 Fișierele se află în acest repository:

- `anu_route.txt`
- `anu_public.txt`
- `anu_home.txt`
- `anu_facultate.txt`
- `baidu_route.txt`
- `baidu_public.txt`
- `baidu_home.txt`
- `baidu_facultate.txt`
- `govza_route.txt`
- `govza_publictxt`
- `govza_home.txt`
- `govza_facultate.txt`
- `raport_traceroute.md`
- `raceroute.py`
-'harta_statica.py'



anu_route.txt
1. 13.53.0.207 → Stockholm, Stockholm, Sweden
2. 240.0.16.12 → N/A, N/A, N/A
3. 242.0.125.163 → N/A, N/A, N/A
4. 240.3.96.13 → N/A, N/A, N/A
5. 242.8.133.131 → N/A, N/A, N/A
6. 99.83.71.200 → Seattle, Washington, United States
7. 99.83.71.201 → Seattle, Washington, United States
8. 171.75.8.43 → Frankfurt am Main, Hesse, Germany
9. 217.163.113.74 → Acton, England, United Kingdom
10. 113.197.15.11 → Melbourne, Victoria, Australia
11. 138.44.161.3 → Canberra, Australian Capital Territory, Australia
12. 150.203.201.5 → Canberra, Australian Capital Territory, Australia
13. 150.203.201.33 → Canberra, Australian Capital Territory, Australia
14. 130.56.67.33 → Canberra, Australian Capital Territory, Australia
15. 130.56.66.249 (destinație atinsă) → Canberra, Australian Capital Territory, Australia

anu_home.txt
1. 172.31.112.1 → N/A, N/A, N/A
2. 192.168.100.1 → N/A, N/A, N/A
3. 10.0.25.81 → N/A, N/A, N/A
4. 10.30.5.65 → N/A, N/A, N/A
5. 10.220.138.248 → N/A, N/A, N/A
6. * → 
7. 10.221.96.21 → N/A, N/A, N/A
8. 195.66.225.227 → London, England, United Kingdom
9. * → 
10. * → 
11. * → 
12. * → 
13. * → 
14. * → 
15. * → 
16. * → 
17. 64.125.29.1 → Seattle, Washington, United States
18. 64.125.193.130 → Seattle, Washington, United States
19. 113.197.15.62 → Melbourne, Victoria, Australia
20. 113.197.15.12 → Melbourne, Victoria, Australia
21. 113.197.15.11 → Melbourne, Victoria, Australia
22. 138.44.161.3 → Canberra, Australian Capital Territory, Australia
23. 150.203.201.5 → Canberra, Australian Capital Territory, Australia
24. 150.203.201.33 → Canberra, Australian Capital Territory, Australia
25. 130.56.67.33 → Canberra, Australian Capital Territory, Australia
26. * → 
27. * → 
28. * → 
29. 130.56.66.249 → Canberra, Australian Capital Territory, Australia

anu_public.txt
1. 172.31.112.1 → N/A, N/A, N/A
2. 192.168.100.1 → N/A, N/A, N/A
3. 10.0.25.81 → N/A, N/A, N/A
4. 10.30.5.65 → N/A, N/A, N/A
5. 10.220.138.248 → N/A, N/A, N/A
6. * → 
7. 10.221.96.21 → N/A, N/A, N/A
8. 195.66.225.227 → London, England, United Kingdom
9. * → 
10. * → 
11. * → 
12. * → 
13. * → 
14. * → 
15. * → 
16. * → 
17. * → 
18. 64.125.193.130 → Seattle, Washington, United States
19. 113.197.15.62 → Melbourne, Victoria, Australia
20. 113.197.15.12 → Melbourne, Victoria, Australia
21. 113.197.15.11 → Melbourne, Victoria, Australia
22. 138.44.161.3 → Canberra, Australian Capital Territory, Australia
23. 150.203.201.5 → Canberra, Australian Capital Territory, Australia
24. 150.203.201.33 → Canberra, Australian Capital Territory, Australia
25. 130.56.67.33 → Canberra, Australian Capital Territory, Australia
26. * → 
27. * → 
28. * → 
29. 130.56.66.249 → Canberra, Australian Capital Territory, Australia



baidu_route.txt
1. 13.53.0.203 → Stockholm, Stockholm, Sweden
2. 240.0.16.14 → N/A, N/A, N/A
3. 242.0.124.165 → N/A, N/A, N/A
4. 240.0.96.4 → N/A, N/A, N/A
5. 242.1.100.35 → N/A, N/A, N/A
6. 100.100.2.120 → N/A, N/A, N/A
7. 81.173.22.57 → Frankfurt am Main, Hesse, Germany
8. 202.97.83.161 → Beijing, Beijing, China
9. * * *
10. * * *
11. 36.110.246.2 → Beijing, Beijing, China
12. 36.110.245.157 → Beijing, Beijing, China
13. * * *
14. 106.38.212.146 → Beijing, Beijing, China
15. * * *
16. * * *
17. * * *
18. * * *
19. * * *
20. * * *
21. * * *
22. * * *
23. * * *
24. * * *
25. * * *
26. * * *
27. * * *
28. * * *
29. * * *
30. * * *

baidu_home.txt
1. 172.31.112.1 → N/A, N/A, N/A
2. 192.168.100.1 → N/A, N/A, N/A
3. 10.0.25.81 → N/A, N/A, N/A
4. 10.30.5.65 → N/A, N/A, N/A
5. 10.220.138.248 → N/A, N/A, N/A
6. * → 
7. 213.249.122.17 → Warsaw, Mazovia, Poland
8. * → 
9. 212.133.94.190 → Berlin, State of Berlin, Germany
10. 202.97.83.161 → Beijing, Beijing, China
11. 202.97.54.53 → Beijing, Beijing, China
12. 202.97.61.229 → Beijing, Beijing, China
13. 36.110.245.126 → Beijing, Beijing, China
14. 36.110.249.70 → Beijing, Beijing, China
15. * → 
16. 106.38.212.146 → Beijing, Beijing, China
17. * → 
18. * → 
19. * → 
20. * → 
21. * → 
22. * → 
23. * → 
24. * → 
25. * → 
26. * → 
27. * → 
28. * → 
29. * → 
30. * → 

baidu_public.txt
1. 172.31.112.1 → N/A, N/A, N/A
2. 192.168.0.1 → N/A, N/A, N/A
3. 85.204.1.1 → Sector 1, București, Romania
4. 95.77.36.161 → Craiova, Dolj, Romania
5. 136.255.248.202 → Bucharest, București, Romania
6. 195.2.29.1 → Paris, Île-de-France, France
7. 195.2.27.198 → Paris, Île-de-France, France
8. 195.2.9.102 → Málaga, Andalusia, Spain
9. 223.119.65.181 → Kwai Chung, Kwai Tsing, Hong Kong
10. * → 
11. 223.120.14.174 → Kwai Chung, Kwai Tsing, Hong Kong
12. 221.183.55.110 → Guangzhou, Guangdong, China
13. 221.183.25.201 → Guangzhou, Guangdong, China
14. 221.183.89.122 → Guangzhou, Guangdong, China
15. * → 
16. 39.156.27.1 → Guangzhou, Guangdong, China
17. * → 
18. * → 
19. * → 
20. * → 
21. * → 
22. * → 
23. * → 
24. * → 
25. * → 
26. * → 
27. * → 
28. * → 
29. * → 
30. * → 



 govza_route.txt
Traceroute către gov.za [163.195.1.225]:
1. 52.93.129.202 → New York, New York, United States
2. 240.5.72.14 → N/A, N/A, N/A
3. 52.93.56.59 → London, England, United Kingdom
4. 196.60.9.254 → Johannesburg, Gauteng, South Africa
5. 168.209.132.138 → Johannesburg, Gauteng, South Africa
6. 168.209.90.80 → Johannesburg, Gauteng, South Africa
7. 168.209.90.83 → Johannesburg, Gauteng, South Africa
8. 168.209.135.141 → Johannesburg, Gauteng, South Africa
9. 197.97.72.34 → Johannesburg, Gauteng, South Africa
10. 163.195.3.73 → Cape Town, Western Cape, South Africa
11. * * *
12. * * *
13. * * *
14. * * *
15. * * *
16. * * *
17. * * *
18. * * *
19. * * *
20. * * *
21. * * *
22. * * *
23. * * *
24. * * *
25. * * *
26. * * *
27. * * *
28. * * *
29. * * *
30. * * *

gozva_home.txt

1. 172.31.112.1 → N/A, N/A, N/A
2. 192.168.100.1 → N/A, N/A, N/A
3. 10.0.25.81 → N/A, N/A, N/A
4. 172.19.212.1 → N/A, N/A, N/A
5. 10.220.184.161 → N/A, N/A, N/A
6. * → 
7. * → 
8. 154.54.38.245 → Bucharest, București, Romania
9. 130.117.3.137 → Frankfurt am Main, Hesse, Germany
10. 154.54.59.86 → Vienna, Vienna, Austria
11. 154.54.58.5 → Vienna, Vienna, Austria
12. 154.54.62.121 → Munich, Bavaria, Germany
13. 154.54.62.142 → Amsterdam, North Holland, The Netherlands
14. 154.54.56.93 → Amsterdam, North Holland, The Netherlands
15. 154.54.61.254 → London, England, United Kingdom
16. 149.6.148.134 → London, England, United Kingdom
17. 168.209.100.215 → Johannesburg, Gauteng, South Africa
18. 168.209.2.201 → Johannesburg, Gauteng, South Africa
19. 168.209.135.146 → Johannesburg, Gauteng, South Africa
20. 168.209.135.141 → Johannesburg, Gauteng, South Africa
21. 197.97.72.34 → Johannesburg, Gauteng, South Africa
22. 163.195.3.73 → Cape Town, Western Cape, South Africa
23. * → 
24. * → 
25. * → 
26. * → 
27. * → 
28. * → 
29. * → 
30. * → 

gozva_public.txt
1. 172.31.112.1 → N/A, N/A, N/A
2. * → 
3. 85.204.1.1 → Sector 1, București, Romania
4. 95.77.36.177 → Craiova, Dolj, Romania
5. 136.255.248.200 → Bucharest, București, Romania
6. 195.2.15.49 → Leeds, England, United Kingdom
7. 195.2.27.201 → Paris, Île-de-France, France
8. 129.250.66.45 → Singapore, North West, Singapore
9. * → 
10. * → 
11. 129.250.3.12 → London, England, United Kingdom
12. 129.250.5.57 → London, England, United Kingdom
13. 212.119.4.211 → London, England, United Kingdom
14. 168.209.138.133 → Johannesburg, Gauteng, South Africa
15. * → 
16. 168.209.90.83 → Johannesburg, Gauteng, South Africa
17. 168.209.135.141 → Johannesburg, Gauteng, South Africa
18. 197.97.72.34 → Johannesburg, Gauteng, South Africa
19. 163.195.3.73 → Cape Town, Western Cape, South Africa
20. * → 
21. * → 
22. * → 
23. * → 
24. * → 
25. * → 
26. * → 
27. * → 
28. * → 
29. * → 
30. * → 

Am observat ca atunci cand am rulat cu wifi-ul de la facultate, nu am obtinut rezultate, toate pachetele s-au pierdut.
