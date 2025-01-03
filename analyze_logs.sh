#!/bin/bash

echo "Отчет о логе веб-сервера" > report.txt
echo "========================" >> report.txt
   

log_file="access.log"
count=0
while IFS= read -r line; do
    count=$((count + 1))
done < "$log_file"

echo "Общее количество запросов:     $count" >> report.txt

awk '{ip=$1} !seen[ip]++ {count++} END {printf "Количество уникальных IP-адресов:      %d\n", count}' "$log_file" >> report.txt

awk '{method=$6; counts[method]++} END {printf "Количество запросов по методам:\n"; for (method in counts) {printf "%d %s\n", counts[method], method}}' access.log >> report.txt

awk '{url=$7; counts[url]++} END {print "Самый популярный URL:   " counts[url], url}' access.log >> report.txt

echo 'Отчет сохранен в report.txt'
